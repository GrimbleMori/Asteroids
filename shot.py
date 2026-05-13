import pygame
import circleshape as cs
import constants

class Shot(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, constants.SHOT_RADIUS, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

