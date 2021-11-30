import pygame
from coordSetup import coords, level1_pipes
from controllers import *
from assets import *

pygame.init()  # initializing pygame

WIDTH, HEIGHT = 750, 500  # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))  # creating window
FPS = 60
COLOUR = (0, 0, 0)


def main():
    CLOCK = pygame.time.Clock()
    # game loop
    running = True
    while running:
        CLOCK.tick(FPS)
        init_tiles()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_pos = pygame.mouse.get_pos()
                tile_coordinates = map_tile(Mouse_pos)
                rotate_tile(tile_coordinates)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
