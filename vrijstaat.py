import datetime
import PygameUI as pg
import winsound
import json
from vrijstaatConst import *
from vrijstaatClass import *
import paho.mqtt.client as mqtt

#TODOLIST
"""
- Create logging system
- send sms/email when there is an error
    - when the program crash, send stacktrace including log
    - When an ESP is not connected send multiple restarts, give an error on screen and send e-mail/sms
- Send Email after each playtrough with data about the playtrough (times, hints given, player data)
- Create scalability
- The playtrough needs to be automated
    - Just give a start signal, and at some points a que where there isnt a device that controls the que
    - Gives signals when a certain phase is behind scedule. 
    - Give hints based on time and puzzles
- Text to speech for debugging
- Soundplayer based on phase
- Create a check button, which checks if everything is ready
    - ESPS connected
    - Every setting reset
-Activebox, turn visability off when there is a new menu popping up
-Hint system
    - Sending voice to bluetooth devices?
    - Hints to players trough lights?
    - Hint to gamemasters?
"""

# MQTT Constants
MQTTON = True
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry"
client = mqtt.Client(CLIENTNAME)

# Initial topiclist
# TODO: make ESP's add their own topic
TOPICLIST = ["poep", "t0", "SIGN", "HB", "relais1", "SP1", "relais"]

# Vars to identify ESPs
ESPs = ["HolletjesButtons"]  # What does this do?
ESPlist = []

# Add buttons to the ESP screen
RelaisButtons = {"Relais 1": lambda: SendMqtt("relais", "1"),
                 "Relais 2": lambda: SendMqtt("relais", "2"),
                 "Relais 3": lambda: SendMqtt("relais", "3"),
                 "Relais 4": lambda: SendMqtt("relais", "4")}

# Dict containing all ESP types, format: name
ESPtypes = {"relais": ["relais", RelaisButtons]}

#Puzzles
puzzleList = []
puzzles = {
			"Holletje"		:	["HolletjesButtons", "HolletjesServo"],
			"Kooitjes"		:	["Kooitjes"],
			"Terrarium"		:	["Terrarium"],
			"PoepScanner"	:	["Poep"],
			"Crusher"		: 	["Crusher"],
			"Medicein"		:	["Medicein"]}

#Phases
phases = {"A":[puzzles["Holletje"]]}


def SendMqtt(topic, msg):
    if MQTTON:
        client.publish(topic, msg)

def JSONdump(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

# Send signal to reset all ESPs, make them send the sign in signal again.
# Set hardreset to True to also make them restart
def resetESPS(hardreset=False):
    # NOT TESTED YET
    print("resetting")
    txtbox.addLine("Resetting")
    if hardreset:
        SendMqtt("SIGN", "1")
    else:
        SendMqtt("SIGN", "0")
    # Clear ESPlist
    # TODO: Create function within ESPmodule class to set a var for SIGNED
    ESPlist[:] = []


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in TOPICLIST:
        client.subscribe(topic)  # Subscribe to the topic


def on_message(client, userdata, msg):
        # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    # print the line to the inprogram terminal
    txtbox.addLine("New Message -> Topic: " + msg.topic +
                   " Payload: " + str(msg.payload))
    # Check if the topic matches any topic of the ESPs
    for esp in ESPlist:
        if esp.topic == msg.topic:
            esp.textbox.addLine(datetime.datetime.now().strftime(
                "%H:%M:%S") + ": " + msg.payload)
            txtbox.addLine("message add to: " + esp.name)

    if msg.topic == "SIGN":
        if msg.payload == "0" or msg.payload == "1":
        	pass
            #creates a loop so do this different, meant to also be called from a different ESP
            #resetESPS(hardreset=msg.payload)
        else:
            #if the send message in SIGN is in the ESPtype-dict, which keys contain the names.
            for topic in ESPtypes:
                if topic in msg.payload:
                    txtbox.addLine("Topic found: " + topic)
                    #Create a container for this ESP
                    container = pg.Container(
                        msg.payload + "Container", (535, 80), (530, 530), BLACK, visable=False, border = 5, bordercolor=WHITE)
                    #Create a ESP instance
                    #esptype[topic][0] contains the name
                    #esptype[topic][1] contains the buttons
                    ESPlist.append(
                        ESPModule(msg.payload, ESPtypes[topic][0], container, **ESPtypes[topic][1]))
                    txtbox.addLine("Module created: " + ESPtypes[topic][0])
                    #Add a button to the dropdown
                    ESPDropdownButton.addObject(pg.DropDown(msg.payload, (0, 50), 
                    	(80, 50), WHITE, msg.payload, function=lambda: container.setVisable(not container.visable)))
                    break
            else:
                txtbox.addLine("Topic not found in type list")

#Connect to the broker
def mqqtConnect():
    print("Connecting...")
    try:
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(BROKERIP, port=PORT, keepalive=180)
        client.loop_start()
        print("Connected")
        return True
    except:
        print("Cannot connect to the MQQT Server")
        return False

if MQTTON:
    mqqtConnect()

#init pygame from the PygameUI module
pg.PyInit(1080, 720)

container = pg.Container("name", (150, 100), (300, 300), BLACK, visable=True, border=2, bordercolor = WHITE)

ESPDropdownButton = pg.DropDownButton("ESP", (5, 5), (100, 50), WHITE, "ESPS", visable=True)

ResetButton = pg.Button(
    "Reset", (110, 5), (100, 50), WHITE, text="Reset ESPs", visable=True, function=lambda: SendMqtt("SIGN", "0"))

FakeButton = pg.Button(
    "Fake", (215, 5), (100, 50), WHITE, text="Fake", visable=True, function=lambda: SendMqtt("SIGN", "relais1"))

txtbox = pg.TextBox("Txtbox1", (5, 515), (500, 200), "TEXTBOX",
                    visable=True, showtitle=True, color=BLACK, max_lines=10, border = 2, bordercolor=WHITE)
txtbox.addLine("debugbox")

timer = pg.TimerObject()

TimerButton = pg.Button(
    "TimerButton", (320, 5), (100, 50), WHITE, text="0", visable=True, function=lambda: timer.reset())


def game():
    TimerButton.text = str(int(timer.currentTime/1000))

gameloop = True

while gameloop:
    game()
    gameloop = pg.GameLoop()
