import sys
import pygame

PROGRAM_CAPTION = "Tile Generator"
FPS_CLOCK = pygame.time.Clock()
FPS = 30

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 460
WINDOW_COLOUR = 0, 0, 0

TILE_HEIGHT = 20
TILE_WIDTH = 20
tile_colour = 255, 255, 255


def main():
    pygame.init()

    main_window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

    is_running = True

    while is_running:
        check_for_quit()
        main_window.fill(WINDOW_COLOUR)

        check_for_input()
        draw_tile(main_window)

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


# Defines Space for Tile Generation
def draw_tile(main_window):
    tile = pygame.draw.rect(main_window, tile_colour, (WINDOW_HEIGHT * .5, WINDOW_WIDTH * .5, TILE_HEIGHT, TILE_WIDTH))


# Checks for User Input for which Tile to Generate. Struggling to get it to output.
def check_for_input():

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:

        pygame.event.post(event)



def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_program()


def quit_program():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()




