import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw the asteroid as a white circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    # asteroid movement
    def update(self, dt):
        self.position += self.velocity * dt  # update position based on velocity

    # split the asteroid into smaller pieces if necessary
    def split(self):
        self.kill()  # remove the current asteroid
        
        if self.radius <= ASTEROID_MIN_RADIUS: # check asteroid size
            return # no split if asteroid too small

        random_angle = random.uniform(20, 50) # generate random angle for splitting
        new_radius = self.radius - ASTEROID_MIN_RADIUS # calculate new radius for smaller asteroids

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) # new smaller asteroid 1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius) # new smaller asteroid 2
        asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2 # change angle and increase speed of asteroid 1
        asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2 # change angle and increase speed of asteroid 2