import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *


class Projectile(Object):
	def __init__(self, locX, locY, direction):
		self.velocity = 0
		self.damage = 0
		self.direction = direction # 0 indicates upward, 1 indicates downward

		self.locX = locX
		self.locY = locY

	def update(self, game):
		if self.direction == 0:
			self.locY -= self.velocity
			if self.locY < 0:
				return False
		elif self.direction == 1:
			self.locY += self.velocity
			if self.locY >= game.WINDOWHEIGHT:
				return False

class BasicProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 5
		self.damage = 5
		self.direction = direction

		self.locX = locX
		self.locY = locY

class LightProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 7
		self.damage = 3
		self.direction = direction

		self.locX = locX
		self.locY = locY

class HeavyProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 3
		self.damage = 7
		self.direction = direction

		self.locX = locX
		self.locY = locY