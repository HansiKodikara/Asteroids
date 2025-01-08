import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = None

    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.add(self.containers)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt