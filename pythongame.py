import pygame

pygame.init()  # initializing pygame

pygame.display.set_caption('Plumr')  # creating title of game

# loading assets
favicon = pygame.image.load('pipe.png')  # favicon
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBGNew.png')
straight_pipe = pygame.image.load('StraightPipe.png')
t_pipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

WIDTH, HEIGHT = 750, 500  # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))  # creating window
FPS = 60
COLOUR = (0, 0, 0)

pipes = (straight_pipe, t_pipe, plus_pipe, curve_pipe)

coords = {'A1': (25, 50), 'A2': (25, 100), 'A3': (25, 150), 'A4': (25, 200), 'A5': (25, 250), 'A6': (25, 300), 'A7': (25, 350), 'A8': (25, 400), 'A9': (25, 450),
          'B1': (75, 50), 'B2': (75, 100), 'B3': (75, 150), 'B4': (75, 200), 'B5': (75, 250), 'B6': (75, 300), 'B7': (75, 350), 'B8': (75, 400), 'B9': (75, 450),
          'C1': (125, 50), 'C2': (125, 100), 'C3': (125, 150), 'C4': (125, 200), 'C5': (125, 250), 'C6': (125, 300), 'C7': (125, 350), 'C8': (125, 400), 'C9': (125, 450),
          'D1': (175, 50), 'D2': (175, 100), 'D3': (175, 150), 'D4': (175, 200), 'D5': (175, 250), 'D6': (175, 300), 'D7': (175, 350), 'D8': (175, 400), 'D9': (175, 450),
          'E1': (225, 50), 'E2': (225, 100), 'E3': (225, 150), 'E4': (225, 200), 'E5': (225, 250), 'E6': (225, 300), 'E7': (225, 350), 'E8': (225, 400), 'E9': (225, 450),
          'F1': (275, 50), 'F2': (275, 100), 'F3': (275, 150), 'F4': (275, 200), 'F5': (275, 250), 'F6': (275, 300), 'F7': (275, 350), 'F8': (275, 400), 'F9': (275, 450),
          'G1': (325, 50), 'G2': (325, 100), 'G3': (325, 150), 'G4': (325, 200), 'G5': (325, 250), 'G6': (325, 300), 'G7': (325, 350), 'G8': (325, 400), 'G9': (325, 450),
          'H1': (375, 50), 'H2': (375, 100), 'H3': (375, 150), 'H4': (375, 200), 'H5': (375, 250), 'H6': (375, 300), 'H7': (375, 350), 'H8': (375, 400), 'H9': (375, 450),
          'I1': (425, 50), 'I2': (425, 100), 'I3': (425, 150), 'I4': (425, 200), 'I5': (425, 250), 'I6': (425, 300), 'I7': (425, 350), 'I8': (425, 400), 'I9': (425, 450),
          'J1': (475, 50), 'J2': (475, 100), 'J3': (475, 150), 'J4': (475, 200), 'J5': (475, 250), 'J6': (475, 300), 'J7': (475, 350), 'J8': (475, 400), 'J9': (475, 450),
          'K1': (525, 50), 'K2': (525, 100), 'K3': (525, 150), 'K4': (525, 200), 'K5': (525, 250), 'K6': (525, 300), 'K7': (525, 350), 'K8': (525, 400), 'K9': (525, 450),
          'L1': (575, 50), 'L2': (575, 100), 'L3': (575, 150), 'L4': (575, 200), 'L5': (575, 250), 'L6': (575, 300), 'L7': (575, 350), 'L8': (575, 400), 'L9': (575, 450),
          'M1': (625, 50), 'M2': (625, 100), 'M3': (625, 150), 'M4': (625, 200), 'M5': (625, 250), 'M6': (625, 300), 'M7': (625, 350), 'M8': (625, 400), 'M9': (625, 450),
          'N1': (675, 50), 'N2': (675, 100), 'N3': (675, 150), 'N4': (675, 200), 'N5': (675, 250), 'N6': (675, 300), 'N7': (675, 350), 'N8': (675, 400), 'N9': (675, 450)
          }

