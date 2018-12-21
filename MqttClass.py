import paho.mqtt.client as mqtt

client = None
MQTTON = True

TOPICLIST = []

def m(a):
    pass

def c(a):
    pass

oncon = c(0)
onmes = m(0)


def MakeClient(clientname)  :
    global client
    client = mqtt.Client(clientname)
    return client

def MQTTConnect(ip, port, on_con, on_mess):
    print("Connecting...")
    try:
        client.on_connect = on_con
        client.on_message = on_mess
        client.connect(ip, port=port, keepalive=180)
        client.loop_start()

        print("Connected to Mqtt server")
        return True
    except:
        print("Cannot connect to the Mqtt Server")
        return False

def SendMqtt(topic, msg):
    if MQTTON:
        client.publish(topic, msg)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in TOPICLIST:
        client.subscribe(topic)  # Subscribe to the topic
        print(topic)
    oncon()

def on_message(client, userdata, msg):
    # Convert the message to string. Original it is a byte printed as b'msg'
    msg.payload = str(msg.payload)[2:-1]
    print("New Message -> Topic: " + msg.topic +
          " Payload: " + str(msg.payload))
    onmes(msg.payload)