# imports of pygame and constant values
import pygame
from constants import *
from player import Player

# main game function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create screen object
    clock = pygame.time.Clock() # create clock object
    dt = 0 # delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player object
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop with screen updates and filled black background
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for quit event
                return
        screen.fill((0, 0, 0)) # fill screen with black
        player.update(dt) # update player rotation
        player.draw(screen) # draw player
        pygame.display.flip() # update screen
        dt = clock.tick(60) / 1000 # limit frame rate to 60 FPS

# run main game function
if __name__ == "__main__":
    main()