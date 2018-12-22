# goto terminal and typ
# pip install paho-mqtt
# pip install pyglet 

import paho.mqtt.client as mqtt
import pygame

pygame.init()
window = pygame.display.set_mode((50,50))
clock = pygame.time.Clock()

BROKERIP = "192.168.178.40"
PORT = 1883
TOPICLIST = ["LAB/RELAIS/POE","t0"]

CLIENTNAME = "Raspberrry"

client = mqtt.Client(CLIENTNAME)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for topic in TOPICLIST:
		client.subscribe(topic) #Subscribe to the topic

def on_message(client, userdata, msg):
	print("New Message -> Topic: " + msg.topic + " Payload: " + str(msg.payload))

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

while True:
	clock.tick (180)

pygame.quit()
