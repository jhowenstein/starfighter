import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from projectiles import *

class Weapon(object):
	def __init__(self):
		self.cooldownTime = 10

	def release(self, locX, locY, direction, game):
		pass
		#n = len(game.objectList)
		#game.objectList.append(Projectile(locX, locY, direction, n))


class BasicCannon(Weapon):
	def __init__(self):
		self.cooldownTime = 10

	def release(self, locX, locY, direction, game):
		game.objectList.append(BasicProjectile(locX, locY, direction))


class LightCannon(Weapon):
	def __init__(self):
		self.cooldownTime = 5

	def release(self, locX, locY, direction, game):
		game.objectList.append(LightProjectile(locX, locY, direction))


class HeavyCannon(Weapon):
	def __init__(self):
		self.cooldownTime = 20

	def release(self, locX, locY, direction, game):
		game.objectList.append(HeavyProjectile(locX, locY, direction))
