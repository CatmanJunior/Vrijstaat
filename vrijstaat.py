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
	- Age
	- Group Size
	- Schools/weekend
- The playtrough needs to be automated
    - Just give a start signal, and at some points a que where there isnt a device that controls the que
    - Gives signals when a certain phase is behind scedule. 
    - Give hints based on time and puzzles
- Text to speech for debugging
	- Create file then play it and remove it when it's done
- Soundplayer based on phase
- Create a check button, which checks if everything is ready
    - ESPS connected
    - Every setting reset
-Hint system
    - Sending voice to bluetooth devices?
    - Hints to players through lights?
    - Hint to gamemasters?
-TypeBoxesESP
	- Color sensor
	- NumPad
	- Poep
- Seperate the layouts to a different file
- Soundplayer/mixer
- other raspberry to play a script on mqtt message
- adding sound effects on the right moment
"""

# MQTT Constants
MQTTON = True
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry"
client = mqtt.Client(CLIENTNAME)

# Initial topiclist
# TODO: make ESP's add their own topic
TOPICLIST = ["poep", "t0", "SIGN", "HB", "relais1", "SP1", "relais", "button"]

# Vars to identify ESPs
ESPs = ["HolletjesButtons"]  # What does this do?
ESPlist = []

# Add buttons to the ESP screen
RelaisButtons = {"Relais 1": lambda: SendMqtt("relais", "1"),
                 "Relais 2": lambda: SendMqtt("relais", "2"),
                 "Relais 3": lambda: SendMqtt("relais", "3"),
                 "Relais 4": lambda: SendMqtt("relais", "4")}

ButtonButtons = {"Button 1": lambda: SendMqtt("button", "1")}

# Dict containing all ESP types, format: name
ESPtypes = {"relais": ["relais", RelaisButtons],
			"button": ["button", ButtonButtons]}


CurrentPhase = 0
ActiveBox = 0
MainActiveBox = 0

def NextPhase():
	global CurrentPhase
	CurrentPhase+=1
	if CurrentPhase == 1:
		Intro()

def SetNewMainActiveBox(cont):
	global MainActiveBox
	if MainActiveBox != 0:
		MainActiveBox.setVisable(False)
	cont.setVisable(True)
	MainActiveBox = cont

def SetNewActiveBox(cont):
	global ActiveBox
	if ActiveBox != 0:
		ActiveBox.setVisable(False)
	cont.setVisable(True)
	ActiveBox= cont

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

    pg.ObjectDict["MainDebugTextBox"].addLine("Resetting")
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
    pg.ObjectDict["MainDebugTextBox"].addLine("New Message -> Topic: " + msg.topic +
                   " Payload: " + str(msg.payload))
    # Check if the topic matches any topic of the ESPs
    for esp in ESPlist:
        if esp.topic == msg.topic:
            esp.textbox.addLine(datetime.datetime.now().strftime(
                "%H:%M:%S") + ": " + msg.payload)
            pg.ObjectDict["MainDebugTextBox"].addLine("message add to: " + esp.name)

    if msg.topic == "SIGN":
        if msg.payload == "0" or msg.payload == "1":
        	pass
            #creates a loop so do this different, meant to also be called from a different ESP
            #resetESPS(hardreset=msg.payload)
        else:
            
            #if the send message in SIGN is in the ESPtype-dict, which keys contain the names.
            for topic in ESPtypes:
                if topic in msg.payload:
                    pg.ObjectDict["MainDebugTextBox"].addLine("Topic found: " + topic)
                    
                    #Create a ESP instance
                    #esptype[topic][0] contains the name
                    #esptype[topic][1] contains the buttons
                    esp = ESPModule(msg.payload, ESPtypes[topic][0], **ESPtypes[topic][1])
                    ESPlist.append(esp)
                    pg.ObjectDict["MainDebugTextBox"].addLine("Module created: " + ESPtypes[topic][0])
                    #Add a button to the dropdown
                    dr = pg.ObjectDict["ESPDropdownButton"].addObject(
                    	pg.DropDown(msg.payload + "Drop", msg.payload, **DROPDOWNITEM))
                    dr.function = lambda: SetNewActiveBox(esp.container)
                    break
            else:
                pg.ObjectDict["MainDebugTextBox"].addLine("Topic not found in type list")

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

for p in phases:
	o = Phase(phases[p]["Name"],"A",phases[p]["UI"])
	# for puz in phases[p]["puzzles"]:
	# 	o.addPuzzel(puz)
	phaseList.append(o)

for p in puzzles:
	o = Puzzel(p,puzzles[p])
	puzzleList.append(o)

gameTimer = pg.TimerObject()

pg.HeaderContainer("HeaderContainer", **HEADER)

for c in CONTAINERS:
	temp_container = pg.Container(c, **CONTAINERS[c]) 

for t in TEXTBOXES:
	temp_textbox = pg.TextBox(t, **TEXTBOXES[t])

for b in BUTTONS:
	temp_button = pg.Button(b, **BUTTONS[b])

for t in TEXTOBJECTS:
	temp_text = pg.Text(t, **TEXTOBJECTS[t])

for d in DROPDOWNBUTTONS:
	temp_drop = pg.DropDownButton(d, **DROPDOWNBUTTONS[d])

for c in CONTAINERS:
	for o in CONTAINERS[c]["objects"]:
		pg.ObjectDict[c].addObject(pg.ObjectDict[o])

for o in HEADER["objects"]:
	pg.ObjectDict["HeaderContainer"].addObject(pg.ObjectDict[o])

SetNewMainActiveBox(pg.ObjectDict["MainContainer"])

#Set button functions
pg.ObjectDict["NextPhaseButton"].function = lambda : NextPhase()
pg.ObjectDict["MainWindowButton"].function = lambda: SetNewMainActiveBox(pg.ObjectDict["MainContainer"])
pg.ObjectDict["ResetButton"].function = lambda:SendMqtt("SIGN", "0")
# pg.ObjectDict["StartGameButton"].function=lambda: StartGame()
pg.ObjectDict["FakeESPButton"].function=lambda: SendMqtt("SIGN", "relais1")

# TimerButton = pg.Button(
#     "TimerButton", (320, 5), (100, 50), WHITE, text="0", visable=True, function=lambda: gameTimer.reset())

for p in phaseList:
	pg.ObjectDict["PhaseDropdownButton"].addObject(pg.DropDown(p.name + "Drop", p.name, **DROPDOWNITEM))
	pg.ObjectDict[p.name+"Drop"].function= lambda : SetNewMainActiveBox(p.container)
	p.container.title = p.name

for p in puzzleList:
	pg.ObjectDict["PuzzelDropdownButton"].addObject(pg.DropDown(p.name + "Drop", p.name, **DROPDOWNITEM))
	pg.ObjectDict[p.name+"Drop"].function= lambda : SetNewActiveBox(p.container)
	p.container.title = p.name

def game():
    # TimerButton.text = str(int(gameTimer.currentTime/1000))
    pg.ObjectDict["GameTimerText"].text =  "Timer: " + str(int(gameTimer.currentTime/1000))


gameloop = True



def StartGame():
	pg.ObjectDict["MainProgressTextBox"].clear()
	gameTimer.reset()
	pg.ObjectDict["MainProgressTextBox"].addLine("Start time: " + datetime.datetime.now().strftime("%H:%M:%S"))
	pg.ObjectDict["MainProgressTextBox"].addLine("Current Phase: " + phaseList[CurrentPhase]["Name"])

def Intro():
	pg.ObjectDict["MainProgressTextBox"].lines[-1]= "Intro Start: " + datetime.datetime.now().strftime("%H:%M:%S")
	pg.ObjectDict["MainProgressTextBox"].addLine("Current Phase: " + phaseList[CurrentPhase]["Name"])

while gameloop:
    game()
    gameloop = pg.GameLoop()
