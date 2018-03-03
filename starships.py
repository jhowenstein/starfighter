import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from weapons import *
from projectiles import *


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

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

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

	def fireWeapon(self, weapon):
		weapon.release(self.weaponX, self.weaponY)

	def fireWeaponA(self):
		fireWeapon(weaponA)

	def fireWeaponB(self):
		fireWeapon(weaponB)

	def update(self, game):
		for com in game.commandList:
			if com = Command.UP:
				moveRight()
			elif com = Command.DOWN:
				moveDown()
			elif com = Command.LEFT:
				moveLeft()
			elif com = Command.RIGHT:
				moveRight()
			elif com = Command.PRIMARY:
				fireWeaponA()
			elif com = Command.SECONDARY:
				fireWeaponB()

		return True


class StandardShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = BasicCannon()
		self.weaponB = Weapon()

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

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

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

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

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY