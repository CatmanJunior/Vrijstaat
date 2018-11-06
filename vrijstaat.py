import pygame
import PygameUI as pg
import winsound
from vrijstaatConst import *
from vrijstaatClass import *

pg.PyInit(800,800)

playButtonList = []

def play(file):
	winsound.PlaySound(soundlist[file], winsound.SND_FILENAME|winsound.SND_ASYNC)

def playlamb(z):
	return lambda : play(z)

groupA = Group("A")
groupB = Group("B")

pTuinA = Phase("Tuin", groupA)
pTuinB = Phase("Tuin", groupB)


kid1 = Kid(1)
kid1.setGroup(groupA)

# y = 50
# z = 50
# 
# for x in soundlist:
# 	if y > 600:
# 		y = 50
# 		z += 200
# 	f = retlamb(x)
# 	playButtonList.append(pg.Button(x, (z,y),(100,50),WHITE,f, x, pg.window))
# 	y+=60

container = pg.Container((150,100),(300,300),WHITE)
container.addObject(pg.Button("bla", (60,60), (50,50), text = "haha"))
container.addObject(pg.Text("a",(10,10), "blabla"))

def game():
	pg.window.fill([0,0,0])
	for obj in pg.ObjectList:
		obj.draw()

pg.GameLoop(game)