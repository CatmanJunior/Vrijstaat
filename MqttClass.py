import paho.mqtt.client as mqtt

client = None
MQTTON = True

def MakeClient(clientname):
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
        # print(msg)
        client.publish(topic, msg)
