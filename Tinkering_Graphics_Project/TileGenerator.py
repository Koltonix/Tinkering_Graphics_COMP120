"""

Pair Programmed with Christopher Robertson
"""

import sys
import pygame

PROGRAM_CAPTION = "Tile Generator"
FPS_CLOCK = pygame.time.Clock()
FPS = 30

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 960
WINDOW_COLOUR = 0, 0, 0

TILE_HEIGHT = 200
TILE_WIDTH = 200
tile_colour = 255, 255, 255

current_colour_overlay = (0, 0, 0)


def main():
    global current_colour_overlay
    pygame.init()

    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    new_surface = pygame.Surface((480, 720))

    is_running = True

    while is_running:
        print(current_colour_overlay)
        check_for_quit()
        main_window.fill(WINDOW_COLOUR)

        draw_tile(new_surface)

        check_for_input(new_surface)
        print(current_colour_overlay)
        if current_colour_overlay is not None:
            set_image_pixels(new_surface, current_colour_overlay)

        main_window.blit(new_surface, (0, 0))

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


# Defines Space for Tile Generation
def draw_tile(new_surface):
    pygame.draw.rect(new_surface, tile_colour, (480 * .5, 720 * .5, TILE_HEIGHT, TILE_WIDTH))


# Checks for User Input for which Tile to Generate. Struggling to get it to output.
def check_for_input(image=pygame.Surface):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            global current_colour_overlay

            if event.key == pygame.K_q:
                current_colour_overlay = (255, 255, 255)

            elif event.key == pygame.K_w:
                current_colour_overlay = (55, 55, 55)


def set_image_pixels(image=pygame.Surface, colour=(0, 0, 0)):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_at((x, y))
            adjusted_pixel_colour = (pixel[0] - colour[0], pixel[1] - colour[1], pixel[2] - colour[2])

            if adjusted_pixel_colour[0] * adjusted_pixel_colour[1] * adjusted_pixel_colour[2] < 0:
                continue

            image.set_at((x, y), adjusted_pixel_colour)


def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_program()
        else:
            pygame.event.post(event)


def quit_program():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()




