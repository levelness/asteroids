import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        LINE_WIDTH = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_first = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_first.velocity = self.velocity.rotate(random_angle) * 1.2

        new_asteroid_second = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_second.velocity = self.velocity.rotate(random_angle * -1) * 1.2

        self.kill()
            