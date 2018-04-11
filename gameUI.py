import pygame, sys, math, time
from pygame.locals import *
from enum import IntEnum
from starships import *
from weapons import *
from projectiles import *
from starship_game_functions import *
import numpy as np

def splashScreen(game):
	game.DISPLAYSURF.fill(game.BG_COLOR)
	fontObj = pygame.font.Font('freesansbold.ttf',48)
	textSurfaceObj = fontObj.render('StarFighter!', True, (255,255,255))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	pygame.display.update()
	time.sleep(5)

def playerModeSelect(game):
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)

	buttonWidth = 150
	buttonHeight = 50

	game.DISPLAYSURF.fill(game.BG_COLOR)
	# Select game mode font object
	fontObj = pygame.font.Font('freesansbold.ttf',36)
	textSurfaceObj = fontObj.render('Select Game Mode', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,150)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 1 Button Rectangle
	p1Button_topLeftX = 275
	p1Button_topLeftY = 275
	p1button = pygame.Rect(p1Button_topLeftX, p1Button_topLeftY, buttonWidth, buttonHeight)
	pygame.draw.rect(game.DISPLAYSURF, BLUE, p1button)
	# Player 1 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',24)
	textSurfaceObj = fontObj.render('1 Player', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (350,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Player 2 Button Rectangle
	p2Button_topLeftX = 575
	p2Button_topLeftY = 275
	p2button = pygame.Rect(p2Button_topLeftX, p2Button_topLeftY, buttonWidth, buttonHeight)
	pygame.draw.rect(game.DISPLAYSURF, BLUE, p2button)
	# Player 2 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',24)
	textSurfaceObj = fontObj.render('2 Player', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (650,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	# Update screen
	pygame.display.update()
	while True:
		eventList = pygame.event.get()
		for event in eventList:
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				mouseX, mouseY = event.pos
				if buttonSelect(p1button, mouseX, mouseY):
					return 1
				elif buttonSelect(p2button, mouseX, mouseY):
					return 2

	return 0


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
	# New Game Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (275, 275, 150, 50))
	# Player 1 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',24)
	textSurfaceObj = fontObj.render('New Game', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (350,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	# Continue Game Button Rectangle
	pygame.draw.rect(game.DISPLAYSURF, BLUE, (575, 275, 150, 50))
	# Player 2 option font object
	fontObj = pygame.font.Font('freesansbold.ttf',24)
	textSurfaceObj = fontObj.render('Continue', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (650,300)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	# Update screen
	pygame.display.update()
	time.sleep(3)

def levelSelect(game):
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)
	game.DISPLAYSURF.fill(game.BG_COLOR)
	# Level Select Header Object
	fontObj = pygame.font.Font('freesansbold.ttf',36)
	textSurfaceObj = fontObj.render('Select Level', True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (500,50)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	yPositions = [100, 200, 300, 400, 500]
	nLevel = [1, 2, 3, 4, 5]

	buttonList = []
	
	# Added button for introductory Level 0
	buttonList.append(pygame.Rect(100, 100, 100, 50))

	for yPos in yPositions:
		buttonList.append(pygame.Rect(300, yPos, 100, 50))

	for yPos in yPositions:
		buttonList.append(pygame.Rect(600, yPos, 100, 50))

	for button in buttonList:
		pygame.draw.rect(game.DISPLAYSURF, BLUE, button)

	for i in range(5):
		fontObj = pygame.font.Font('freesansbold.ttf',24)
		level_tag = 'Level ' + str(nLevel[i])
		textSurfaceObj = fontObj.render(level_tag, True, WHITE)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (350, yPositions[i]+25)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	nLevel = [6, 7, 8, 9, 10]
	for i in range(5):
		fontObj = pygame.font.Font('freesansbold.ttf',24)
		level_tag = 'Level ' + str(nLevel[i])
		textSurfaceObj = fontObj.render(level_tag, True, WHITE)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (650, yPositions[i]+25)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)

	# Code for level 0 button text
	fontObj = pygame.font.Font('freesansbold.ttf',24)
	level_tag = 'Level 0'
	textSurfaceObj = fontObj.render(level_tag, True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (150, 125)
	game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	
	pygame.display.update()

	while True:
		eventList = pygame.event.get()
		for event in eventList:
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				mouseX, mouseY = event.pos
				for i in range(len(buttonList)):
					if buttonSelect(buttonList[i], mouseX, mouseY):
						return i
	return -1

def startCountdown(game):
	stringList = ['Ready!', '3', '2', '1']

	for item in stringList:
		game.DISPLAYSURF.fill(game.BG_COLOR)
		fontObj = pygame.font.Font('freesansbold.ttf',48)
		textSurfaceObj = fontObj.render(item, True, (255,255,255))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500,300)
		game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
		pygame.display.update()
		time.sleep(1)
		

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


def buttonSelect(button, mouseX, mouseY):
	if (mouseX > button.left and mouseX < button.right and mouseY > button.top and mouseY < button.bottom):
		return True
	else:
		return False

