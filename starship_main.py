import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *
from levels import *
from gameUI import *


pygame.init()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600

game = Game(WINDOWWIDTH,WINDOWHEIGHT)

BLACK = (0, 0, 0)

game.BG_COLOR = BLACK

game.DISPLAYSURF = pygame.display.set_mode((game.WINDOWWIDTH, game.WINDOWHEIGHT))
game.DISPLAYSURF.fill(game.BG_COLOR)
pygame.display.set_caption('Starship PvP')

#numberPlayers = 1

splashScreen(game)
numberPlayers = playerModeSelect(game)
game.setPlayers(numberPlayers)
#singlePlayerSetup(game)
lvl = levelSelect(game)
game.setLevel(lvl)

game.player1.ship = BasicShip(1,500,500,0,game)
#game.player1.ship = LightShip(1,500,500,0,game)
#game.player1.ship = HeavyShip(1,500,500,0,game)

FPS = 30
fpsClock = pygame.time.Clock()

startCountdown()

while game.status == True:

	processInput(game)

	updateGame(game)

	pygame.display.update()
	
	fpsClock.tick(FPS)

finalScreen(game)

pygame.quit()
sys.exit()
