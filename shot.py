import pygame

from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        LINE_WIDTH = 1
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt