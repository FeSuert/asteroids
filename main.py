import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    dt = 0 

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot):
                    obj.split()
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
