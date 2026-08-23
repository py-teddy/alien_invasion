
import pygame

class Ship:
	"""A class to manage ship element."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		self.settings = ai_game.settings # Take it's instance of settings class
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Load ship image and get its rect
		self.image = pygame.image.load('game_images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom
		# Store a decimal value for ship's horizontal position
		self.f_x = float(self.rect.x)

		# Ship movement flags
		self.ship_moving_right = False
		self.ship_moving_left = False

	def update_ship(self):
		"""Update ship's location in correspondence to keypresses."""
		# Increment values at rate of set ship speed of f_x and not rect
		if self.ship_moving_right and self.rect.right < self.screen_rect.right:
			self.f_x += self.settings.ship_speed 
		if self.ship_moving_left and self.rect.left > 0:
			self.f_x -= self.settings.ship_speed # (leftwards)
		# Update rect object from self.f_rect
		self.rect.x = self.f_x
	
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
