import pygame
import sys
import os
from coordSetup import *

favicon = pygame.image.load('pipe.png')  # favicon
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBGNew.png')
straight_pipe = pygame.image.load('StraightPipe.png')
t_pipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

coords = {'A1': (25, 50), 'A2': (25, 100), 'A3': (25, 150), 'A4': (25, 200), 'A5': (25, 250), 'A6': (25, 300), 'A7': (25, 350), 'A8': (25, 400), 'A9': (25, 450),
          'B1': (75, 50), 'B2': (75, 100), 'B3': (75, 150), 'B4': (75, 200), 'B5': (75, 250), 'B6': (75, 300), 'B7': (75, 350), 'B8': (75, 400), 'B9': (75, 450),
          'C1': (125, 50), 'C2': (125, 100), 'C3': (125, 150), 'C4': (125, 200), 'C5': (125, 25), 'C6': (125, 300), 'C7': (125, 350), 'C8': (125, 400), 'C9': (125, 450),
          'D1': (175, 50), 'D2': (175, 100), 'D3': (175, 150), 'D4': (175, 200), 'D5': (175, 25), 'D6': (175, 300), 'D7': (175, 350), 'D8': (175, 400), 'D9': (175, 450),
          'E1': (225, 50), 'E2': (225, 100), 'E3': (225, 150), 'E4': (225, 200), 'E5': (225, 25), 'E6': (225, 300), 'E7': (225, 350), 'E8': (225, 400), 'E9': (225, 450),
          'F1': (275, 50), 'F2': (275, 100), 'F3': (275, 150), 'F4': (275, 200), 'F5': (275, 25), 'F6': (275, 300), 'F7': (275, 350), 'F8': (275, 400), 'F9': (275, 450),
          'G1': (325, 50), 'G2': (325, 100), 'G3': (325, 150), 'G4': (325, 200), 'G5': (325, 25), 'G6': (325, 300), 'G7': (325, 350), 'G8': (325, 400), 'G9': (325, 450),
          'H1': (375, 50), 'H2': (375, 100), 'H3': (375, 150), 'H4': (375, 200), 'H5': (375, 25), 'H6': (375, 300), 'H7': (375, 350), 'H8': (375, 400), 'H9': (375, 450),
          'I1': (425, 50), 'I2': (425, 100), 'I3': (425, 150), 'I4': (425, 200), 'I5': (425, 25), 'I6': (425, 300), 'I7': (425, 350), 'I8': (425, 400), 'I9': (425, 450),
          'J1': (475, 50), 'J2': (475, 100), 'J3': (475, 150), 'J4': (475, 200), 'J5': (475, 25), 'J6': (475, 300), 'J7': (475, 350), 'J8': (475, 400), 'J9': (475, 450),
          'K1': (525, 50), 'K2': (525, 100), 'K3': (525, 150), 'K4': (525, 200), 'K5': (525, 25), 'K6': (525, 300), 'K7': (525, 350), 'K8': (525, 400), 'K9': (525, 450),
          'L1': (575, 50), 'L2': (575, 100), 'L3': (575, 150), 'L4': (575, 200), 'L5': (575, 25), 'L6': (575, 300), 'L7': (575, 350), 'L8': (575, 400), 'L9': (575, 450),
          'M1': (625, 50), 'M2': (625, 100), 'M3': (625, 150), 'M4': (625, 200), 'M5': (625, 25), 'M6': (625, 300), 'M7': (625, 350), 'M8': (625, 400), 'M9': (625, 450),
          'N1': (675, 50), 'N2': (675, 100), 'N3': (675, 150), 'N4': (675, 200), 'N5': (675, 25), 'N6': (675, 300), 'N7': (675, 350), 'N8': (675, 400), 'N9': (675, 450)
          }

level1_pipes = {
    'A1': {straight_pipe, 1}, 'A2': {curve_pipe, 2}, 'A3': {straight_pipe, 3}, 'A4': {t_pipe, 2}, 'A5': {curve_pipe, 2}, 'A6': {straight_pipe, 2}, 'A7': {t_pipe, 2}, 'A8': {straight_pipe, 2}, 'A9': {curve_pipe, 1},
    'B1': {straight_pipe, 1}, 'B2': {curve_pipe, 2}, 'B3': {straight_pipe, 3}, 'B4': {t_pipe, 2}, 'B5': {curve_pipe, 2}, 'B6': {straight_pipe, 2}, 'B7': {t_pipe, 2}, 'B8': {straight_pipe, 2}, 'B9': {curve_pipe, 1},
    'C1': {straight_pipe, 1}, 'C2': {curve_pipe, 2}, 'C3': {straight_pipe, 3}, 'C4': {t_pipe, 2}, 'C5': {curve_pipe, 2}, 'C6': {straight_pipe, 2}, 'C7': {t_pipe, 2}, 'C8': {straight_pipe, 2}, 'C9': {curve_pipe, 1},
    'D1': {straight_pipe, 1}, 'D2': {curve_pipe, 2}, 'D3': {straight_pipe, 3}, 'D4': {t_pipe, 2}, 'D5': {curve_pipe, 2}, 'D6': {straight_pipe, 2}, 'D7': {t_pipe, 2}, 'D8': {straight_pipe, 2}, 'D9': {curve_pipe, 1},
    'E1': {straight_pipe, 1}, 'E2': {curve_pipe, 2}, 'E3': {straight_pipe, 3}, 'E4': {t_pipe, 2}, 'E5': {curve_pipe, 2}, 'E6': {straight_pipe, 2}, 'E7': {t_pipe, 2}, 'E8': {straight_pipe, 2}, 'E9': {curve_pipe, 1},
    'F1': {straight_pipe, 1}, 'F2': {curve_pipe, 2}, 'F3': {straight_pipe, 3}, 'F4': {t_pipe, 2}, 'F5': {curve_pipe, 2}, 'F6': {straight_pipe, 2}, 'F7': {t_pipe, 2}, 'F8': {straight_pipe, 2}, 'F9': {curve_pipe, 1},
    'G1': {straight_pipe, 1}, 'G2': {curve_pipe, 2}, 'G3': {straight_pipe, 3}, 'G4': {t_pipe, 2}, 'G5': {curve_pipe, 2}, 'G6': {straight_pipe, 2}, 'G7': {t_pipe, 2}, 'G8': {straight_pipe, 2}, 'G9': {curve_pipe, 1},
    'H1': {straight_pipe, 1}, 'H2': {curve_pipe, 2}, 'H3': {straight_pipe, 3}, 'H4': {t_pipe, 2}, 'H5': {curve_pipe, 2}, 'H6': {straight_pipe, 2}, 'H7': {t_pipe, 2}, 'H8': {straight_pipe, 2}, 'H9': {curve_pipe, 1},
    'I1': {straight_pipe, 1}, 'I2': {curve_pipe, 2}, 'I3': {straight_pipe, 3}, 'I4': {t_pipe, 2}, 'I5': {curve_pipe, 2}, 'I6': {straight_pipe, 2}, 'I7': {t_pipe, 2}, 'I8': {straight_pipe, 2}, 'I9': {curve_pipe, 1},
    'J1': {straight_pipe, 1}, 'J2': {curve_pipe, 2}, 'J3': {straight_pipe, 3}, 'J4': {t_pipe, 2}, 'J5': {curve_pipe, 2}, 'J6': {straight_pipe, 2}, 'J7': {t_pipe, 2}, 'J8': {straight_pipe, 2}, 'J9': {curve_pipe, 1},
    'K1': {straight_pipe, 1}, 'K2': {curve_pipe, 2}, 'K3': {straight_pipe, 3}, 'K4': {t_pipe, 2}, 'K5': {curve_pipe, 2}, 'K6': {straight_pipe, 2}, 'K7': {t_pipe, 2}, 'K8': {straight_pipe, 2}, 'K9': {curve_pipe, 1},
    'L1': {straight_pipe, 1}, 'L2': {curve_pipe, 2}, 'L3': {straight_pipe, 3}, 'L4': {t_pipe, 2}, 'L5': {curve_pipe, 2}, 'L6': {straight_pipe, 2}, 'L7': {t_pipe, 2}, 'L8': {straight_pipe, 2}, 'L9': {curve_pipe, 1},
    'M1': {straight_pipe, 1}, 'M2': {curve_pipe, 2}, 'M3': {straight_pipe, 3}, 'M4': {t_pipe, 2}, 'M5': {curve_pipe, 2}, 'M6': {straight_pipe, 2}, 'M7': {t_pipe, 2}, 'M8': {straight_pipe, 2}, 'M9': {curve_pipe, 1},
    'N1': {straight_pipe, 1}, 'N2': {curve_pipe, 2}, 'N3': {straight_pipe, 3}, 'N4': {t_pipe, 2}, 'N5': {curve_pipe, 2}, 'N6': {straight_pipe, 2}, 'N7': {t_pipe, 2}, 'N8': {straight_pipe, 2}, 'N9': {curve_pipe, 1}
}

straight_pipe_values = (0, 1)
curved_pipe_values = (0, 1, 2, 3)
plus_pipe_values = 0
t_pipe_values = (0, 1, 2, 3)


def rotate_tile(tilecoords):
    oldTile = 0
    # stores all the tile data including the key and value of coords dict in tiles_list
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            oldTile = tile[0]
            break
    # stores the key and value of the selected pipe from the level1_pipe into a list.
    pipe_copy = list(level1_pipes[oldTile].copy())

    if(pipe_copy[1] == straight_pipe):
        pipe_copy = pygame.transform.rotate(pipe_copy[1], 90)
        for i in straight_pipe_values:
            if(pipe_copy == i):
                if i == 3:
                    level1_pipes[oldTile] = {straight_pipe, 0}
                else:
                    level1_pipes[oldTile] = {straight_pipe, i+1}
    level1_pipes[oldTile] = pipe_copy


def new_tile(pipe, tilecoords):
    newTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            newTile = tile[0]
            break
    print(newTile)
    print(level1_pipes[newTile])
    level1_pipes[newTile] = pipe
    print(level1_pipes[newTile])


def rotate_init(pipe, label):
    #print(pipe, label)
    new_pipe = 0
    if (pipe == straight_pipe):
        # print("true")
        if(label == 1):
            new_pipe = pipe
        elif(label == 2):
            new_pipe = pygame.transform.rotate(pipe, 90)
    elif(pipe == curve_pipe or pipe == t_pipe):
        if(label == 1):
            new_pipe = pipe
        elif(label == 2):
            new_pipe = pygame.transform.rotate(pipe, 90)
        elif(label == 3):
            new_pipe = pygame.transform.rotate(pipe, 180)
        elif(label == 4):
            new_pipe = pygame.transform.rotate(pipe, 270)
    elif(pipe == plus_pipe):
        new_pipe = pipe
    # print(new_pipe)
    return new_pipe


#new_tile(curve_pipe, (125, 100))
#rotate_tile((125, 100))
# print(len(t_pipe_values))
pipe = level1_pipes['A1']
label = level1_pipes_values['A1']
print(pipe)
print(label)
new_pipe = rotate_init(pipe, label)

new = rotate_init(pipe, label)
print(new)
