
import pygame

class Ship:
	"""A class to manage ship element."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Load ship image and get its rect
		self.image = pygame.image.load('game_images/ship.bmp')
		self.rect = self.image.get_rect()

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
