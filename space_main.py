import pygame, sys, math
from pygame.locals import *
from space_game.py import *


WINDOWWIDTH = 800
WINDOWHEIGHT = 800

SHIP_WIDTH = 100
SHIP_HEIGHT = 68

shipX = 400
shipY = 400


BLACK = (0, 0, 0)

BG_COLOR = BLACK

shipImg = pygame.image.load('SpaceShipSmall.png')

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
DISPLAYSURF.fill(BG_COLOR)
pygame.display.set_caption('Space Duel')
DISPLAYSURF.blit(shipImg, (shipX, shipY))

while True:
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
	pygame.display.update()