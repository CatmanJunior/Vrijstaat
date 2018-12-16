import pygame
from gtts import gTTS
from MqttClass import SendMqtt
import copy
import collections

window = ""
font = ""
gameLoop = False
clock = ""

ObjectList = []
ButtonList = []
TimerList = []
ObjectDict = collections.OrderedDict()

GREY = [200,200,200]
WHITE = [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]
GREEN = [0,255,0]

def addDict(base, adder):
	adder = copy.deepcopy(adder)
	adder.update(base)
	return adder




#Creates a ui from a dictionary
#Needs a maincontainer, or in the dictionary (key = "MainContainer"),
#or as an arg (type = container)
def FromDict(ui, main = None):
	if "MainContainer" not in ui and main == None:
		print (str(ui) + "Has no main container: Can't create")
		return None
	elif "MainContainer" in ui:
		mc = ui["MainContainer"]
		if "fromobject" in mc:
			cont = mc["fromobject"]["type"](mc["contname"], **mc)
		else:
			cont = mc["type"](mc["contname"], **mc)
	elif isinstance(main, Container):
		cont = main
	elif main != None:
		cont = main["type"](main["contname"], **main)
	for obj in ui:
		if obj is not "MainContainer":
			if "fromobject" in ui[obj]:
				temp_object = ui[obj]["fromobject"]["type"](obj, **ui[obj])
			else:
				temp_object = ui[obj]["type"](obj, **ui[obj])
			cont.addObject(temp_object)
	for obj in ui:
		if "objects" in ui[obj]:
				for element in ui[obj]["objects"]:
					ObjectDict[obj].addObject(ObjectDict[element])
	return cont

#Turn this into sound from pygame
def playTTS(txt):
	tts = gTTS(text=txt, lang='en')
	tts.save("text1" + ".mp3")
	pygame.mixer.music.load('text1.mp3')
	pygame.mixer.music.play()

def PlaySound(file):
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()

#USE THIS IF YOURE NOT INITIATING IT ANYWHERE ELSE
def PyInit(w = 800,h = 800, title = "Screen" ,FULLSCREENMODE = False):
	global font, window, gameLoop, clock
	pygame.init()
	window = pygame.display.set_mode((w,h),(pygame.FULLSCREEN if FULLSCREENMODE else 0))
	pygame.display.set_caption(title)
	clock = pygame.time.Clock()
	gameLoop = True
	font = pygame.font.SysFont("arial", 18)

#THIS ONE IF YOU JUST WANT TO USE THE UI ELEMENTS
def UIinit(win, fon):
	global window, font
	window = win
	font = fon

def GameLoop():
	gameloop = True
	for event in pygame.event.get():
		# if event.type==SONG_END:
		# 	pass
		if (event.type==pygame.QUIT):
			gameloop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameloop = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos
			for but in ButtonList:
				if but.rect.collidepoint(mouse_pos):
					if but.visable:
						print("Button Pressed: " + (but.name) + " : " +  str(but.function))
						but.use()
						break
			else:
				for but in ButtonList:
					if isinstance(but, DropDownButton):
						but.collapse()
		if event.type == pygame.MOUSEMOTION:
			for obj in ButtonList:
					if obj.visable and obj.rect.collidepoint(event.pos):
						obj.highLight()
					elif obj.highlighted:
						obj.highlighted = False

	window.fill(BLACK)
	for obj in ObjectDict:
		if ObjectDict[obj].visable:
			ObjectDict[obj].draw()

	for t in TimerList:
		t.currentTime = pygame.time.get_ticks() - t.startTime

	pygame.display.update()			
	pygame.display.flip()
	clock.tick (60)
	
	return gameloop

class TimerObject():
	def __init__(self):
		self.startTime = pygame.time.get_ticks()
		self.currentTime = 0
		TimerList.append(self)
	def reset(self):
		self.startTime = pygame.time.get_ticks()

