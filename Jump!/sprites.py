# Sprite Classes for platform game
from settings import *
import pygame as pg
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
	def __init__(self,game):
		self.game = game
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((30,40))
		self.image.fill(YELLOW)

		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)

		self.pos = vec(WIDTH/2, HEIGHT / 2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		
	def update(self):
		self.acc = vec(0,PLAYER_GRAV)
		keys = pg.key.get_pressed()

		if keys[pg.K_a]:
			self.acc.x = -PLAYER_ACC
		if keys[pg.K_d]:
			self.acc.x = PLAYER_ACC

		# Applys Friction
		self.acc.x += self.vel.x * PLAYER_FRICTION

		# Equations of motion
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		# Wrap around the sides of the screen
		if self.pos.x > WIDTH:
			self.pos.x = 0

		if self.pos.x < 0:
			self.pos.x = WIDTH

		# The rectangles new position
		self.rect.midbottom = self.pos

	def jump(self):
		# If the player is on a platform then it is allowed to jump
		self.rect.x +=1
		hits = pg.sprite.spritecollide(self,self.game.platforms,False)
		if hits:
			self.vel.y = -20


class Platform(pg.sprite.Sprite):
	def __init__(self,x,y,w,h,color):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y