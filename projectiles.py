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
		
		self.color = (255, 255, 255) # white default

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
				
		offset = round((self.width / 2) - .5)
		adjX = self.locX - offset
		pygame.draw.rect(DISPLAYSURF, self.color, (adjX, self.locY, self.width, self.height))
		return True
				
		

class BasicProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 5
		self.damage = 5
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 3
		self.height = 3

class LightProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 7
		self.damage = 3
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 1
		self.height = 1

class HeavyProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 3
		self.damage = 7
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 5
		self.height = 5
