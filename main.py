import pygame
from constants import *

def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while (True):
        pygame.display.flip()



if __name__ == "__main__":
    main()