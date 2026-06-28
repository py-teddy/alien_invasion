import sys

import pygame

class AlienInvasion:
	""" Overall class to manage game assests and behavior."""

	def __init__(self):
		"""Define game attributes, create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")

	def run_game(self):
		"""Start main loop for game."""
		while True:
			# Watch out for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()


		# Makes most recently drawn screen visible
		pygame.display.flip()



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()


