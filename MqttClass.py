import paho.mqtt.client as mqtt

BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "Raspberrry"
client = mqtt.Client(CLIENTNAME)

def MQTTConnect(oncon, ):
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

client.publish(topic, msg)

if MQTTON:
    mqqtConnect()