import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        angle = random.uniform(20,50)
        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        new_asteroid_1.velocity = new_vector_1 * 1.2 
        new_asteroid_2.velocity = new_vector_2 * 1.2

        

        