level1_pipes = {
    'A1': straight_pipe, 'A2': curve_pipe, 'A3': straight_pipe, 'A4': t_pipe, 'A5': curve_pipe, 'A6': straight_pipe, 'A7': t_pipe, 'A8': straight_pipe, 'A9': curve_pipe,
    'B1': straight_pipe, 'B2': curve_pipe, 'B3': straight_pipe, 'B4': t_pipe, 'B5': curve_pipe, 'B6': straight_pipe, 'B7': t_pipe, 'B8': straight_pipe, 'B9': curve_pipe,
    'C1': straight_pipe, 'C2': curve_pipe, 'C3': straight_pipe, 'C4': t_pipe, 'C5': curve_pipe, 'C6': straight_pipe, 'C7': t_pipe, 'C8': straight_pipe, 'C9': curve_pipe,
    'D1': straight_pipe, 'D2': curve_pipe, 'D3': straight_pipe, 'D4': t_pipe, 'D5': curve_pipe, 'D6': straight_pipe, 'D7': t_pipe, 'D8': straight_pipe, 'D9': curve_pipe,
    'E1': straight_pipe, 'E2': curve_pipe, 'E3': straight_pipe, 'E4': t_pipe, 'E5': curve_pipe, 'E6': straight_pipe, 'E7': t_pipe, 'E8': straight_pipe, 'E9': curve_pipe,
    'F1': straight_pipe, 'F2': curve_pipe, 'F3': straight_pipe, 'F4': t_pipe, 'F5': curve_pipe, 'F6': straight_pipe, 'F7': t_pipe, 'F8': straight_pipe, 'F9': curve_pipe,
    'G1': straight_pipe, 'G2': curve_pipe, 'G3': straight_pipe, 'G4': t_pipe, 'G5': curve_pipe, 'G6': straight_pipe, 'G7': t_pipe, 'G8': straight_pipe, 'G9': curve_pipe,
    'H1': straight_pipe, 'H2': curve_pipe, 'H3': straight_pipe, 'H4': t_pipe, 'H5': curve_pipe, 'H6': straight_pipe, 'H7': t_pipe, 'H8': straight_pipe, 'H9': curve_pipe,
    'I1': straight_pipe, 'I2': curve_pipe, 'I3': straight_pipe, 'I4': t_pipe, 'I5': curve_pipe, 'I6': straight_pipe, 'I7': t_pipe, 'I8': straight_pipe, 'I9': curve_pipe,
    'J1': straight_pipe, 'J2': curve_pipe, 'J3': straight_pipe, 'J4': t_pipe, 'J5': curve_pipe, 'J6': straight_pipe, 'J7': t_pipe, 'J8': straight_pipe, 'J9': curve_pipe,
    'K1': straight_pipe, 'K2': curve_pipe, 'K3': straight_pipe, 'K4': t_pipe, 'K5': curve_pipe, 'K6': straight_pipe, 'K7': t_pipe, 'K8': straight_pipe, 'K9': curve_pipe,
    'L1': straight_pipe, 'L2': curve_pipe, 'L3': straight_pipe, 'L4': t_pipe, 'L5': curve_pipe, 'L6': straight_pipe, 'L7': t_pipe, 'L8': straight_pipe, 'L9': curve_pipe,
    'M1': straight_pipe, 'M2': curve_pipe, 'M3': straight_pipe, 'M4': t_pipe, 'M5': curve_pipe, 'M6': straight_pipe, 'M7': t_pipe, 'M8': straight_pipe, 'M9': curve_pipe,
    'N1': straight_pipe, 'N2': curve_pipe, 'N3': straight_pipe, 'N4': t_pipe, 'N5': curve_pipe, 'N6': straight_pipe, 'N7': t_pipe, 'N8': straight_pipe, 'N9': curve_pipe,

}


def rotate_tile(tilecoords):
    oldTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            oldTile = tile[0]
            break
    pipe_copy = level1_pipes[oldTile].copy()
    pipe_copy = pygame.transform.rotate(pipe_copy, 90)
    level1_pipes[oldTile] = pipe_copy


def map_tile(Mouse_pos):
    for i in range(25, 725, 50):
        for j in range(50, 500, 50):
            if(i <= Mouse_pos[0] <= i+50):
                if(j <= Mouse_pos[1] <= j+50):
                    return i, j


def new_tile(pipe, tilecoords):
    newTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            newTile = tile[0]
            break
    level1_pipes[newTile] = pipe


def init_tiles():
    window.fill(COLOUR)
    window.blit(background, (0, 0))
    for i in coords.keys():
        coord = coords[i]
        pipe = level1_pipes[i]
        window.blit(pipe, (coord[0], coord[1]))


def main():
    pipe = curve_pipe
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
