import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from projectiles import *

class Weapon(object):
	def __init__(self):
		self.fireRate = 5

	def release(self, game, direction):
		pass
		#n = len(game.objectList)
		#game.objectList.append(Projectile(locX, locY, direction, n))


class BasicCannon(Weapon):
	def __init__(self):
		self.fireRate = 5

	def release(self, game, direction):
		game.objectList.append(BasicProjectile(locX, locY, direction))


class LightCannon(Weapon):
	def __init__(self):
		self.fireRate = 7

	def release(self, game, direction):
		game.objectList.append(LightProjectile(locX, locY, direction))


class HeavyCannon(Weapon):
	def __init__(self):
		self.fireRate = 3

	def release(self, game, direction):
		game.objectList.append(HeavyProjectile(locX, locY, direction))