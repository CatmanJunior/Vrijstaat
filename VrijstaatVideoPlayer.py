import PygameUI as pg
from MqttClass import MakeClient, MQTTConnect, SendMqtt
import os

BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "MusicPlayer"
client = MakeClient(CLIENTNAME)

TOPICLIST = ["MusicPlayer", "IntroVideo"]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in TOPICLIST:
        client.subscribe(topic)  # Subscribe to the topic

def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    if msg.topic == TOPICLIST[0]:
        pg.PlaySound(msg.payload)
    if msg.topic == TOPICLIST[1]:
        os.system("omxplayer TinadeBioloog.mov")

#Connect to the broker
MQTTConnect(BROKERIP,PORT,on_connect,on_message)

#init pygame from the PygameUI module
pg.PyInit(1080, 720)

gameloop = True

def game():
	pass

os.system("omxplayer TinadeBioloog.mov")

while gameloop:
    game()
    gameloop = pg.GameLoop()
