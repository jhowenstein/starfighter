import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
#from survival import *


class Projectile(object):
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
		
		offset = round((self.width / 2))
		rendX = self.locX - offset - 1
		
		# Check for object contact
		locationVal = game.incidenceMap[self.locY, self.locX]
		if locationVal > 0:
			game.impactList.append(ImpactObject(locationVal, self.damage))
			self.color = (255, 0 , 0)
			pygame.draw.rect(game.DISPLAYSURF, self.color, (rendX - offset, self.locY - offset, self.width * 2, self.height * 2))
			return False
			
		pygame.draw.rect(game.DISPLAYSURF, self.color, (rendX, self.locY, self.width, self.height))
		return True
				
		

class BasicProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 5
		self.damage = 10
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 4
		self.height = 5

class LightProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 7
		self.damage = 5
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 2
		self.height = 3

class HeavyProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 3
		self.damage = 20
		self.direction = direction

		self.color = (255, 255, 255) # white default
		
		self.locX = locX
		self.locY = locY
		
		self.width = 6
		self.height = 7
		
class ImpactObject(object):
	def __init__(self, locID, damage):
		self.locID = locID
		self.damage = damage
