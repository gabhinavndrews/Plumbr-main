import pygame
from coordSetup import *
from assets import *
from tkinter import *
from tkinter import messagebox


pygame.init()  # initializing pygame


def rotate_tile(tilecoords):
    oldTile = 0
    tiles_list = coords.items()
    for tile in tiles_list:
        if tile[1] == tilecoords:
            oldTile = tile[0]
            # break
    pipe_values = level1_pipes[oldTile]
    for i in pipe_values:
        if(isinstance(i, int)):
            rotation_value = i
        else:
            pipe = i
    pipe_copy = pygame.transform.rotate(pipe, 180)
    if(rotation_value+90 >= 360):
        rotation_value = 0
    else:
        rotation_value = rotation_value+90
    level1_pipes[oldTile] = {pipe_copy, rotation_value}
    active_keys = level1_pipes_active_pipes.items()
    for i in active_keys:
        if(oldTile == i[0]):
            level1_pipes_active_pipes[oldTile] = rotation_value
    final_check()


def final_check():
    print(level1_pipes_active_pipes)
    print(level1_pipes_values_correct)
    if (level1_pipes_active_pipes == level1_pipes_values_correct):
        print("WE DID IT!!")
        Tk().wm_withdraw()
        messagebox.showinfo('Congratulations', 'You won!!')


def map_tile(pos):
    for i in range(25, 725, 50):
        for j in range(50, 500, 50):
            if i <= pos[0] <= i + 50:
                if j <= pos[1] <= j + 50:
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
        # print(coord)
        pipe_values = level1_pipes[i]
        # print(pipe_values)
        for i in pipe_values:
            if(isinstance(i, int)):
                rotation_value = i
            else:
                pipe = i
        # print(rotation_value)
        # print(pipe)
        pipe_copy = pipe
        pipe_copy = pygame.transform.rotate(pipe_copy, rotation_value)
        window.blit(pipe_copy, (coord[0], coord[1]))
        if(rotation_value+90 >= 360):
            rotation_value = 0
        else:
            rotation_value = rotation_value+90
        level1_pipes[i] = {pipe_copy, rotation_value}


def init_rotate(pipe_values):
    for i in pipe_values:
        if(isinstance(i, int)):
            rotation_value = i
        else:
            pipe = i
        # print(rotation_value)
        # print(pipe)
    pipe_copy = pipe
    pipe_copy = pygame.transform.rotate(pipe_copy, 90)
    return(pipe_copy)
