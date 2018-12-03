import datetime
import PygameUI as pg
import winsound
import json
from vrijstaatConst import *
from vrijstaatClass import *
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
- other raspberry to play a script on mqtt message
- adding sound effects on the right moment
"""

# MQTT Constants
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry"
client = MakeClient(CLIENTNAME)

CurrentPhase = 0
ActiveBox = 0
MainActiveBox = 0

def FakeAll():
	for e in ESPDict:
		SendMqtt("SIGN",ESPDict[e]["sign"])

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

def JSONdump(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def convertLambda(lamb, arg):
	return lambda : lamb(arg)

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
    DEBUGBOX.addLine("New Message -> Topic: " + msg.topic +
                   " Payload: " + str(msg.payload))
    # Check if the topic matches any topic of the ESPs
    for esp in ESPlist:
        if esp.topic == msg.topic:
            esp.textbox.addLine(datetime.datetime.now().strftime(
                "%H:%M:%S") + ": " + msg.payload)
            DEBUGBOX.addLine("message add to: " + esp.name)

    if msg.topic == "SIGN":
        if msg.payload == "0" or msg.payload == "1":
        	pass
            #creates a loop so do this different, meant to also be called from a different ESP
            #resetESPS(hardreset=msg.payload)
        else:
            #if the send message in SIGN is in the ESPtype-dict, which keys contain the names.
            for esp in ESPlist:
                if msg.payload == esp.name:
                    DEBUGBOX.addLine("ESP found: " + esp.name)
                    esp.Sign()
                    for p in puzzleList:
                        p.checkReady()
                    break
            else:
                DEBUGBOX.addLine("ESP unknown")

#Connect to the broker
MQTTConnect(BROKERIP,PORT,on_connect,on_message)

#init pygame from the PygameUI module
pg.PyInit(1080, 720)

gameTimer = pg.TimerObject()

pg.FromDict(HEADER)
pg.FromDict(MAINWINDOW, CONTAINERS["MainContainer"])
DEBUGBOX = pg.TextBox("MainDebugTextBox", **TEXTBOXES["MainDebugTextBox"])

#Set button functions
pg.ObjectDict["NextPhaseButton"].function = lambda : NextPhase()
pg.ObjectDict["MainWindowButton"].function = lambda: SetNewMainActiveBox(pg.ObjectDict["MainContainer"])
pg.ObjectDict["ResetButton"].function = lambda:SendMqtt("SIGN", "0")
# pg.ObjectDict["StartGameButton"].function=lambda: StartGame()
pg.ObjectDict["FakeESPButton"].function=lambda: FakeAll()

for esp in ESPDict:
    new_esp = ESPModule(**ESPDict[esp])
    ESPlist.append(new_esp)
    client.subscribe(new_esp.topic)
    #Add a button to the dropdown
    dd = pg.ObjectDict["ESPDropdownButton"].addObject(
    	pg.DropDown(ESPDict[esp]["sign"] + "Drop", esp, **DROPDOWNITEM))
    dd.function = convertLambda(SetNewActiveBox,new_esp.container)

for z in puzzles:
	puz = Puzzel(z)
	puzzleList.append(puz)
	dd = pg.DropDown(puz.name + "Drop", puz.name, **DROPDOWNITEM)
	pg.ObjectDict["PuzzelDropdownButton"].addObject(dd)
	dd.function = convertLambda(SetNewActiveBox,puz.container)
	puz.container.title = puz.name
	for e in puzzles[z]:
		for es in ESPlist:
			if es.name == e:
				puz.addESP(es)
				puz.but.function = convertLambda(SetNewActiveBox, es.container)

for p in phases:
	o = Phase(phases[p]["Name"],phases[p]["UI"])
	for puz in phases[p]["puzzles"]:
		for pu in puzzleList:
			if pu.name == puz:
				o.addPuzzel(pu)
	dd = pg.DropDown(p + "Drop", p, **DROPDOWNITEM)
	pg.ObjectDict["PhaseDropdownButton"].addObject(dd)
	dd.function = convertLambda(SetNewMainActiveBox, o.container)
	phaseList.append(o)

SetNewMainActiveBox(pg.ObjectDict["MainContainer"])

def game():
    pg.ObjectDict["GameTimerText"].text =  "Timer: " + str(int(gameTimer.currentTime/1000))

gameloop = True

def StartGame():
	DEBUGBOX.clear()
	gameTimer.reset()
	DEBUGBOX.addLine("Start time: " + datetime.datetime.now().strftime("%H:%M:%S"))
	DEBUGBOX.addLine("Current Phase: " + phaseList[CurrentPhase]["Name"])

def Intro():
	DEBUGBOX.lines[-1]= "Intro Start: " + datetime.datetime.now().strftime("%H:%M:%S")
	DEBUGBOX.addLine("Current Phase: " + phaseList[CurrentPhase]["Name"])

while gameloop:
    game()
    gameloop = pg.GameLoop()
