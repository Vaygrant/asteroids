from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self, asteroid_field_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(30,60)
        adjusted_vector_1 = self.velocity.rotate(random_angle)
        adjusted_vector_2 = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = adjusted_vector_1 * 1.2
        asteroid_field_group.add(asteroid1)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = adjusted_vector_2 * 1.2
        asteroid_field_group.add(asteroid2)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt