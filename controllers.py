import pygame
from coordSetup import coords, level1_pipes, level1_pipes_values
from assets import *


pygame.init()  # initializing pygame

rotate_values = {}


def rotate_tile(tilecoords):
    oldTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            oldTile = tile[0]
            break
    pipe_copy = level1_pipes[oldTile].copy()
    level1_pipes[oldTile] = pygame.transform.rotate(pipe_copy, 90)
    if(level1_pipes[oldTile] == straight_pipe):
        if(level1_pipes_values[oldTile] == 1):
            level1_pipes_values[oldTile] = 2
        elif(level1_pipes_values[oldTile] == 2):
            level1_pipes_values[oldTile] = 1
    elif(level1_pipes[oldTile] == curve_pipe or level1_pipes[oldTile] == t_pipe):
        if(level1_pipes_values[oldTile] == 1):
            level1_pipes_values[oldTile] = 2
        elif(level1_pipes_values[oldTile] == 2):
            level1_pipes_values[oldTile] = 3
        elif(level1_pipes_values[oldTile] == 3):
            level1_pipes_values[oldTile] = 4
        elif(level1_pipes_values[oldTile] == 4):
            level1_pipes_values[oldTile] = 1
    elif(level1_pipes[oldTile] == plus_pipe):
        level1_pipes_values[oldTile] = 1


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


def rotate_init(pipe, label):
    #print(pipe, label)
    new_pipe = 0
    if(pipe == straight_pipe):
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
    return new_pipe


def init_tiles():
    window.fill(COLOUR)
    window.blit(background, (0, 0))
    for i in coords.keys():
        coord = coords[i]
        pipe = level1_pipes[i]
        label = level1_pipes_values[i]
        new_pipe = rotate_init(pipe, label)
        window.blit(new_pipe, (coord[0], coord[1]))
