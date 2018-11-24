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
	def __init__(self, name, group):
		self.group = group
		self.name = name
		self.puzzels = []
		self.active = False
		self.done = False

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
		self.topics = [topic]

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
	def __init__(self, name, topic, container, **kwargs):
		self.name = name
		self.topic = topic
		self.container = container
		self.textbox = self.container.addObject(pg.TextBox(
		    "Txtbox1", (290, 25), (200, 490), "TEXTBOX", visable=True, max_lines=16, border = 2, color = BLACK, bordercolor = WHITE))
		
		i = 0
		for kw in kwargs:
			self.container.addObject(pg.Button(str(kw) + "ESPButton", (20, 20 + i * 55),
			                         (80, 50), color=WHITE, text=str(kw), function=kwargs[kw]))
			i += 1

		but = self.container.addObject(pg.Button(
			"close", (self.container.rect.w-20, 0),
			(15, 15), color=RED, text="",
			function = lambda: self.container.setVisable(False), textcolor=WHITE))

