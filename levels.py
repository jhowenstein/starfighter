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
		ship.bottomLim = game.WINDOWHEIGHT * .5
		
	def updateAI(self):
		pass
		
class Level1(Level):
	def __init__(self, game):
		game.AI = True

		enemy_1 = BasicShip(3, 300, 32, game)
		enemy_2 = BasicShip(4, 500, 32, game)
		enemy_3 = BasicShip(5, 700, 32, game)
		
		self.setAI(enemy_1, 1)
		self.setAI(enemy_2, 1)
		self.setAI(enemy_3, 1)
		
		game.objectList.append(enemy_1)
		game.objectList.append(enemy_2)
		game.objectList.append(enemy_3)
	
		for entity in game.objectList:
			entity.direction = 1
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

# Level currently in development
class Level2(Level):
	def __init__(self, game):
		game.AI = True

		enemy_1 = BasicShip(3, 350, 182, game)
		enemy_2 = BasicShip(4, 200, 182, game)
		enemy_3 = BasicShip(5, 200, 32, game)
		enemy_4 = BasicShip(6, 350, 32, game)

		enemy_5 = BasicShip(7, 650, 182, game)
		enemy_6 = BasicShip(8, 800, 182, game)
		enemy_7 = BasicShip(9, 800, 32, game)
		enemy_8 = BasicShip(10, 650, 32, game)

		self.setAI(enemy_1, 1)
		self.setAI(enemy_2, 1)
		self.setAI(enemy_3, 1)
		self.setAI(enemy_4, 1)
		self.setAI(enemy_5, 2)
		self.setAI(enemy_6, 2)
		self.setAI(enemy_7, 2)
		self.setAI(enemy_8, 2)

		game.objectList.append(enemy_1)
		game.objectList.append(enemy_2)
		game.objectList.append(enemy_3)
		game.objectList.append(enemy_4)
		game.objectList.append(enemy_5)
		game.objectList.append(enemy_6)
		game.objectList.append(enemy_7)
		game.objectList.append(enemy_8)

		for entity in game.objectList:
			entity.direction = 1
			entity.flipImage()

	def updateAI(self, game, counter):
		for entity in game.objectList:
			if entity.AI == 1:
				entity.commandList = self.runAI_1(counter, entity.counter_offset)
			elif entity.AI == 2:
				entity.commandList = self.runAI_2(counter, entity.counter_offset)

	def runAI_1(self, counter):
		counter = counter % 120
		if counter < 30:
			command = [3]
		elif counter < 60:
			command = [1]
		elif counter < 90:
			command = [4]
		elif counter < 120
			command = [2]
		else:
			command = []

		if command == 0 or command == 10 or command == 20 or command == 30:
			command.append[5]
		return command
		
	def runAI_2(self, counter):
		counter = counter % 120
		if counter < 30:
			command = [4]
		elif counter < 60:
			command = [1]
		elif counter < 90:
			command = [3]
		elif counter < 120
			command = [2]
		else:
			command = []

		if command == 0 or command == 10 or command == 20 or command == 30:
			command.append[5]
		return command



			
		
