import PygameUI as pg
from vrijstaatConst import *

class Group():
	def __init__(self, name):
		self.name = name
		self.phase = 0
		self.phases = []
		self.kidList = []

	def addKid(self, kid):
		self.kidList.append(kid)
		kid.group = self

	def setPhase(self, phase):
		self.phase = phase

class Phase():
	def __init__(self, name, group, ui):
		self.group = group
		self.name = name
		self.puzzels = []
		self.active = False
		self.done = False
		self.timer = pg.TimerObject()
		self.container = pg.FromDict(**ui)
		
	def startTimer(self,timer):
		self.timer.reset()

	def addPuzzel(self, puzzel):
		self.puzzels.append(puzzel)

	def setActive(self):
		self.active = True

	def setDone(self):
		self.done = True


class Puzzel():
	def __init__(self, name, topic=""):
		self.name = name
		self.state = 0
		self.fixed = False
		self.topics = topic
		self.container = pg.Container(self.name + "Container", **CONTAINERS["SubContainer"])
                    
	def setFixed(self):
		self.fixed = True


class Kid():
	def __init__(self, iden):
		self.id = iden
		self.group = ""

	def setGroup(self, group):
		self.group = group
		group.kidList.append(self)


class ESPModule():
	def __init__(self, name, topic, **kwargs):
		
		self.name = name
		self.topic = topic
		self.container = pg.Container(self.name + "ESPContainer", **CONTAINERS["SubContainer"])
		self.textbox = self.container.addObject(
			pg.TextBox(self.name + "ESPMqttTextBox", **TEXTBOXES["ESPMqttTextBox"]))
		self.container.title = self.name    
		i = 0
		
		for kw in kwargs:
			
			but = pg.Button(str(kw) + "ESPButton", **BUTTONS["ResetButton"])
			but.rect.x = 20
			but.rect.y = 20 + i * 55
			print("nuh uh")
			but.size = (80, 50)
			but.text = str(kw)
			but.function = kwargs[kw]
			self.container.addObject(but)
		
			i += 1

