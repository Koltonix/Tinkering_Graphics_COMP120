# Developed by Callum Metcalfe

import pygame
from pygame.locals import *
import random
import sys


# Draws each tile based on the size of the tile map
def draw_tiles():
    for row in range(mapHeight):
        for column in range(mapWidth):
            pygame.draw.rect(screen, colours[tile_map[row][column]],
                             (column * tile_size, row * tile_size, tile_size, tile_size))


# Designates the colour to be used
green = (40, 255, 30)
brown = (139, 69, 19)
red = (155, 20, 30)
yellow = (0, 155, 155)
skyBlue = (135, 206, 235)
waterBlue = (0, 119, 190)
platform_colour = (255, 140, 0)

grass = 0
dirt = 1
lava = 2
water = 3
platform = 4
sky = 5

# Creates a dictionary for the tiles
colours = {
    grass: green,
    dirt: brown,
    lava: red,
    sky: skyBlue,
    water: waterBlue,
    platform: platform_colour
}


# Tells the program what each tile should be
def gen_tile_map():
    global tile_map
    tile_map = [
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5),
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5), sky, sky, sky, sky, sky, sky, sky, sky, sky,
         random.randint(4, 5),
         sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5)],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5),
         sky, sky, random.randint(4, 5), sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5)],
        [sky, sky, sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5)
            , sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5), random.randint(4, 5), random.randint(4, 5), random.randint(4, 5), random.randint(4, 5),
         random.randint(4, 5),
         sky, sky, sky, sky, sky, sky, sky, sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
         sky,
         sky, sky, sky, sky, sky, sky, sky, sky, sky],
        [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3)],
        [random.randint(1, 1), random.randint(1, 1), random.randint(1, 1), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
         random.randint(0, 3), random.randint(0, 3)]
    ]


# randomly generates the bottom layer of the tile map

# Game Dimensions
tile_size = 32
mapWidth = 32
mapHeight = 16

pygame.init()
screen = pygame.display.set_mode((mapWidth * tile_size, mapHeight * tile_size))

is_running = True

gen_tile_map()

while is_running:
    draw_tiles()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.event.post(event)

    pygame.display.update()
