import pygame
from vrijstaatConst import *
window = ""
font = ""
gameLoop = False
clock = ""

ObjectList = []
ButtonList = []
TimerList = []



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
						print("Button Pressed: " + (but.name))
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
	def __init__(self, name, loc, size, color = BLACK, win = "", visable = False, ):
		if win == "":
			win = window
		self.window = win
		self.visable = visable
		self.name = name
		self.rect = pygame.Rect(loc[0],loc[1],size[0],size[1])
		self.color = color
		self.highLightColor = GREY
		self.highlighted = False
		self.realColor = color
		ObjectList.append(self)

	def setVisable(self, vis):
		self.visable = vis

	def draw(self):
		if self.highlighted == False:
			self.color= self.realColor

	def highLight(self):
		self.highlighted = True
		self.color = self.highLightColor

class Container(UIObject):
	def __init__(self, name, loc, size, color = BLACK, win = "", visable = False, showtitle = False, text = "", textcolor = WHITE, border = 0, bordercolor = BLACK):
		super().__init__(name,loc,size,color,win,visable)
		self.textColor = textcolor
		self.font = pygame.font.SysFont("arial", 14)
		self.showTitle = showtitle
		self.objectList = []
		self.text = text
		self.border = border
		self.borderColor = bordercolor

	def draw(self):
		if self.showTitle:
			self.window.blit(self.font.render(self.name, True, self.textColor),(self.rect.topleft[0], self.rect.topleft[1] - 20))
		pygame.draw.rect(self.window, self.color, self.rect, 0)
		if self.border != 0:
			pygame.draw.rect(self.window, self.borderColor, self.rect, self.border)
		
		super().draw()

	def addObject(self, obj):
		obj.rect.x += self.rect.x
		obj.rect.y += self.rect.y
		self.objectList.append(obj)
		obj.visable = self.visable
		return obj
		
	def setVisable(self, vis):
		self.visable = vis
		for obj in self.objectList:
			obj.setVisable(vis)

class TextBox(Container):
		def __init__(self, name, loc, size, text = "", color = BLACK, win = "", showtitle = False,  visable = False, textcolor = BLACK, max_lines = 15, border = 0, bordercolor = BLACK):
			super().__init__(name,loc,size,color = color,win = win,visable = visable, showtitle = showtitle, text = text, textcolor = textcolor, border = border, bordercolor = bordercolor)
			self.lines = []
			self.textColor = textcolor
			self.max_lines = max_lines
		def addLine(self, line):
			self.lines.append(line)
			if len(self.lines) > self.max_lines:
				self.lines.pop(0)

		def draw(self):
			super().draw()
			self.window.blit(self.font.render(self.text, True, self.color),(self.rect.topleft[0] ,self.rect.topleft[1]-20))
			i = 5
			for line in self.lines:
				self.window.blit(self.font.render(line, True, WHITE),(self.rect.topleft[0]+ 5, self.rect.topleft[1] + i))
				i += 20
				
			

class Button(UIObject):
	def __init__(self, name, loc, size, color = BLACK, win = "", function = lambda : print(), text = "", visable = False, textcolor = BLACK):
		super().__init__(name,loc,size,color,win,visable)
		self.textColor = textcolor
		self.function = function
		self.text = text
		self.font = pygame.font.SysFont("arial", 18)
		ButtonList.append(self)
		

	def draw(self, font = font):
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(self.font.render(self.text, True, self.textColor),(self.rect.midleft[0] + 10,self.rect.midleft[1]-20))
		super().draw()

	def use(self):
		return self.function()

class Text(UIObject):
	def __init__(self, name, loc, text = "", color = BLACK, win = "", visable = False):
		super().__init__(name,loc,(50,50),color,win,visable)
		self.text = text
		self.font = pygame.font.SysFont("arial", 18)
		
	def draw(self):
		self.window.blit(self.font.render(self.text, True, self.color),self.rect.topleft)
		super().draw()

class DropDownButton(Button):
	def __init__(self, name, loc, size, color, text, win = "", visable = False, function = lambda: print(), textcolor = BLACK):
		super().__init__(name,loc,size,color,win,function,text,visable,textcolor)
		self.dropdown = []
		self.collapsed = True
	
	def addObject(self, obj):
		obj.rect.x += self.rect.x 
		obj.rect.y += self.rect.y + len(self.dropdown) * 55
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
	def __init__(self, name, loc, size, color, text, win = "", visable = False, function = lambda: print(),  textcolor = BLACK):
		super().__init__(name,loc,size,color,win,function,text,visable, textcolor)
		
	def draw(self, font = font):
		super().draw()
