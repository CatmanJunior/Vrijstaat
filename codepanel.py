import paho.mqtt.client as mqtt
import PygameUI as pg


GREY = [200,200,200]
WHITE= [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]

W, H = (1080,720)

BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry"
client = mqtt.Client(CLIENTNAME)
topic = "panel"
kasttopic = "MED"

codelist = "1234# 2345# 3793# 4600# 7777# 8888#".split()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)  # Subscribe to the topic
    client.subscribe(kasttopic)  # Subscribe to the topic
def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    if msg.topic == "panel":
    	txt.text = "Kleur Code: " + msg.payload
def MQTTConnect():
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

# client.publish(topic, msg)

#MQTTConnect()

pg.PyInit(W, H, FULLSCREENMODE=True)
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
g = 0;
print(codelist)
def CodeCheck(c):
	global g
	global code
	code += c
	codetxt.text = "Code: " + code
	print(code)
	if code == "#":
		return
	if c == "#":
		if code in str(codelist):
			print("yasss")
			client.publish(kasttopic, str(g + 1) + "A")
			g += 1
			codelist.remove(code)
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
