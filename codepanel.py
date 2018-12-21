import paho.mqtt.client as mqtt
import PygameUI as pg

FULLSCREEN = False

GREY = [200,200,200]
WHITE= [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]

W, H = (1080,720)

BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "LabBerry"
client = mqtt.Client(CLIENTNAME)
topic = "LAB/PANEL/#"
kasttopic = "LAB/MEDKAST/#"
crushertopic = "LAB/CRUSHER/#"
c=1

codelist = "1234# 2345# 3793# 4600# 7777# 8888#".split()

def keymethod(key):
	print(key)
	if key in range(256,266):
		client.publish(topic, str(key-256))
		CodeCheck(str(key-256))
	if key == 271:
		client.publish(topic, "Enter")
		CodeCheck("#")

	
pg.KeyMethod = keymethod
keywordlist = "null t1 t2 b1 b2	kr	kl	rSw	rP f1 f2 time repeat".split()
	#0	t1 	t2 	b1	b2	kr	kl	rSw	rP	f1	f2 time repeat 
orderlist = [
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	 0,0],
	[0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	 0,0],
	[0,	0,	0,	1,	0,	1,	1,	0,	0,	0,	0,	 0,5],
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	 0,0],
	[0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	 5,0],
	[0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	 0,0],
	]

inputTimer = pg.TimerObject()

inputstate = [0]*13

#Skip first command
state = 1
counter = 0
def checkInput(inp, msg):
	global state
	global counter
	print(inp + msg)
	if inp in keywordlist:
		inp_num = keywordlist.index(inp)
		inputstate[inp_num] = int(msg)
		print(keywordlist[inp_num] + "set to: " + msg)
	else:
		return True
	print (inputstate)
	print (orderlist[state])
	print("counter: " + str(counter))
	for inp_num in range(len(keywordlist)-4):
		
		if inputstate[inp_num] == orderlist[state][inp_num]:
			print("Right key: " + keywordlist[inp_num])
		elif inputstate[inp_num] == orderlist[state-1][inp_num]:
			print("previous key was right")
			return True
		else:
			print("Wrong key: " + keywordlist[inp_num])
			state = 1
			return False
	inputTimer.reset()
	if inputTimer.currentTime > orderlist[state][-2]:
		if orderlist[state][-1] == 0:
			state+=1
			inputTimer.reset()
		elif orderlist[state][-1]-1 == counter:
			print(counter)
			state+=1
			inputTimer.reset()
			counter = 0	
		else: 
			counter+= 1
			print(counter)
			state -= 1

	print("move to next state: " + str(state))
	
	if state == 8:
		state = 1
	return True

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic) # Subscribe to the topic
    client.subscribe(kasttopic) # Subscribe to the topic
    client.subscribe(crushertopic) 

def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    if msg.topic == topic[:-1]:
    	txt.text = "Kleur Code: " + msg.payload
    if msg.topic.startswith(crushertopic[:-1]):
    	checkInput( msg.topic[len(crushertopic[:-1]):],msg.payload)

def on_log(client, userdata, level, buff):
	# print(client)
	# print(userdata)
	# print(level)
	# print(buff)
	pass

def MQTTConnect():
    print("Connecting...")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_log = on_log
    client.connect(BROKERIP, port=PORT, keepalive=180)
    client.loop_start()
    print("Connected")
    return True
    
# client.publish(topic, msg)

MQTTConnect()

pg.PyInit(W, H, FULLSCREENMODE=FULLSCREEN)
BUTTONS = {
	"BUT" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,100),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Fake",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},
}

CONTAINER = {


		"MainContainer" : {
		"location"		:	(0, 0),
		"size"			:	(W, H),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	8,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Main",
		"showtitle"		:	True,
		},

}
CON = {
	"codetxt" : {
			"location"		:	(50,H - 50),
			"size"			:	(50,50),
			"color"			:	WHITE,
			"visable"		:	True,
			"text"			:	"Code: ",
			"fontsize"		:	30,
			},
					"BLA" : {
		"location"		:	(W/2, 0),
		"size"			:	(10, H),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	8,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Main",
		"showtitle"		:	True,
		},

		"ColorText" : {
			"location"		:	(600,H/2),
			"size"			:	(50,50),
			"color"			:	WHITE,
			"visable"		:	True,
			"text"			:	"Kleur Code: ",
			"fontsize"		:	30,
			},

}

buttonlist = "1 2 3 A 4 5 6 B 7 8 9 C * 0 # D ".split()

temp_container = pg.Container("main", **CONTAINER["MainContainer"])
codetxt = pg.Text("codetxt", **CON["codetxt"])
txt = pg.Text("ColorText", **CON["ColorText"])
grrt = pg.Container("ColorTexaat", **CON["BLA"])
code = ""
g = 0
print(codelist)

kastlist = "3 2 1 6 5 4".split()

def CodeCheck(c):
	global g
	global code
	global codelist
	code += c
	codetxt.text = "Code: " + code
	print(code)
	if code == "#":
		return
	if c == "#":
		if code in str(codelist):
			print("yasss")
			client.publish(kasttopic, "a" + str(kastlist[g]) + "B")
			g += 1
			codelist.remove(code)
		if code == "1111#":
			codelist = "1234# 2345# 3793# 4600# 7777# 8888#".split()
			client.publish("SIGN", 1)
			g = 0

		code = ""


def convert(g):
	return lambda : CodeCheck( g)

j = 0
for i in buttonlist:
	tmp = pg.Button(i, **BUTTONS["BUT"])
	tmp.function =  convert(i)
	tmp.text = i
	tmp.rect.x = 20+(j%4)*110
	
	tmp.rect.y = H/2-215+int((j/4))*110
	j+=1

# for c in CON:
# 	pg.ObjectDict["main"].addObject(pg.ObjectDict[c])

gameloop = True

while gameloop:
    # game()
    gameloop = pg.GameLoop()
