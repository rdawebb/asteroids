# imports of pygame and constant values
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# main game function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create screen object
    clock = pygame.time.Clock() # create clock object
    dt = 0 # delta time
    
    updatable = pygame.sprite.Group() # create group for updatable objects
    drawable = pygame.sprite.Group() # create group for drawable objects
    Player.containers = (updatable, drawable) # assign player instance to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player object

    asteroids = pygame.sprite.Group() # create group for asteroids
    Asteroid.containers = (asteroids, updatable, drawable) # assign asteroid instances to groups
    AsteroidField.containers = (updatable) # assign asteroid field to groups
    asteroid_field = AsteroidField() # create asteroid field object

    # command line start message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop with screen updates and filled black background
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for quit event
                return
        screen.fill((0, 0, 0)) # fill screen with black
        updatable.update(dt) # update movement
        for sprite in drawable:
            sprite.draw(screen) # draw player and asteroids
        pygame.display.flip() # update screen
        dt = clock.tick(60) / 1000 # limit frame rate to 60 FPS

# run main game function
if __name__ == "__main__":
    main()