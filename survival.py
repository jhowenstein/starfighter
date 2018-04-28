import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *
from levels import *
from gameUI import *

class Survivor(object):
	def __init__(self):
		self.status = True
		self.roundCount = 0
		self.numEnemies = 1
		self.enemySpeed = 5
		self.enemyProjSpeed = 5
		self.enemyDamage = 10
		self.enemyRefresh = 10
		self.enemyHealth = 50
		self.enemyCurrDirection = []


def playSurvival(game):

	startCountdown(game)

	while game.survivor.status == True:
		createRound(game)

		roundEntry(game)

		gameLoop(game)

		updateSurvivor(game)


def gameLoop(game):

	FPS = 30
	fpsClock = pygame.time.Clock()

	while game.status == True:

		processInput(game)

		survivalAI(game)

		updateGame(game)

		pygame.display.update()
		
		fpsClock.tick(FPS)

	return game.endCondition


def updateSurvivor(game):
	endCondition = game.endCondition
	if endCondition == -1:
		game.survivor = False
	elif endCondition == 1:
		updateEnemyStats(game)

	# Probably want something to update to the game totals here


def createRound(game):
	game.objectList = []

	xLoc = [500, 350, 650]
	yLoc = 0
	for i in range(game.survivor.numEnemies):
		shipID = i + 3
		game.objectList.append(BasicShip(shipID, xLoc[i], yLoc, 1, game))

	for entity in objectList:
		entity.speed = game.survivor.enemySpeed
		entity.weaponA = CustomCannon()
		entity.weaponA.projectileSpeed = game.survivor.enemyProjSpeed
		entity.weaponA.projectileDamage = game.survivor.enemyDamage
		entity.weaponA.cooldownTime = game.enemyRefresh
		entity.health = 50
		entity.bottomLim = game.WINDOWHEIGHT * .5
		entity.setImage('ship3.png')
		entity.flipImage()


def roundEntry(game):
	yTarget = 100

	FPS = 30
	fpsClock = pygame.time.Clock()

	while game.objectList[0].shipY < 100:

		for entity in game.objectList:
			entity.commandList = [2]

		updateGame(game)

		pygame.display.update()

		fpsClock.tick(FPS)

def survivalAI(game):
	counter = game.counter
	mainLocY = game.objectList[0].shipY
	directionBias = 0
	leftQuarter = game.WINDOWWIDTH * .25
	rightQuarter = game.WINDOWWIDTH * .75
	if mainLocY < leftQuarter:
		directionBias = -1
	elif mainLocY > rightQuarter:
		leftBias = 1

	if (counter % 10) == 0:
		rNum = randint(0,9)
		if rNum < 2:
			direction = []
		elif rNum < 4:
			direction = [1]
		elif rNum < 6:
			direction = [2]
		elif rNum < (8 + directionBias):
			direction = [3]
		elif rNum < 10:
			direction = [4]

		game.survivor.enemyCurrDirection = direction

	for entity in game.objectList:
		entity.commandList = game.survivor.enemyCurrDirection
		fireRandInt = randint(0,99)
		if fireRandInt < 20:
			entity.commandList.append(5)


#### NEED TO SIMPLIFY TO TEST FIRST
def updateEnemyStats(game):
	roundCount = game.survivor.roundCount

	enemy.survivor.enemySpeed += 1
	'''
	RC = roundCount % 5

	if RC == 0:
		game.survivor.enemySpeed += 2
	elif RC == 1:
		game.survivor.enemyProjSpeed += 1
	elif RC == 2:
		game.survivor.enemyDamage += 3
	elif RC == 3:
		game.survivor.enemyHealth += 10
	elif RC = 4:
		if game.survivor.numEnemies < 3:
			game.survivor.numEnemies += 1
		elif game.survivor.enemyRefresh > 0:
			game.survivor.enemyRefresh -= 1
	'''

