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


def main():
    pygame.init()

    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    new_surface = pygame.Surface((480, 720))

    is_running = True

    while is_running:
        check_for_quit()
        main_window.fill(WINDOW_COLOUR)
        main_window.blit(new_surface, (0, 0))

        draw_tile(new_surface)
        check_for_input(new_surface)

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


# Defines Space for Tile Generation
def draw_tile(new_surface):
    pygame.draw.rect(new_surface, tile_colour, (480 * .5, 720 * .5, TILE_HEIGHT, TILE_WIDTH))


# Checks for User Input for which Tile to Generate. Struggling to get it to output.
def check_for_input(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print('hello')
                for x in range(surface.get_width()):
                    for y in range(surface.get_height()):
                        pixel = surface.get_at((x, y))
                        surface.set_at(
                            (x, y),
                            pygame.color(int(pixel.r * 0.5), pixel.g, pixel.b)
                        )


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




