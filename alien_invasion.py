import sys

import pygame

from settings import Settings
from ship import Ship

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

		# creating ship element
		self.ship = Ship(self)

	def run_game(self):
		"""Start main loop for game."""
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		"""Respond to keypress and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""
		Update images, background and other elements on screen, 
		flip to recently drawn screen.
		"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()




if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()



