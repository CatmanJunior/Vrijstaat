class Group():
	def __init__(self, name):
		self.name = name
		self.phase = 0
		self.phases = []
		self.kidList = []

	def addKid(self,kid):
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
	def __init__(self,name, topic=""):
		self.name = name
		self.state = 0
		self.fixed = False
		self.topic = topic
		
	
	def setFixed(self):
		self.fixed = True

class Kid():
	def __init__(self,iden):
		self.id = iden
		self.group = ""

	def setGroup(self, group):
		self.group = group
		group.kidList.append(self)

class ESPModule():
	def __init__(self, name, topic, container):
		self.name = name
		self.topic = topic
		self.container = container
		# self.textbox = self.container.addObject(pg.TextBox("Txtbox1", (100,100),(300,300), "TEXTBOX", visable = True))




