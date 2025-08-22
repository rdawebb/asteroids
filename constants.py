# screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# asteroid constants
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# player constants
PLAYER_RADIUS = 20 # player hit box radius
PLAYER_TURN_SPEED = 300  # turn speed in degrees per second
PLAYER_SPEED = 200  # movement speed in pixels per second

# shot constants
SHOT_RADIUS = 5 # shot hit box radius
PLAYER_SHOOT_SPEED = 500  # shot speed in pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3  # shot cooldown in seconds