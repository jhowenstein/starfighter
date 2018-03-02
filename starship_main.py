import pygame, sys, math
from pygame.locals import *
from enum import IntEnum



pygame.init()
game = Game()

BLACK = (0, 0, 0)

BG_COLOR = BLACK

DISPLAYSURF = pygame.display.set_mode((game.WINDOWWIDTH, game.WINDOWHEIGHT))
DISPLAYSURF.fill(BG_COLOR)
pygame.display.set_caption('Starship PvP')

while True:

	processInput()

	updateGame()

	pygame.display.update()