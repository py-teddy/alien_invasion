
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from spaceship!"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullet_color = self.settings.bullet_color

        # Create bullet rect value at 0,0, then pull position from settings
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_color)
        # aligning bullet position with moving ship
        self.rect.midtop = self.ai_game.ship.rect.midtop

        # Storing bullet's position as decimal value(for precise adjustments)
        self.y = float(self.rect.y)

    def update(self):
        """Move's a shot bullet up the screen."""
        # Update decimal position y of bullet object
        self.y -= self.settings.bullet_speed
        # update rect's y coordinate/attribute value to current 'y' value
        self.rect.y = self.y

    def draw_me(self):
        """Draw rectangular bullets on to screen in the updated location."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
