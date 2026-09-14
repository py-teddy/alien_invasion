import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	""" Overall class to manage game assests and behavior."""

	def __init__(self):
		"""Define game attributes, create game resources."""
		pygame.init()
		self.settings = Settings()


		# Creating screen surface
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# creating elements
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group() # Group to store bullet sprites

	def run_game(self):
		"""Start main loop for game."""
		while True:
			self._check_events()
			self.ship.update_ship()
			self.bullets.update()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypress and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check list of recent events for a keypress action
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			# Check list of recent events for key release action
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.ship.ship_moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.ship_moving_left = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q: # if pressed q key
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.ship_moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.ship_moving_left = False

	def _fire_bullet(self):
		"""Creates bullet's object and adds it to sprite group."""
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_screen(self):
		"""
		Update images, background and other elements on screen, 
		flip to recently drawn screen.
		"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			if bullet.rect.top > self.screen.get_rect().top:
				bullet.draw_me()
		
		pygame.display.flip()




if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()



