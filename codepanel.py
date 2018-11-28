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

codelist = "1234# 2345# 5555# 6666# 7777# 8888#".split()

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

MQTTConnect()

pg.PyInit(W, H)
BUTTONS = {
	"BUT" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(150,150),
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
	"START" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Fake",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},
}

buttonlist = "1 2 3 A 4 5 6 B 7 8 9 C * 0 # D ".split()

temp_container = pg.Container("main", **CONTAINER["MainContainer"])

# pg.Button("START", **CON["START"])

code = ""
g = 0;
print(codelist)
def CodeCheck(c):
	global g
	global code
	code += c
	print(code)
	if c == "#":
		if c in str(codelist):
			print("yasss")
			client.publish(kasttopic, g)
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
	tmp.rect.x = W/2-330+(j%4)*170
	
	tmp.rect.y = H/2-330+int((j/4))*170
	j+=1

# for c in CON:
# 	pg.ObjectDict["main"].addObject(pg.ObjectDict[c])

gameloop = True

while gameloop:
    # game()
    gameloop = pg.GameLoop()
