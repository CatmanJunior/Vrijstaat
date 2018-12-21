import MqttClass as mqtt

# MQTT Constants
BROKERIP = "192.168.178.40"
PORT = 1883
CLIENTNAME = "RaspberrryRadio"
mqtt.TOPICLIST.append("CRUSH")
client = mqtt.MakeClient(CLIENTNAME, autoconnect = True, ip = BROKERIP, port = PORT)


keywordlist = "t1 t2 b1	b2	kr	kl	rSw	rP f1	f2 time repeat".split()
	#t1 t2 	b1	b2	kr	kl	rSw	rP	f1	f2, time repeat 
orderlist = [
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	 0],
	[0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	5,	 0],
	[0,	0,	1,	0,	1,	1,	0,	0,	0,	0,	0,	 5],
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	 0],
	]

inputstate = [0]*12

#Skip first command
c = 1

def checkInput(client, userdata, msg):
	global c
	inputstate[m[0]] = m[1]
	for inp in range(len(keywordlist)):
		if inputstate[inp] == orderlist[c][inp] or inputstate[inp] == orderlist[c-1][inp]:
			# print(str(c) + " " + keywordlist[inp] + " yas")
			# print(orderlist[c][inp])
			# print(orderlist[c-1][inp])
			pass
		else:
			# print(str(c) + " " + keywordlist[inp] + " nah")
			return False
	c+=1	
	return True


mqtt.onmes = lambda x : checkInput(x)

while True:
	pass