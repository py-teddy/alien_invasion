
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

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Ship movement flags
		self.is_ship_moving_right = False
		self.is_ship_moving_left = False

	def update_ship(self):
		"""Update ship's location in correspondence to keypresses."""
		if self.is_ship_moving_right:
			self.rect.x += 1 # Increment rect x value by a pixel
		if self.is_ship_moving_left:
			self.rect.x += -1 # Reduce rect x value by a pixel(leftwards)
	
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
