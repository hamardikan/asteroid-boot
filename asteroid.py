import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Save state we need (kill removes from groups but object still exists)
        pos = self.position.copy()
        vel = self.velocity
        old_radius = self.radius

        # This asteroid is always destroyed
        self.kill()

        # Small asteroids just disappear
        if old_radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        v1 = vel.rotate(angle) * 1.2
        v2 = vel.rotate(-angle) * 1.2

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(pos.x, pos.y, new_radius)
        a1.velocity = v1

        a2 = Asteroid(pos.x, pos.y, new_radius)
        a2.velocity = v2
