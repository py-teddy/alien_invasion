

class Settings:
	"""A class to store all settings for alien invasion."""

	def __init__(self):
		"""Initialize game settings."""
		# Screen settings
		self.screen_width = 1360
		self.screen_height = 720
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5