import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from weapons import *
from projectiles import *

class Command(IntEnum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	PRIMARY = 5
	SECONDARY = 6
	
class Ship(object):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = Weapon()
		self.weaponB = Weapon()

		self.shipX = initX
		self.shipY = initY
		self.direction = 0 # Upward: 0, Downward: 1
		
		self.weaponX = self.shipX + round(.5 * self.shipX)
		self.weaponY = self.shipY

		self.commandList = []


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

	def moveLeft(self):
		step = self.speed
		lim = step - 1
		if self.shipX > lim:
			self.move('LEFT')
		else:
			self.shipX = 0

	def moveRight(self):
		WIDTH = 800
		step = self.speed
		lim = step - 1
		if self.shipX + 100 < (WIDTH - 1 - lim):
			self.move('RIGHT')
		else:
			self.shipX = WIDTH - 1

	def moveUp(self):
		step = self.speed
		lim = step - 1
		if self.shipY > lim:
			self.move('UP')
		else:
			self.shipY = 0

	def moveDown(self):
		HEIGHT = 800
		step = self.speed
		lim = step - 1
		if self.shipY < (HEIGHT - 1 - lim):
			self.move('DOWN')
		else:
			self.shipY = HEIGHT - 1

	def fireWeapon(self, weapon, game):
		weapon.release(self.weaponX, self.weaponY, self.direction, game)

	def fireWeaponA(self, game):
		self.fireWeapon(self.weaponA, game)

	def fireWeaponB(self, game):
		self.fireWeapon(self.weaponB, game)
		
	def update(self, game):
		for com in game.commandList:
			if com == Command.UP:
				self.moveUp()
			elif com == Command.DOWN:
				self.moveDown()
			elif com == Command.LEFT:
				self.moveLeft()
			elif com == Command.RIGHT:
				self.moveRight()
			elif com == Command.PRIMARY:
				self.fireWeaponA(game)
			elif com == Command.SECONDARY:
				self.fireWeaponB(game)
		
		game.DISPLAYSURF.blit(self.shipImg, (self.shipX, self.shipY))
		return True

class BasicShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = BasicCannon()
		self.weaponB = Weapon()

		self.shipX = initX
		self.shipY = initY
		self.direction = 0 # Upward: 0, Downward: 1
		
		self.weaponX = self.shipX + round(.5 * self.shipX)
		self.weaponY = self.shipY


class LightShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 7
		self.armor = 3
		self.health = 100

		self.weaponA = LightCannon()
		self.weaponB = Weapon()

		self.shipX = initX
		self.shipY = initY
		self.direction = 0 # Upward: 0, Downward: 1
		
		self.weaponX = self.shipX + round(.5 * self.shipX)
		self.weaponY = self.shipY

class HeavyShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 3
		self.armor = 7
		self.health = 100

		self.weaponA = HeavyCannon()
		self.weaponB = Weapon()

		self.shipX = initX
		self.shipY = initY
		self.direction = 0 # Upward: 0, Downward: 1
		
		self.weaponX = self.shipX + round(.5 * self.shipX)
		self.weaponY = self.shipY
