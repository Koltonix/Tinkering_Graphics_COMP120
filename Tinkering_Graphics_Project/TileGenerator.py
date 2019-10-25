import sys
import pygame

"""
This program presents the user with a blank white tile.
The user can change the appearance of the tile using the qwert keys.
The will change the appearance of the tile to colours representing grass, dirt, water, etc... 

Pair Programmed with Christopher Robertson
"""

__author__ = "James Mead Heath"
__copyright__ = "MIT License Copyright (c) 2019"

PROGRAM_CAPTION = "Tile Generator"
FPS_CLOCK = pygame.time.Clock()
FPS = 30

# Defining the Main Window size and Colour
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 960
WINDOW_COLOUR = 0, 0, 0

# Defining the size of the surface which the tile is drawn on
SURFACE_WIDTH = 300
SURFACE_HEIGHT = 300

# Defining the size and default colour for the tile when the program is loaded
TILE_HEIGHT = 200
TILE_WIDTH = 200
tile_colour = 255, 255, 255

# Needed to hold the value of the new colour of the tile
new_tile_colour = (0, 0, 0)


# Creates a game loop that will constantly update itself dependant on user input
def main():
    global new_tile_colour
    pygame.init()

    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    new_surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

    is_running = True

    while is_running:
        print(new_tile_colour)
        check_for_quit()
        main_window.fill(WINDOW_COLOUR)

        draw_tile(new_surface)

        check_for_input(new_surface)
        print(new_tile_colour)
        if new_tile_colour is not None:
            set_image_pixels(new_surface, new_tile_colour)

        main_window.blit(new_surface, (0, 0))

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


# Defines Space for Tile Generation
def draw_tile(new_surface):
    pygame.draw.rect(new_surface, tile_colour, (SURFACE_WIDTH * .5, SURFACE_WIDTH * .5, TILE_HEIGHT, TILE_WIDTH))


# Checks for User Input for which Tile to Generate.
def check_for_input(image=pygame.Surface):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            global new_tile_colour

            # Pressing q will result in a green grass tile being generated
            if event.key == pygame.K_q:
                new_tile_colour = (255, 1, 255)

            # Pressing w will result in a blue water tile being generated
            elif event.key == pygame.K_w:
                new_tile_colour = (255, 255, 1)

            # Pressing r will result in a brown dirt tile being generated
            elif event.key == pygame.K_r:
                new_tile_colour = (125, 196, 235)

            # Pressing e will result in a light blue sky tile being generated
            elif event.key == pygame.K_e:
                new_tile_colour = (255, 100, 25)

            # Pressing t will result in the default white tile being generated
            elif event.key == pygame.K_t:
                new_tile_colour = (0, 0, 0)


# Needed to change the pixel colours within the tile, gets the range of pixels on the surface
def set_image_pixels(image=pygame.Surface, colour=(0, 0, 0)):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_at((x, y))
            adjusted_pixel_colour = (pixel[0] - colour[0], pixel[1] - colour[1], pixel[2] - colour[2])

            if adjusted_pixel_colour[0] * adjusted_pixel_colour[1] * adjusted_pixel_colour[2] < 0:
                continue

            image.set_at((x, y), adjusted_pixel_colour)


# Needed to check if the user is trying to quit the program
def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_program()
        else:
            pygame.event.post(event)


# Needed so that the program will quit when the user chooses to
def quit_program():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()




