import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from weapons import *
from projectiles import *
import numpy as np

class Command(IntEnum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	PRIMARY = 5
	SECONDARY = 6
	
class Ship(object):
	def __init__(self, shipID, initX, initY, direction, game):
		self.ID = shipID
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = self.shipImg.get_width()
		self.height = self.shipImg.get_height()
		
		self.halfWidth = round(self.width / 2)

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = Weapon()
		self.weaponB = Weapon()
		self.cooldownA = 100
		self.cooldownB = 100

		self.direction = direction # Upward: 0, Downward: 1

		self.shipX = initX
		if self.direction == 0:
			self.shipY = initY
		elif self.direction == 1:
			self.shipY = initY - self.shipImg.get_height()
		
		
		if self.ID == 1:
			self.topLim = game.WINDOWHEIGHT * .75
			self.bottomLim = game.WINDOWHEIGHT
		elif self.ID > 1:
			self.topLim = 0
			self.bottomLim = game.WINDOWHEIGHT * .25
			
		self.AI = 0
		self.offsetAI = 0 # Time offset of the AI procedure for individual ship

		self.commandList = []
		self.damageList = []


	def move(self, direction):
		step = self.speed
		if direction == 'LEFT':
			self.shipX -= step
		elif direction == 'RIGHT':
			self.shipX += step
		elif direction == 'UP':
			self.shipY -= step
		elif direction == 'DOWN':
			self.shipY += step

	def moveLeft(self, game):
		step = self.speed
		lim = step - 1
		if (self.shipX - self.halfWidth)  > lim:
			self.move('LEFT')
		else:
			self.shipX = self.halfWidth

	def moveRight(self, game):
		WIDTH = game.WINDOWWIDTH
		step = self.speed
		lim = step - 1
		if (self.shipX + self.halfWidth) < (WIDTH - 1 - lim):
			self.move('RIGHT')
		else:
			self.shipX = (WIDTH - 1) - self.halfWidth

	def moveUp(self, game):
		step = self.speed
		lim = step - 1
		if self.shipY > (self.topLim + lim):
			self.move('UP')
		else:
			self.shipY = self.topLim

	def moveDown(self, game):
		#HEIGHT = game.WINDOWHEIGHT
		HEIGHT = self.bottomLim
		step = self.speed
		lim = step - 1
		if self.shipY < (HEIGHT - 1 - lim - self.height):
			self.move('DOWN')
		else:
			self.shipY = HEIGHT - 1 - self.height

	def flipImage(self):
		self.shipImg = pygame.transform.flip(self.shipImg, False, True)
		
	def fireWeapon(self, weapon, game):
		if self.direction == 0:
			weapon.release(self.shipX, self.shipY, self.direction, game)
		elif self.direction == 1:
			weapon.release(self.shipX, self.shipY + self.height + 1, self.direction, game)

	def fireWeaponA(self, game):
		self.fireWeapon(self.weaponA, game)

	def fireWeaponB(self, game):
		self.fireWeapon(self.weaponB, game)
		
	def handleDamage(self):
		for damage in self.damageList:
			self.health -= damage
			
		self.damageList = []
		
		if self.health <= 0:
			return False
		else:
			return True
			
		
	def update(self, game):
		# Handle damage from any projectile impacts
		if len(self.damageList) > 0:
			shipStatus = self.handleDamage()
			if shipStatus == False:
				return False
			
		# Tracks cooldown of each weapon. Will likely move this into weapon object
		if self.cooldownA < 100:
			self.cooldownA += 1
		if self.cooldownB < 100:
			self.cooldownB += 1
			
			
		for com in self.commandList:
			if com == Command.UP:
				self.moveUp(game)
			elif com == Command.DOWN:
				self.moveDown(game)
			elif com == Command.LEFT:
				self.moveLeft(game)
			elif com == Command.RIGHT:
				self.moveRight(game)
			elif com == Command.PRIMARY:
				if self.cooldownA >= self.weaponA.cooldownTime:
					self.fireWeaponA(game)
					self.cooldownA = 0
			elif com == Command.SECONDARY:
				if self.cooldownB >= self.weaponB.cooldownTime:
					self.fireWeaponB(game)
					self.cooldownB = 0
		
		adjX = self.shipX - self.halfWidth  # Adjustment to center the ship image for rendering
		game.DISPLAYSURF.blit(self.shipImg, (adjX, self.shipY))
		
		game.incidenceMap[self.shipY:(self.shipY + self.height),adjX:(adjX + self.width)] = self.ID
		
		self.commandList = []
		return True

class BasicShip(Ship):
	def __init__(self, shipID, initX, initY, direction, game):
		self.ID = shipID
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = self.shipImg.get_width()
		self.height = self.shipImg.get_height()
		
		self.halfWidth = round(self.width / 2)

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = BasicCannon()
		self.weaponB = Weapon()
		self.cooldownA = 100
		self.cooldownB = 100

		self.direction = direction # Upward: 0, Downward: 1

		self.shipX = initX
		if self.direction == 0:
			self.shipY = initY
		elif self.direction == 1:
			self.shipY = initY - self.shipImg.get_height()
		
		if self.ID == 1:
			self.topLim = game.WINDOWHEIGHT * .75
			self.bottomLim = game.WINDOWHEIGHT
		elif self.ID > 1:
			self.topLim = 0
			self.bottomLim = game.WINDOWHEIGHT * .25

		self.AI = 0
		self.offsetAI = 0 # Time offset of the AI procedure for individual ship
						
		self.commandList = []
		self.damageList = []
		

class LightShip(Ship):
	def __init__(self, shipID, initX, initY, direction, game):
		self.ID = shipID
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = self.shipImg.get_width()
		self.height = self.shipImg.get_height()
		
		self.halfWidth = round(self.width / 2)

		self.speed = 7
		self.armor = 3
		self.health = 100

		self.weaponA = LightCannon()
		self.weaponB = Weapon()
		self.cooldownA = 100
		self.cooldownB = 100
		
		self.direction = direction # Upward: 0, Downward: 1

		self.shipX = initX
		if self.direction == 0:
			self.shipY = initY
		elif self.direction == 1:
			self.shipY = initY - self.shipImg.get_height()

		if self.ID == 1:
			self.topLim = game.WINDOWHEIGHT * .75
			self.bottomLim = game.WINDOWHEIGHT
		elif self.ID > 1:
			self.topLim = 0
			self.bottomLim = game.WINDOWHEIGHT * .25

		self.AI = 0
		
		self.commandList = []
		self.damageList = []
		

class HeavyShip(Ship):
	def __init__(self, shipID, initX, initY, direction, game):
		self.ID = shipID
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = self.shipImg.get_width()
		self.height = self.shipImg.get_height()
		
		self.halfWidth = round(self.width / 2)

		self.speed = 3
		self.armor = 7
		self.health = 100

		self.weaponA = HeavyCannon()
		self.weaponB = Weapon()
		self.cooldownA = 100
		self.cooldownB = 100
		
		self.direction = direction # Upward: 0, Downward: 1

		self.shipX = initX
		if self.direction == 0:
			self.shipY = initY
		elif self.direction == 1:
			self.shipY = initY - self.shipImg.get_height()

		if self.ID == 1:
			self.topLim = game.WINDOWHEIGHT * .75
			self.bottomLim = game.WINDOWHEIGHT
		elif self.ID > 1:
			self.topLim = 0
			self.bottomLim = game.WINDOWHEIGHT * .25

		self.AI = 0
		self.offsetAI = 0 # Time offset of the AI procedure for individual ship
							
		self.commandList = []
		self.damageList = []
		
