import pygame
import sys
from pygame.locals import *

green = (40, 255, 30)
brown = (40, 60, 90)
red = (155, 20, 30)
yellow = (0, 155, 155)
skyBlue = (135, 206, 235)
waterBlue = (0, 119, 190)

grass = 0
dirt = 1
lava = 2
sky = 3
water = 4

# Creates a dictionary for the tiles
colours = {
    grass: green,
    dirt: brown,
    lava: red,
    sky: skyBlue,
    water: waterBlue
}

tilemap = [
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky],
    [water, water, water, water, water, water, water, water, water, water, water, water, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky, sky]
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
            pygame.quit()
            sys.exit()
        pygame.event.post(event)

    for row in range(mapHeight):
        for column in range(mapWidth):
            pygame.draw.rect(screen, colours[tilemap[row][column]],
                             (column * tilesize, row * tilesize, tilesize, tilesize))
    pygame.display.update()
