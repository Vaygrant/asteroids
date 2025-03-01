import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids,updateable,drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable,drawable)

    player_character = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT /2), PLAYER_RADIUS, shots)
    asteroid_field = AsteroidField()

    game_time = pygame.time.Clock()
    dt = 0
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
              
        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)

        updateable.update(dt)

        for enemy in asteroids:
            if enemy.check_for_collision(player_character):
                        print("Game Over!")
                        return
            
            for bullet in shots:
                if bullet.check_for_collision(enemy):
                    enemy.split(asteroids)
                    bullet.kill()
    
        pygame.display.flip()
        dt = game_time.tick(60) / 1000



if __name__ == "__main__":
    main()