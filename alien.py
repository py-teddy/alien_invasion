
import pygame
from pygame.sprite import Sprite # Alien objects would need sprite functionality

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize alien and set its starting position."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        # Load alien image and set its rect attribute.
        self.image = pygame.image.load("game_images/alien.bmp")
        self.rect = self.image.get_rect()

        # Setting image position to near topleft
        self.rect.x = self.rect.width # horizontal space equal to alien width
        self.rect.y = self.rect.height

        # Store each alien precise horizontal position
        self.x = float(self.rect.x)