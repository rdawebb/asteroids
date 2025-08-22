import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # draw the shot as a red circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width=0)

    # shot movement
    def update(self, dt):
        self.position += self.velocity * dt