BASE = {
	"name"			:	"",
	"location"		:	(0,0),
	"size"			:	(0,0),
	"color"			:	BLACK,
	"highlightcolor":	GREY,
	"bordercolor"	:	WHITE,
	"textcolor"		:	WHITE,
	"togglecolor"	:	GREEN,
	"visable"		:	False,
	"title"			:	"",
	"showtitle"		:	False,
	"border"		:	0,
	"autofit"		:	False,
	"maxlines"		:	10,
	"function"		:	"pass",
	"offfunction"	:	"pass",
	"text"			:	"",
	"fontsize"		:	12,
	"fullwidth"		:	False,
}

class UIObject():
	def __init__(self, name, **kwargs):
		
		if "fromobject" in kwargs:
			temp = addDict(kwargs["fromobject"], BASE)
			kwargs = addDict(kwargs,temp)
		else:
			kwargs = addDict(kwargs,BASE)
		
		self.window = window
		self.name = name
		self.rect = pygame.Rect(kwargs["location"][0],kwargs["location"][1],kwargs["size"][0],kwargs["size"][1])
		self.visable = kwargs["visable"]
		self.color = kwargs["color"]
		self.realColor = self.color
		self.highLightColor = kwargs["highlightcolor"]
		self.highlighted = False
		self.textColor = kwargs["textcolor"]
		self.showTitle = kwargs["showtitle"]
		self.objectList = []
		self.title = kwargs["title"]
		self.borderColor = kwargs["bordercolor"]
		self.border = kwargs["border"]
		self.textColor = kwargs["textcolor"]
		self.autofit = kwargs["autofit"]
		self.lastobject = (5,5)
		self.lines = []
		self.max_lines = kwargs["maxlines"]
		self.function = lambda : exec(kwargs["function"])
		self.offfunction = lambda : exec(kwargs["offfunction"])
		self.text = kwargs["text"]
		self.font = pygame.font.SysFont("arial", kwargs["fontsize"])
		self.toggled = False
		self.togglecolor = kwargs["togglecolor"]
		self.fullwidth = kwargs["fullwidth"]

		ObjectList.append(self)
		ObjectDict[self.name] = self
		return self

	def setVisable(self, vis):
		self.visable = vis

	def draw(self):
		if self.highlighted == False:
			self.color= self.realColor
		else:
			#Change this later cause this is gona slow it down
			self.color = self.highLightColor

	def highLight(self):
		self.highlighted = True
		self.color = self.highLightColor

class Container(UIObject):
	def __init__(self, name, **kw):
		super().__init__(name, **kw)
		
	def draw(self):
		if self.showTitle:
			self.window.blit(self.font.render(self.title, True, self.textColor),(self.rect.topleft[0], self.rect.topleft[1] - 20))
		pygame.draw.rect(self.window, self.color, self.rect, 0)
		if self.border != 0:
			pygame.draw.rect(self.window, self.borderColor, self.rect, self.border)
		
		super().draw()

	def addObject(self, obj):
		
		if self.autofit:
			if self.lastobject[0] + obj.rect.width > self.rect.width:
				self.lastobject = (5, self.lastobject[1] + obj.rect.height + 5)
			obj.rect.x = self.lastobject[0] + self.rect.x
			obj.rect.y = self.lastobject[1]	+ self.rect.y
			self.lastobject = (self.lastobject[0] + 5 +obj.rect.width,self.lastobject[1])
		else:
			obj.rect.x += self.rect.x
			obj.rect.y += self.rect.y

		self.objectList.append(obj)
		
		obj.visable = self.visable
		return obj
		
	def moveObjects(self,oldlocation):
		for obj in self.objectList:
			if self.autofit:
				self.lastobject= (0,0)
				if self.lastobject[0] + obj.rect.width > self.rect.width:
					self.lastobject = (5, self.lastobject[1] + obj.rect.height + 5)
				obj.rect.x = self.lastobject[0] + self.rect.x
				obj.rect.y = self.lastobject[1]	+ self.rect.y
				self.lastobject = (self.lastobject[0] + 5 +obj.rect.width,self.lastobject[1])
			else:
				obj.rect.x = self.rect.x - oldlocation[0] + obj.rect.x 
				obj.rect.y = self.rect.y - oldlocation[1] + obj.rect.y


	def setVisable(self, vis):
		self.visable = vis
		for obj in self.objectList:
			obj.setVisable(vis)

