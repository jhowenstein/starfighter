import pygame, sys, math, time
from pygame.locals import *
from enum import IntEnum
from starships import *
from weapons import *
from projectiles import *
import numpy as np

def finalScreen(game):
	if game.endCondition == -1:
		# Game Over
		game.DISPLAYSURF.fill(game.BG_COLOR)
		fontObj = pygame.font.Font('freesansbold.ttf',48)
		textSurfaceObj = fontObj.render('GAME OVER!', True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500,300)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		pygame.display.update()
		time.sleep(5)
	elif game.endCondition == 1:
		# Player 1 Wins
		game.DISPLAYSURF.fill(game.BG_COLOR)
		fontObj = pygame.font.Font('freesansbold.ttf',48)
		textSurfaceObj = fontObj.render('PLAYER 1 WINS!', True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500,300)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		pygame.display.update()
		time.sleep(5)
	elif game.endCondition == 2:
		# Player 2 Wins
		game.DISPLAYSURF.fill(game.BG_COLOR)
		fontObj = pygame.font.Font('freesansbold.ttf',48)
		textSurfaceObj = fontObj.render('PLAYER 2 WINS!', True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500,300)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		pygame.display.update()
		time.sleep(5)
	elif game.endCondition == 0:
		# Error! Unexpected Game Exit
		game.DISPLAYSURF.fill(game.BG_COLOR)
		fontObj = pygame.font.Font('freesansbold.ttf',48)
		textSurfaceObj = fontObj.render('Error. Unexpected Game Exit', True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500,300)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		pygame.display.update()
		time.sleep(5)

def splashScreen(game):
	game.DISPLAYSURF.fill(game.BG_COLOR)
	fontObj = pygame.font.Font('freesansbold.ttf',48)
	textSurfaceObj = fontObj.render('Starship PvP!', True, (255,255,255))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	pygame.display.update()
	time.sleep(5)

def playerModeSelect(game):
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)

	game.DISPLAYSURF.fill(game.BG_COLOR)
	# Select game mode font object
	fontObj = pygame.font.Font('freesansbold.ttf',36)
	textSurfaceObj = fontObj.render('Select Game Mode', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,150)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 1 Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (300, 275, 100, 50))
	# Player 1 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',28)
	textSurfaceObj = fontObj.render('1 Player', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (350,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 2 Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (600, 275, 100, 50))
	# Player 2 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',28)
	textSurfaceObj = fontObj.render('2 Player', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (650,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	# Update screen
	pygame.display.update()


def singlePlayerSetup(game):
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)

	game.DISPLAYSURF.fill(game.BG_COLOR)
	# Select game mode font object
	fontObj = pygame.font.Font('freesansbold.ttf',36)
	textSurfaceObj = fontObj.render('Single Player Options', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,150)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 1 Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (300, 275, 100, 50))
	# Player 1 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',28)
	textSurfaceObj = fontObj.render('New Game', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (350,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 2 Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (600, 275, 100, 50))
	# Player 2 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',28)
	textSurfaceObj = fontObj.render('Continue Game', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (650,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	# Update screen
	pygame.display.update()

def levelSelect(game):
	game.DISPLAYSURF.fill(game.BG_COLOR)
	# Level Select Header Object
	fontObj = pygame.font.Font('freesansbold.ttf',36)
	textSurfaceObj = fontObj.render('Select Level', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,50)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	yPositions = [100, 200, 300, 400, 500]
	nLevel = [1, 2, 3, 4, 5]

	for yPos in yPositions:
		pygame.draw.rect(game.DISPLAYSURF, BLUE, (300, yPos, 100, 50))

	for yPos in yPositions:
		pygame.draw.rect(game.DISPLAYSURF, BLUE, (600, yPos, 100, 50))

	for i in range(5):
		fontObj = pygame.font.Font('freesansbold.ttf',28)
		level_tag = 'Level ' + str(nLevel[i])
		textSurfaceObj = fontObj.render('Continue Game', True, WHITE)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (350, yPositions[i])
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	nLevel = [6, 7, 8, 9, 10]
	for i in range(5):
		fontObj = pygame.font.Font('freesansbold.ttf',28)
		level_tag = 'Level ' + str(nLevel[i])
		textSurfaceObj = fontObj.render('Continue Game', True, WHITE)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (650, yPositions[i])
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	pygame.display.update()



