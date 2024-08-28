import pygame
from constants import *
from circleshape import CircleShape 
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            # Small asteroid; splits into nothing
            return
        else:
            randomAngle = random.uniform(20, 50)
            newVector1 = self.velocity.rotate(randomAngle)
            newVector2 = self.velocity.rotate(-randomAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            newAsteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            newAsteroid1.velocity = newVector1 * 1.2
            newAsteroid2.velocity = newVector2 * 1.2
            

        
