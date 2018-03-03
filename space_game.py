import pygame, sys, math
from pygame.locals import *
from enum import IntEnum


class Game(object):
	def __init__(self, controlType):
		self.objectList = []
		self.garbageList = []
		self.commandList = []

		self.WINDOWHEIGHT = 800
		self.WINDOWWIDTH = 800

		self.userControl = controlType

class Command(IntEnum):
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	PRIMARY = 5
	SECONDARY = 6

class Control(IntEnum):
	Keyboard = 1
	Controller = 2

class Ship(object):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = Weapon()
		self.weaponB = Weapon()

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

		self.commandList = []


	def move(self, direction):
		step = self.speed
		if direction == 'LEFT':
			self.shipX -= step
		elif direction == 'RIGHT':
			self.shipX += step
		elif direction == 'UP':
			self.shipY -= step
		elif direction == 'DOWN':
			self.shipY += step

	def moveLeft(self):
		step = self.speed
		lim = step - 1
		if self.shipX > lim:
			self.move('LEFT')
		else:
			self.shipX = 0

	def moveRight(self):
		WIDTH = 800
		step = self.speed
		lim = step - 1
		if self.shipX + 100 < (WIDTH - 1 - lim):
			self.move('RIGHT')
		else:
			self.shipX = WIDTH - 1

	def moveUp(self):
		step = self.speed
		lim = step - 1
		if self.shipY > lim:
			self.move('UP')
		else:
			self.shipY = 0

	def moveDown(self):
		HEIGHT = 800
		step = self.speed
		lim = step - 1
		if self.shipY < (HEIGHT - 1 - lim):
			self.move('DOWN')
		else:
			self.shipY = HEIGHT - 1

	def fireWeapon(self, weapon):
		weapon.release(self.weaponX, self.weaponY)

	def fireWeaponA(self):
		fireWeapon(weaponA)

	def fireWeaponB(self):
		fireWeapon(weaponB)

	def update(self, game):
		for com in game.commandList:
			if com = Command.UP:
				moveRight()
			elif com = Command.DOWN:
				moveDown()
			elif com = Command.LEFT:
				moveLeft()
			elif com = Command.RIGHT:
				moveRight()
			elif com = Command.PRIMARY:
				fireWeaponA()
			elif com = Command.SECONDARY:
				fireWeaponB()

		return True


class StandardShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 5
		self.armor = 5
		self.health = 100

		self.weaponA = BasicCannon()
		self.weaponB = Weapon()

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

class LightShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 7
		self.armor = 3
		self.health = 100

		self.weaponA = LightCannon()
		self.weaponB = Weapon()

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY

class HeavyShip(Ship):
	def __init__(self, initX, initY):
		self.shipImg = pygame.image.load('SpaceShipSmall.png')
		self.width = 100
		self.height = 68

		self.speed = 3
		self.armor = 7
		self.health = 100

		self.weaponA = HeavyCannon()
		self.weaponB = Weapon()

		self.weaponX = shipX + round(.5 * self.shipX)
		self.weaponY = shipY

		self.shipX = initX
		self.shipY = initY


class Weapon(object):
	def __init__(self):
		self.fireRate = 5

	def release(self, game, direction):
		pass
		#n = len(game.objectList)
		#game.objectList.append(Projectile(locX, locY, direction, n))


class BasicCannon(Weapon):
	def __init__(self):
		self.fireRate = 5

	def release(self, game, direction):
		game.objectList.append(BasicProjectile(locX, locY, direction))


class LightCannon(Weapon):
	def __init__(self):
		self.fireRate = 7

	def release(self, game, direction):
		game.objectList.append(LightProjectile(locX, locY, direction))


class HeavyCannon(Weapon):
	def __init__(self):
		self.fireRate = 3

	def release(self, game, direction):
		game.objectList.append(HeavyProjectile(locX, locY, direction))


class Projectile(Object):
	def __init__(self, locX, locY, direction):
		self.velocity = 0
		self.damage = 0
		self.direction = direction # 0 indicates upward, 1 indicates downward

		self.locX = locX
		self.locY = locY

	def update(self, game):
		if self.direction == 0:
			self.locY -= self.velocity
			if self.locY < 0:
				return False
		elif self.direction == 1:
			self.locY += self.velocity
			if self.locY >= game.WINDOWHEIGHT:
				return False

class BasicProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 5
		self.damage = 5
		self.direction = direction

		self.locX = locX
		self.locY = locY

class LightProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 7
		self.damage = 3
		self.direction = direction

		self.locX = locX
		self.locY = locY

class HeavyProjectile(Projectile):
	def __init__(self, locX, locY, direction):
		self.velocity = 3
		self.damage = 7
		self.direction = direction

		self.locX = locX
		self.locY = locY


pygame.init()

#DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#DISPLAYSURF.fill(BG_COLOR)

while True:

	processInput()

	updateGame()

	pygame.display.update()



def processInput(game):
	if game.userControl == Control.Keyboard:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if event.key == K_UP:
					game.commandList.append(Command.UP)
				elif event.key == K_DOWN:
					game.commandList.append(Command.DOWN)
				elif event.key == K_LEFT:
					game.commandList.append(Command.LEFT)
				elif event.key == K_RIGHT:
					game.commandList.append(Command.RIGHT)
				elif event.key == K_SPACE:
					game.commandList.append(Command.PRIMARY)
				elif event.key == K_x:
					game.commandList.append(Command.SECONDARY)
	elif game.userControl == Control.Controller:
		print("Controller not yet supported")
		pygame.quit()
		sys.exit()


def updateGame(game):
	i = 0
	while (i < len(game.objectList)):
		alive = objectList[i].update(game)
		if alive == False:
			game.garbageList.append(i)
		i += 1

	if len(game.garbageList) > 0:
		for entity in game.garbageList:
			game.objectList.pop(entity)

	game.commandList = []
	game.garbageList = []


	