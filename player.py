import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # Player's rotation angle
        self.shot_timer = 0  # Timer for shot cooldown

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2) # draw the triangle coloured white

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # update rotation angle

    def update(self, dt):
        self.shot_timer -= dt # decrease shot timer
        keys = pygame.key.get_pressed() # get the state of all keyboard buttons
        
        # key controls
        if keys[pygame.K_LEFT]: # if left arrow is pressed
            self.rotate(-dt)  # rotate left
        if keys[pygame.K_RIGHT]:  # if right arrow is pressed
            self.rotate(dt)  # rotate right
        if keys[pygame.K_UP]:  # if up arrow is pressed
            self.move(dt)  # move forward
        if keys[pygame.K_DOWN]:  # if down arrow is pressed
            self.move(-dt)  # move backward
        if keys[pygame.K_SPACE]:  # if space is pressed
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # get the forward direction
        self.position += forward * PLAYER_SPEED * dt # update player position

    def shoot(self):
        if self.shot_timer <= 0: # only run if cooldown is over
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN # reset shot timer

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]