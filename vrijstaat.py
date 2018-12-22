import datetime
import PygameUI as pg
import winsound
import json
from vrijstaatConst import *
from vrijstaatClass import *
from vrijstaatESPs import *
from MqttClass import MakeClient, MQTTConnect, SendMqtt

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
    - Just give a start signal, and at some points a que where there isnt a device that controls the que.
    - Gives signals when a certain Room is behind scedule. 
    - Give hints based on time and puzzles.
- Text to speech for debugging
	- Create file then play it and remove it when it's done
- Soundplayer based on Room
- Create a check button, which checks if everything is ready
    - ESPS connected
    - Every setting reset
-Hint system
    - Sending voice to bluetooth devices?
    - Hints to players through lights?
    - Hint to gamemasters?
- other raspberry to play a script on mqtt message
- adding sound effects on the right moment
"""

# MQTT Constants
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry2"
client = MakeClient(CLIENTNAME)

CurrentRoom = 0
ActiveBox = 0
MainActiveBox = 0

def FakeAll():
	for e in ESPDict:
		SendMqtt("SIGN",ESPDict[e]["sign"])

def NextRoom():
	global CurrentRoom
	CurrentRoom+=1
	if CurrentRoom == 1:
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

def JSONdump(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def convertLambda(lamb, arg):
	return lambda : lamb(arg)

# Send signal to reset all ESPs, make them send the sign message again
# Set hardreset to True to also make them restart
def resetESPS(hardreset=False):
    for e in ESPlist:
        e.UnSign()
    DEBUGBOX.addLine("Resetting")
    if hardreset:
        SendMqtt("SIGN", "1")
    else:
        SendMqtt("SIGN", "0")
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # for topic in TOPICLIST:
    client.subscribe("#")  # Subscribe to the topic

def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))

    DEBUGBOX.addLine("New Message -> Topic: " + msg.topic +
                   " Payload: " + str(msg.payload))
    
    # Check if the topic matches any topic of the ESPs
    for esp in ESPlist:
        if esp.topic == msg.topic:
            esp.textbox.addLine(datetime.datetime.now().strftime(
                "%H:%M:%S") + ": " + msg.payload)
    
    if msg.topic == "SIGN":
        if msg.payload == "0" or msg.payload == "1":
        	pass
        elif msg.payload == "2":
            resetESPS()
        else:
            for esp in ESPlist:
                if msg.payload == esp.name:
                    DEBUGBOX.addLine("ESP found: " + esp.name)
                    esp.Sign()
                    break
            else:
                DEBUGBOX.addLine("ESP unknown")
        for p in puzzleList:
            p.checkReady()
                    
#Connect to the broker
MQTTConnect(BROKERIP,PORT,on_connect,on_message)

#init pygame from the PygameUI module
pg.PyInit(1080, 720, FULLSCREENMODE = False)

gameTimer = pg.TimerObject()

pg.FromDict(HEADER)
pg.FromDict(MAINWINDOW)
DEBUGBOX = pg.TextBox("MainDebugTextBox", **TEXTBOXES["MainDebugTextBox"])

#Set button functions
pg.ObjectDict["NextRoomButton"].function = lambda : NextRoom()
pg.ObjectDict["MainWindowButton"].function = lambda: SetNewMainActiveBox(pg.ObjectDict["MainContainer"])
pg.ObjectDict["ResetButton"].function = lambda: resetESPS()
# pg.ObjectDict["StartGameButton"].function=lambda: StartGame()
pg.ObjectDict["FakeESPButton"].function=lambda: FakeAll()

for esp in ESPDict:
    new_esp = ESPModule(**ESPDict[esp])
    client.subscribe(new_esp.topic)
    dd = pg.ObjectDict["ESPDropdownButton"].addObject(
    	pg.DropDown(ESPDict[esp]["sign"] + "Drop", esp, **DROPDOWNITEM))
    dd.function = convertLambda(SetNewActiveBox,new_esp.container)

for z in puzzles:
	puz = Puzzel(z)
	dd = pg.DropDown(puz.name + "Drop", puz.name, **DROPDOWNITEM)
	pg.ObjectDict["PuzzelDropdownButton"].addObject(dd)
	dd.function = convertLambda(SetNewActiveBox,puz.container)
	puz.container.title = puz.name
	for top in puzzles[z]:
		for es in ESPlist:
			if es.name == top:
				puz.addESP(es)
				puz.but.function = convertLambda(SetNewActiveBox, es.container)

for r in Rooms:
	room = Room(Rooms[r]["Name"],Rooms[r]["UI"])
	for room_puzzel in Rooms[r]["puzzles"]:
		for puzzel in puzzleList:
			if puzzel.name == room_puzzel:
				room.addPuzzel(puzzel)
	dd = pg.DropDown(room.name + "Drop", r, **DROPDOWNITEM)
	pg.ObjectDict["RoomDropdownButton"].addObject(dd)
	dd.function = convertLambda(SetNewMainActiveBox, room.container)
	RoomList.append(room)

SetNewMainActiveBox(pg.ObjectDict["MainContainer"])
def game():
    pg.ObjectDict["GameTimerText"].text =  "Timer: " + str(int(gameTimer.currentTime/1000))


gameloop = True

def StartGame():
	DEBUGBOX.clear()
	gameTimer.reset()
	DEBUGBOX.addLine("Start time: " + datetime.datetime.now().strftime("%H:%M:%S"))
	DEBUGBOX.addLine("Current Room: " + RoomList[CurrentRoom]["Name"])

def Intro():
	DEBUGBOX.lines[-1]= "Intro Start: " + datetime.datetime.now().strftime("%H:%M:%S")
	DEBUGBOX.addLine("Current Room: " + RoomList[CurrentRoom]["Name"])

while gameloop:
    game()
    gameloop = pg.GameLoop()
