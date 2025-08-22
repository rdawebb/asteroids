# imports of pygame, sys, constant values and game objects
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    shots = pygame.sprite.Group() # create group for shots
    Shot.containers = (shots, updatable, drawable) # assign shot instances to groups

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

        # collision checks
        for asteroid in asteroids: # check for player collisions with asteroids
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit() # exit the game
            for shot in shots: # check for asteroid collisions with shots
                if shot.collision_check(asteroid):
                    shot.kill() # remove shot on collision
                    asteroid.split() # split or remove asteroid on collision

        for sprite in drawable:
            sprite.draw(screen) # draw player, asteroids and shots
        pygame.display.flip() # update screen
        dt = clock.tick(60) / 1000 # limit frame rate to 60 FPS

# run main game function
if __name__ == "__main__":
    main()