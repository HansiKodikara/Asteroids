import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_object = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_object.update(dt)
        player_object.draw(screen)
        pygame.display.flip()
        dt_ms = clock.tick(60)
        dt = dt_ms/1000

if __name__ == "__main__":
    main()
