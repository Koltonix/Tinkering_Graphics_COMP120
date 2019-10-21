# Developed by Callum Metcalfe

import pygame
import sys
from pygame.locals import *
import random

# Designates the colour to be used
green = (40, 255, 30)
brown = (139, 69, 19)
red = (155, 20, 30)
yellow = (0, 155, 155)
skyBlue = (135, 206, 235)
waterBlue = (0, 119, 190)

grass = 0
dirt = 1
lava = 2
water = 3
sky = 4

# Creates a dictionary for the tiles
colours = {
    grass: green,
    dirt: brown,
    lava: red,
    sky: skyBlue,
    water: waterBlue
}

# Tells the program what each tile should be
tilemap = [
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky,
     sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3)],  # Randomly generates the bottom two layers of the tilemap
    [random.randint(1, 1), random.randint(1, 1), random.randint(1, 1), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3),
     random.randint(0, 3), random.randint(0, 3)]
]

# Game Dimensions
tilesize = 32
mapWidth = 32
mapHeight = 16

pygame.init()
screen = pygame.display.set_mode((mapWidth * tilesize, mapHeight * tilesize))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
            pygame.quit()
        pygame.event.post(event)

    # Draws each tile based on the size of the tilemap
    for row in range(mapHeight):
        for column in range(mapWidth):
            pygame.draw.rect(screen, colours[tilemap[row][column]],
                             (column * tilesize, row * tilesize, tilesize, tilesize))
    pygame.display.update()
