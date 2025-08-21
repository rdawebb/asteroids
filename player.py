import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Player's rotation angle

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2) # draw the triangle coloured white

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # update rotation angle

    def update(self, dt):
        keys = pygame.key.get_pressed() # get the state of all keyboard buttons

        if keys[pygame.K_a]: # if a is pressed
            self.rotate(-dt) # rotate left
        if keys[pygame.K_d]: # if d is pressed
            self.rotate(dt) # rotate right

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]