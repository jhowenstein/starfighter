import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *



pygame.init()
game = Game(Control.Keyboard)

BLACK = (0, 0, 0)

game.BG_COLOR = BLACK

game.DISPLAYSURF = pygame.display.set_mode((game.WINDOWWIDTH, game.WINDOWHEIGHT))
game.DISPLAYSURF.fill(game.BG_COLOR)
pygame.display.set_caption('Starship PvP')

FPS = 30
fpsClock = pygame.time.Clock()

game.player1 = BasicShip(400,400)
#game.player1 = LightShip(400,400)
#game.player1 = HeavyShip(400,400)


while True:

	processInput(game)

	updateGame(game)

	pygame.display.update()
	
	fpsClock.tick(FPS)
