import pygame
import PygameUI as pg
import winsound
from vrijstaatConst import *
from vrijstaatClass import *
import paho.mqtt.client as mqtt

BROKERIP = "192.168.178.40"
PORT = 1883
TOPICLIST = ["poep","t0", "SIGN", "HB", "relais1","SP1"]

CLIENTNAME = "Raspberrry"

client = mqtt.Client(CLIENTNAME)

signedList = []

ESPs = ["HolletjesButtons"]
ESPlist = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for topic in TOPICLIST:
		client.subscribe(topic) #Subscribe to the topic

def on_message(client, userdata, msg):
	print("New Message -> Topic: " + msg.topic + " Payload: " + str(msg.payload))
	if msg.topic == "SIGN":

		signedList.append(msg.payload)
		con = pg.Container("name", (100,100),(500,500),WHITE)
		# ESPlist.append(ESPModule(msg.payload, msg.payload, con))
		dropdownButton.addObject(pg.DropDown(msg.payload, (0,50),(80,30),WHITE, msg.payload, function = lambda : con.setVisable(not con.visable)))

def mqqtConnect():
	print("Connecting")
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

mqqtConnect()

pg.PyInit(1000,1000)

playButtonList = []

def play(file):
	winsound.PlaySound(soundlist[file], winsound.SND_FILENAME|winsound.SND_ASYNC)

def playlamb(z):
	return lambda : play(z)

groupA = Group("A")
groupB = Group("B")

pTuinA = Phase("Tuin", groupA)
pTuinB = Phase("Tuin", groupB)

kid1 = Kid(1)
kid1.setGroup(groupA)

container = pg.Container("name", (150,100),(300,300), WHITE, visable = True)
container.addObject(pg.Button("har", (200,60), (50,50), text = "haha", function = lambda : relaisContainer.setVisable(not relaisContainer.visable)))
container.addObject(pg.Text("a",(10,10), "Mqqt"))
container.addObject(pg.Text("a",(10,50), "Connected:"))
mqqttext = container.addObject(pg.Text("a",(10,80), "Mqqt"))

relaisContainer = pg.Container("name", (100,100),(500,500),WHITE)
relaisContainer.addObject(pg.Button("bla", (20,20), (50,50), color = WHITE, text = "Relais1", function=lambda : client.publish("SP1", "3")))
relaisContainer.addObject(pg.Button("bla", (90,20), (50,50), color = WHITE,text = "Relais2"))
relaisContainer.addObject(pg.Button("bla", (160,20), (50,50),color = WHITE, text = "Relais3"))
relaisContainer.addObject(pg.Button("bla", (230,20), (50,50),color = WHITE, text = "Relais4"))
relaisContainer.addObject(pg.Button("bla", (20,50), (50,50), color = WHITE, text = "Relais1", function=lambda : client.publish("SP1", "4")))

dropdownButton = pg.DropDownButton("ESP", (0,30),(100,50), WHITE, "ESPS", visable = True)

txtbox = relaisContainer.addObject(pg.TextBox("Txtbox1", (100,100),(300,300), "TEXTBOX", visable = True))
txtbox.addLine("GAGA")
txtbox.addLine("BLABLA")

# relaisContainer.setVisable(True)
dropdownButton.setVisable(True)

def game():

	_txt = ""
	for i in signedList: 
		_txt += str(i)[2:-1]
	mqqttext.text = _txt + '\n'
gameloop = True

while gameloop:
	game()
	gameloop = pg.GameLoop()