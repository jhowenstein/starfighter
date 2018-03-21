import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *

class Level(object):
	def __init__(self, game):
		# define enemies
		# configure enemies
			# Set enemy properties
			# set enemy AI commands
		# Add enemies to game objectList
		# flip image
		pass
		
	def setAI(self, ship, N):
		ship.AI = N
		
	def updateAI(self):
		pass
		
class Level1(Level):
	def __init__(self, game):
		game.AI = True

		enemy_1 = BasicShip(3, 300, 32, game)
		enemy_2 = BasicShip(4, 500, 32, game)
		enemy_3 = BasicShip(5, 700, 32, game)

		enemy_1.direction = 1
		enemy_2.direction = 1
		enemy_3.direction = 1
		
		self.setAI(enemy_1, 1)
		self.setAI(enemy_2, 1)
		self.setAI(enemy_3, 1)
		
		game.objectList.append(enemy_1)
		game.objectList.append(enemy_2)
		game.objectList.append(enemy_3)
	
		for entity in game.objectList:
			entity.flipImage()
			
	def updateAI(self, game, counter):
		for entity in game.objectList:
			if entity.AI == 1:
				entity.commandList = self.runAI_1(counter)
				
	def runAI_1(self, counter):
		counter = counter % 150
		if counter < 30:
			command = [3]
		elif counter < 90:
			command = [4]
		elif counter < 120:
			command = [3]
		elif counter == 120 or counter == 130 or counter == 140:
			command = [5]
		else:
			command = []
		return command

			
		
