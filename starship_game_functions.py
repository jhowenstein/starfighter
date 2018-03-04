import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starships import *
from weapons import *
from projectiles import *



class Game(object):
	def __init__(self, controlType):
		self.objectList = []
		self.garbageList = []
		self.commandList = []

		self.WINDOWHEIGHT = 800
		self.WINDOWWIDTH = 800
		
		self.DISPLAYSURF = 0 # Display surface to be initialize prior to game loop
		
		self.BG_COLOR = (0, 0, 0) # Default = Black

		self.userControl = controlType

class Command(IntEnum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	PRIMARY = 5
	SECONDARY = 6

class Control(IntEnum):
	Keyboard = 1
	Controller = 2
	
class Ship(IntEnum):
	Basic = 1
	Light = 2
	Heavy = 3

'''	
def createShip(game, shipType, location):
	if shipType == Ship.Basic:
		game.objectList.append(BasicShip(location[0],location[1]))
	elif shipType == Ship.Light:
		game.objectList.append(LightShip(location[0],location[1]))
	elif shipType == Ship.Heavy:
		game.objectList.append(HeavyShip(location[0],location[1]))
'''


def processInput(game):
	if game.userControl == Control.Keyboard:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if event.key == K_UP:
					game.commandList.append(Command.UP)
				elif event.key == K_DOWN:
					game.commandList.append(Command.DOWN)
				elif event.key == K_LEFT:
					game.commandList.append(Command.LEFT)
				elif event.key == K_RIGHT:
					game.commandList.append(Command.RIGHT)
				elif event.key == K_SPACE:
					game.commandList.append(Command.PRIMARY)
				elif event.key == K_x:
					game.commandList.append(Command.SECONDARY)
	elif game.userControl == Control.Controller:
		print("Controller not yet supported")
		pygame.quit()
		sys.exit()


def updateGame(game):
	
	game.DISPLAYSURF.fill(game.BG_COLOR)
	
	i = 0
	while (i < len(game.objectList)):
		alive = game.objectList[i].update(game)
		if alive == False:
			game.garbageList.append(i)
		i += 1

	if len(game.garbageList) > 0:
		for entity in game.garbageList:
			game.objectList.pop(entity)

	game.commandList = []
	game.garbageList = []
