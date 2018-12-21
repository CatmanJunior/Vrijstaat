import MqttClass

# MQTT Constants
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry2aaa"
client = MqttClass.MakeClient(CLIENTNAME)



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print(flags)
    print(userdata)
    print(rc)
    client.subscribe("SIGN/#")  # Subscribe to the topic

    oncon()

def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    onmes(msg.payload)

MqttClass.MQTTConnect(BROKERIP,PORT,on_connect,on_message)

while True:
	pass