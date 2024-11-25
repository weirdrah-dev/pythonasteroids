import pygame, random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            adjust_angle = random.uniform(20,50)
            new_velocity_one = self.velocity.rotate(adjust_angle) * 1.2
            new_velocity_two = self.velocity.rotate(adjust_angle * -1) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = new_velocity_one
            asteroid_two.velocity = new_velocity_two

    def update(self, dt):
        self.position += self.velocity * dt