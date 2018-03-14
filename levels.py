import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *

def level_1(game):
	enemy_1 = BasicShip(3, 300, 32, game)
	enemy_2 = BasicShip(4, 500, 32, game)
	enemy_3 = BasicShip(5, 700, 32, game)

	game.objectList.append(enemy_1)
	game.objectList.append(enemy_2)
	game.objectList.append(enemy_3)
	
	for entity in game.objectList:
		entity.flipImage()
		
