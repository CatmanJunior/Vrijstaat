import pygame
from vrijstaatConst import *
window = ""
font = ""
gameLoop = False
clock = ""


ObjectList = []
ButtonList = []

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
						print(but.name)
						but.use()

	window.fill(BLACK)
	for obj in ObjectList:
		if obj.visable:
			obj.draw()

	pygame.display.update()			
	pygame.display.flip()
	clock.tick (60)
	
	return gameloop

class UIObject():
	def __init__(self, name, loc, size, color = BLACK, win = "", visable = False):
		if win == "":
			win = window
		self.window = win
		self.visable = visable
		self.name = name
		self.rect = pygame.Rect(loc[0],loc[1],size[0],size[1])
		self.color = color
		ObjectList.append(self)

	def setVisable(self, vis):
		self.visable = vis

	def draw(self):
		pass

	def highLight(self):
		pass

class Container(UIObject):
	def __init__(self, name, loc, size, color = BLACK, win = "", visable = False, showtitle = False, text = "", textcolor = BLACK):
		super().__init__(name,loc,size,color,win,visable)
		self.textColor = textcolor
		self.font = pygame.font.SysFont("arial", 14)
		self.showTitle = showtitle
		self.objectList = []
		self.text = text

	def draw(self):
		super().draw()
		if self.showTitle:
			self.window.blit(self.font.render(self.name, True, self.textColor),(self.rect.topleft[0], self.rect.topleft[1] - 50) )
		pygame.draw.rect(self.window, self.color, self.rect, 2)
		pygame.draw.rect(self.window, self.color, self.rect)

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
		def __init__(self, name, loc, size, text = "", color = BLACK, win = "", showtitle = False,  visable = False, textcolor = BLACK):
			super().__init__(name,loc,size,color,win,visable, showtitle, text)
			self.lines = []
			self.textColor = textcolor

		def addLine(self, line):
			self.lines.append(line)
			if len(self.lines) > 10:
				self.lines.pop()

		def draw(self):
			super().draw()
			self.window.blit(self.font.render(self.text, True, self.color),(self.rect.topleft[0],self.rect.topleft[1]-20))
			i = 30
			for line in self.lines:
				self.window.blit(self.font.render(line, True, BLACK),(self.rect.topleft[0], self.rect.topleft[1] + i) )
				i += 30

class Button(UIObject):
	def __init__(self, name, loc, size, color = BLACK, win = "", function = lambda : print(), text = "", visable = False, textcolor = BLACK):
		super().__init__(name,loc,size,color,win,visable)
		self.textColor = textcolor
		self.function = function
		self.text = text
		self.font = pygame.font.SysFont("arial", 18)
		ButtonList.append(self)
		

	def draw(self, font = font):
		super().draw()
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(self.font.render(self.text, True, self.textColor),(self.rect.midleft[0] + 10,self.rect.midleft[1]-20))

	def use(self):
		return self.function()

class Text(UIObject):
	def __init__(self, name, loc, text = "", color = BLACK, win = "", visable = False):
		super().__init__(name,loc,(50,50),color,win,visable)
		self.text = text
		self.font = pygame.font.SysFont("arial", 18)
		
	def draw(self):
		super().draw()
		self.window.blit(self.font.render(self.text, True, self.color),self.rect.topleft)
	
class DropDownButton(Button):
	def __init__(self, name, loc, size, color, text, win = "", visable = False, function = lambda: print(), textcolor = BLACK):
		super().__init__(name,loc,size,color,win,function,text,visable,textcolor)
		self.dropdown = []
		self.collapsed = True
	
	def addObject(self, obj):
		obj.rect.x += self.rect.x 
		obj.rect.y += self.rect.y + len(self.dropdown) * 40
		self.dropdown.append(obj)
		obj.visable = not self.collapsed
		return obj

	def removeDropDown(self, item):
		self.dropdown.remove(item)

	def draw(self, font = font):
		super().draw()
		if not self.collapsed:
			for drop in self.dropdown:
				drop.draw()
	
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