class HeaderContainer(Container):
	def addObject(self, obj):
		if len(self.objectList) != 0:
			x = self.objectList[-1].rect.topright[0] + 5
		else:
			x = self.rect.x + 5
		if obj.rect.height > self.rect.height:
			self.rect.height = obj.rect.height + 10
		obj.rect.x = x
		obj.rect.y = self.rect.y + 5
		self.objectList.append(obj)
		obj.visable = self.visable
		i = 0
		if self.fullwidth:
			for o in self.objectList:
				o.rect.width = self.rect.width/len(self.objectList)
				o.rect.x = self.rect.width/len(self.objectList)*i+self.rect.x+5
				i+=1
		return obj
		
class TextBox(Container):
	def __init__(self, name, **kw):
		super().__init__(name, **kw)
		
	def addLine(self, line):
		self.lines.append(line)
		if len(self.lines) > self.max_lines:
			self.lines.pop(0)

	def draw(self):
		super().draw()
		i = 5
		for line in self.lines:
			self.window.blit(self.font.render(line, True, WHITE),(self.rect.topleft[0]+ 5, self.rect.topleft[1] + i))
			i += 20
	
	def clear(self):
		self.lines[:] = []
		
class Button(UIObject):
	def __init__(self, name, **kw):
		super().__init__(name,**kw)
		ButtonList.append(self)
		
	def draw(self, font = font):
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(self.font.render(self.text, True, self.textColor),(self.rect.midleft[0]+5,self.rect.midleft[1]))
		super().draw()

	def use(self):
		return self.function()

class ButtonArray(Container):
	def __init__(self, name,**template):
		super().__init__(name,**template)
		print(self.rect)
		self.autofit = True
		for var in template["varlist"]:
			temp_func = {
				"function" : template["functionlist"][0] + str(var) + template["functionlist"][1],
				"text"	: str(var),}
			temp = addDict(temp_func, template["buttontemplate"])
			but = Button(self.name + str(var) + "Button", **temp)
			self.addObject(but)
		
	def addObject(self,obj):
		super().addObject(obj)		
		
		
	def draw(self, font = font):
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(self.font.render(self.text, True, self.textColor),(self.rect.midleft[0]+5,self.rect.midleft[1]))
		super().draw()

	def use(self):
		return self.function()

class ToggleButton(Button):
	def __init__(self, name, **kw):
		super().__init__(name,**kw)

	def draw(self, font = font):
		if self.toggled:
			self.color = self.togglecolor
		super().draw()

	def use(self):
		self.toggled = not self.toggled
		if self.toggled == True:
			return self.function()
		else:
			return self.offfunction()
	
class Text(UIObject):
	def __init__(self, name, **kw):
		super().__init__(name,**kw)
		
	def draw(self):
		self.window.blit(self.font.render(self.text, True, self.color),self.rect.topleft)
		super().draw()

class DropDownButton(Button):
	def __init__(self, name, **kw):
		super().__init__(name,**kw)
		self.dropdown = []
		self.collapsed = True
	
	def addObject(self, obj):
		obj.rect.x += self.rect.x 
		obj.rect.y += self.rect.y + len(self.dropdown) * (obj.rect.height + 1) + 1
		self.dropdown.append(obj)
		obj.visable = not self.collapsed
		return obj

	def removeDropDown(self, item):
		self.dropdown.remove(item)

	def draw(self, font = font):
		if not self.collapsed:
			for drop in self.dropdown:
				drop.draw()
		super().draw()

	def collapse(self):
		self.collapsed = True
		for drop in self.dropdown:
			drop.visable = False

	def use(self):
		self.collapsed = not self.collapsed
		for drop in self.dropdown:
			ObjectDict.move_to_end(drop.name)
			drop.visable = not drop.visable

class DropDown(Button):
	def __init__(self, name, text, **kw):
		kw["text"] = text
		super().__init__(name,**kw)
		
	def draw(self, font = font):
		super().draw()
