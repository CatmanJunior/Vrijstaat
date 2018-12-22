import PygameUI as pg
from vrijstaatConst import *

class Group():
	def __init__(self, name, aantal, age, roomlist):
		self.name = name
		self.aantal = aantal
		self.age = age
		self.Room = 0
		self.RoomList = roomlist
		
	def nextRoom(self):
		self.Room += 1


class Room():
	def __init__(self, name, ui):
		self.name = name
		self.puzzels = []
		self.active = False
		self.done = False
		self.timer = pg.TimerObject()
		self.container = pg.FromDict(ui)
		
	def startTimer(self,timer):
		self.timer.reset()

	def addPuzzel(self, puzzel):
		self.puzzels.append(puzzel)

	def setActive(self):
		self.active = True

	def setDone(self):
		self.done = True

class Puzzel():
	def __init__(self, name):
		self.name = name
		self.container = pg.Container(self.name + "Container", **TEMPLATE["SubContainer"])
		self.butContainer = pg.Container(self.name + "PuzButContainer", **ESPUI["ButtonContainer"])
		self.readyText = pg.Text(self.name + "ReadyText", **ESPUI["SignedText"])
		self.readyText.text = "Ready: NO"
		self.container.addObject(self.readyText)
		self.container.addObject(self.butContainer)
		self.esps = []
		self.ready = False
		puzzleList.append(self)

	def addESP(self,esp):
		self.esps.append(esp)
		self.but = self.container.addObject(pg.Button(self.name + esp.name + "Button", **TEMPLATE["MiddleButton"]))
		self.but.text = esp.name
		self.butContainer.addObject(self.but)

	def checkReady(self):
		for e in self.esps:
			if not e.signed:
				self.readyText.text = "Ready: NO"
				pg.ObjectDict[self.name + "Drop"].realColor = pg.RED		
				return False
		self.readyText.text = "Ready: YES"
		pg.ObjectDict[self.name + "Drop"].realColor = pg.GREEN		
		self.ready = True
		return True


class Kid():
	def __init__(self, iden):
		self.id = iden
		self.group = ""

	def setGroup(self, group):
		self.group = group
		group.kidList.append(self)


class ESPModule():
	def __init__(self, **kwargs):
		self.name = kwargs["sign"]
		self.topic = kwargs["topic"]
		self.container = pg.Container(self.name + "ESPContainer", **ESPUI["MainContainer"])
		self.butContainer = pg.Container(self.name + "ESPButContainer", **ESPUI["ButtonContainer"])
		self.container.addObject(self.butContainer)
		self.textbox = self.container.addObject(
			pg.TextBox(self.name + "ESPMqttTextBox", **ESPUI["ESPMqttTextBox"]))
		self.container.title = self.name
		self.signedtext = pg.Text(self.name + "ESPsignedText", **ESPUI["SignedText"])
		self.container.addObject(self.signedtext)   
		self.signed = False
		self.emptybutton = pg.Button(self.name + "Emptybutton", **ESPUI["EmptyButton"])
		self.emptybutton.function = lambda : self.Empty()
		self.container.addObject(self.emptybutton)
		TOPICLIST.append(self.topic)
		ESPlist.append(self)

		if "outputs" in kwargs:
			pg.FromDict(kwargs["outputs"],self.butContainer)

	def Empty(self):
		self.textbox.lines = []

	def Sign(self):
		self.signed = True
		self.signedtext.text = "Signed: YES"
		pg.ObjectDict[self.name + "Drop"].realColor = pg.GREEN
		for puz in puzzleList:
			if self in puz.esps:
				pg.ObjectDict[puz.name + self.name + "Button"].realColor = pg.GREEN
	
	def UnSign(self):
		self.signed = False
		self.signedtext.text = "Signed: NOPE"
		pg.ObjectDict[self.name + "Drop"].realColor = pg.RED
		for puz in puzzleList:
			if self in puz.esps:
				pg.ObjectDict[puz.name + self.name + "Button"].realColor = pg.RED
