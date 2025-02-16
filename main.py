import pygame
from constants import *
from player import *
from circleshape import *
from asteroids import *
from AsteroidField import *
from shot_obj import * 
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")

    Asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    player.containers = (updateable, drawable)
    Asteroid.containers = (Asteroids, updateable, drawable)
    shot.containers = (updateable,drawable, bullets)

    asteroid_field = AsteroidField()
    player1 = player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updateable.update(dt)
        
        for ast in Asteroids:
            if ast.collision(player1) == True:
                print("Game Over!")
                sys.exit()

        for ast in Asteroids:
            for bullet in bullets:
                if ast.collision(bullet) == True:
                    bullet.kill()
                    ast.kill()

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()  
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()