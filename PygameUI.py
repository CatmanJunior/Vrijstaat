import pygame
from vrijstaatConst import *
window = ""
font = ""
gameLoop = False
clock = ""


ObjectList = []


#USE THIS IF YOURE NOT INITIATING IT ANYWHERE ELSE
def PyInit(w = 500,h = 500, title = "Screen" ,FULLSCREENMODE = False):
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

def GameLoop(function, buttonList = []):
	global gameLoop
	while gameLoop:
		for event in pygame.event.get():
			if (event.type==pygame.QUIT):
				gameLoop = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos 
				for but in buttonList:
					if but.rect.collidepoint(mouse_pos):
						but.use()

		function()

		pygame.display.update()			
		pygame.display.flip()
	
		clock.tick (180)

	pygame.quit()

class Container():
	def __init__(self, loc, size, color, objectlist = [], win = ""):
		if win == "":
			win = window
		self.window = win
		
		self.rect = pygame.Rect(loc[0],loc[1],size[0],size[1])
		self.color = color
		self.objectList = objectlist
		ObjectList.append(self)

	def draw(self):
		pygame.draw.rect(self.window, self.color, self.rect, 2)

	def addObject(self, obj):
		obj.rect.x += self.rect.x
		obj.rect.y += self.rect.y
		self.objectList.append(obj)

class Button():
	def __init__(self, name, loc, size, color = WHITE, function = print(), text = "", win = ""):
		if win == "":
			win = window
		self.window = win
		self.name = name
		self.rect = pygame.Rect(loc[0],loc[1],size[0],size[1])
		self.color = color
		self.function = function
		self.text = text
		ObjectList.append(self)

	def draw(self, font = font):
		font = pygame.font.SysFont("arial", 18)
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(font.render(self.text, True, (0, 0, 0)),(self.rect.midleft[0] + 5,self.rect.midleft[1]-25))
	

	def use(self):

		return self.function()

class Text():
	def __init__(self, name, loc, text, color = WHITE, win = ""):
		if win == "":
			win = window
		self.window = win
		self.rect = pygame.Rect(loc[0],loc[1],50,50)
		self.text = text
		self.font = pygame.font.SysFont("arial", 18)
		self.color = color
		ObjectList.append(self)
	
	def draw(self):
		
		self.window.blit(self.font.render(self.text, True, self.color),self.rect.topleft)
	
class DropDownButton():
	def __init__(self, name, loc, size, color, function, text, win = "", dropdowns = []):
		if win == "":
			win = window
		self.window = win
		self.name = name
		self.rect = pygame.Rect(loc[0],loc[1],size[0],size[1])
		self.color = color
		self.text = text
		self.dropdown = dropdowns
		self.collapsed = True
	def addDropDown(self, item):
		self.dropdown.append(item)

	def removeDropDown(self, item):
		self.dropdown.remove(item)

	def draw(self, font = font):
		font = pygame.font.SysFont("arial", 18)
		pygame.draw.rect(self.window, self.color, self.rect)
		self.window.blit(font.render(self.text, True, (0, 0, 0)),(self.rect.midleft[0] + 5,self.rect.midleft[1]-25))
		if not self.collapsed:
			for drop in self.dropdown:
				drop.draw()
	
	def use(self):
		self.collapsed = not self.collapsed