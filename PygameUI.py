import pygame
from gtts import gTTS
from MqttClass import SendMqtt

window = ""
font = ""
gameLoop = False
clock = ""

ObjectList = []
ButtonList = []
TimerList = []
ObjectDict = {}

GREY = [200,200,200]
WHITE = [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]
GREEN = [0,255,0]

def FromDict(ui, main = None):

	if "MainContainer" not in ui and main == None:
		print (str(ui) + "Has no main container: Can't create")
		return None
	elif "MainContainer" in ui:
		if "fromobject" in ui["MainContainer"]:
				ui["MainContainer"]["fromobject"].update(ui["MainContainer"])
				ui["MainContainer"] = ui["MainContainer"]["fromobject"]
		cont = ui["MainContainer"]["type"](ui["MainContainer"]["contname"], **ui["MainContainer"])
	elif isinstance(main, Container):
		cont = main

	elif main != None:
		cont = main["type"](main["contname"], **main)
	
	for obj in ui:

		if obj is not "MainContainer":
			if "fromobject" in ui[obj]:

				ui[obj]["fromobject"].update(ui[obj])
				ui[obj] = ui[obj]["fromobject"]
			
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
		if event.type == pygame.MOUSEMOTION:
			for obj in ButtonList:
					if obj.visable and obj.rect.collidepoint(event.pos):
						obj.highLight()

					elif obj.highlighted:
						obj.highlighted = False

	window.fill(BLACK)
	for obj in ObjectList:
		if obj.visable:
			obj.draw()

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

class UIObject():
	def __init__(self, name, **kwargs):
		self.window = window
		self.name = name
		self.rect = pygame.Rect(kwargs["location"][0],kwargs["location"][1],kwargs["size"][0],kwargs["size"][1])
		
		if "visable" in kwargs:
			self.visable = kwargs["visable"]
		else:
			self.visable = False
		
		if "color" in kwargs:
			self.color = kwargs["color"]
		else:
			self.color = BLACK

		self.highLightColor = GREY
		self.highlighted = False
		self.realColor = self.color
		ObjectList.append(self)
		ObjectDict[self.name] = self
		return self

	def setVisable(self, vis):
		self.visable = vis

	def draw(self):
		if self.highlighted == False:
			self.color= self.realColor

	def highLight(self):
		self.highlighted = True
		self.color = self.highLightColor

class Container(UIObject):
	def __init__(self, name, **kw):
		super().__init__(name, **kw)
		self.font = pygame.font.SysFont("arial", 14)
		if "showtitle" in kw:
			self.showTitle = kw["showtitle"]
		else:
			self.showtitle = False
		self.objectList = []
		self.title = kw["title"]
		self.border = kw["border"]
		if "bordercolor" in kw:
			self.borderColor = kw["bordercolor"]
		else:
			self.bordercolor = WHITE
		self.textColor = WHITE
		if "autofit" in kw:
			self.autofit = kw["autofit"]
			self.lastobject = (5,5)
		else:
			self.autofit = False


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
		return obj

		
class TextBox(Container):
	def __init__(self, name, **kw):
		super().__init__(name, **kw)
		self.lines = []
		self.textColor = kw["textcolor"]
		self.max_lines = kw["maxlines"]

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
		self.textColor = kw["textcolor"]
		if "function" in kw:
			self.function = lambda : exec(kw["function"])
		else:
			self.function = lambda : print()
		if "text" in kw:	
			self.text = kw["text"]
		else:
			self.text= "Button"
		self.font = pygame.font.SysFont("arial", kw["fontsize"])
		ButtonList.append(self)
		
	def draw(self, font = font):
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(self.font.render(self.text, True, self.textColor),(self.rect.midleft[0]+5,self.rect.midleft[1]))
		super().draw()

	def use(self):

		return self.function()

class Text(UIObject):
	def __init__(self, name, **kw):
		super().__init__(name,**kw)
		self.text = kw["text"]
		self.font = pygame.font.SysFont("arial", kw["fontsize"])
		
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

	def use(self):
		self.collapsed = not self.collapsed
		for drop in self.dropdown:
			drop.draw()
			drop.visable = not drop.visable

class DropDown(Button):
	def __init__(self, name, text, **kw):
		kw["text"] = text
		super().__init__(name,**kw)
		
	def draw(self, font = font):
		super().draw()

