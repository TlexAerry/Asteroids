from circleshape import *
from constants import * 
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(split_angle)
            new_velocity2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_ast1 = Asteroid(self.position[0],self.position[1], new_radius)
            new_ast2 = Asteroid(self.position[0],self.position[1], new_radius)
            new_ast1.velocity = new_velocity1
            new_ast2.velocity = new_velocity2