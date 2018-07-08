import pygame, sys, math
from pygame.locals import *
from enum import IntEnum
from starship_game_functions import *
from starships import *
from weapons import *
from projectiles import *
from levels import *
from gameUI import *
#from survival import *


pygame.init()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 600

game = Game(WINDOWWIDTH,WINDOWHEIGHT)

BLACK = (0, 0, 0)

game.BG_COLOR = BLACK

game.DISPLAYSURF = pygame.display.set_mode((game.WINDOWWIDTH, game.WINDOWHEIGHT_WITH_SCORE))
game.DISPLAYSURF.fill(game.BG_COLOR)
pygame.display.set_caption('Starship PvP')

splashScreen(game)

numberPlayers = playerModeSelect(game)
game.setPlayers(numberPlayers)

if game.numberPlayers == 1:
	while True:
		game.spGameType = gameTypeSelect(game)
		if game.spGameType == 1:
			game.player1.ship = BasicShip(1,500,500,0,game)
			displayPlayerOneControls(game)
			playSurvival(game)
			break
		elif game.spGameType == 2:
			fontObj = pygame.font.Font('freesansbold.ttf',24)
			textSurfaceObj = fontObj.render('Sorry! Campaign Unavailable!', True, (255,255,255))
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.center = (650,350)
			game.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
			pygame.display.update()
			time.sleep(1.5)
			'''s
			lvl = levelSelect(game)
			game.setLevel(lvl)
			game.player1.ship = BasicShip(1,500,500,0,game)
			displayPlayerOneControls(game)
			playGame(game)
			break
			'''
elif game.numberPlayers == 2:
	playerOneSelectShip(game)
	if game.player1.shipType == 1:
		game.player1.ship = LightShip(1,500,500,0,game)
		game.player1.ship.setImage('ship1.png')
	elif game.player1.shipType == 2:
		game.player1.ship = BasicShip(1,500,500,0,game)
		game.player1.ship.setImage('ship2.png')
	elif game.player1.shipType == 3:
		game.player1.ship = HeavyShip(1,500,500,0,game)
		game.player1.ship.setImage('ship3.png')

	playerTwoSelectShip(game)
	if game.player2.shipType == 1:
		game.player2.ship = LightShip(2,500,100,1,game)
		game.player2.ship.setImage('ship1.png')
		game.player2.ship.flipImage()
	elif game.player2.shipType == 2:
		game.player2.ship = BasicShip(2,500,100,1,game)
		game.player2.ship.setImage('ship2.png')
		game.player2.ship.flipImage()
	elif game.player2.shipType == 3:
		game.player2.ship = HeavyShip(2,500,100,1,game)
		game.player2.ship.setImage('ship3.png')
		game.player2.ship.flipImage()
	displayPlayerOneControls(game)
	displayPlayerTwoControls(game)
	playGame(game)

finalScreen(game)

if game.spGameType == 1:
	survivalFinalScreen(game)

creditScreen(game)

pygame.quit()
sys.exit()
