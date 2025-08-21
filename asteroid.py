import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)  # draw the asteroid as a white circle

    # asteroid movement
    def update(self, dt):
        self.position += self.velocity * dt  # update position based on velocity