import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    isRunnng = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, drawable_group, updateable_group)
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidField = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while isRunnng:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        
        updateable_group.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collision(player) == True:
                print("Game Over!")
                isRunnng = False

        for asteroid in asteroids_group:
            for shot in shots_group:
                if shot.collision(asteroid) == True:
                    asteroid.split()
        
        for object in drawable_group:
            object.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
