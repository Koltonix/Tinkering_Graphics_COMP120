import sys
import os
import pygame
import random

FPS_CLOCK = pygame.time.Clock()
FPS = 30

PROGRAM_CAPTION = "Entity Generator"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


def main():
    pygame.init()

    print(os.path)

    main_screen = (pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))
    pygame.display.set_caption(PROGRAM_CAPTION)

    print(get_random_colour())

    print(str(os.getcwd()) + "\\Images\\" + "Cactus.png")
    image = pygame.image.load(str(os.getcwd()) + "\\Images\\" + "Cactus.png")
    save_image(image, "New_Cactus.png", os.getcwd())

    is_running = True
    while is_running:
        check_for_quit()

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


def save_image(image, file_name="", path=os.path):
    pygame.image.save(image, str(path) + "\\Images\\" + file_name)
    print("Image has saved as: " + file_name)


def get_random_colour():
    # Returns a random colour from the entire colour spectrum
    colour = [0, 0, 0]
    for i in range(0, 2):
        colour[i] = random.randint(0, 255)

    return tuple(colour)


def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate_program()
        pygame.event.post(event)


def terminate_program():
    pygame.quit()
    sys.exit()


class BodyPart:
    def __init__(self, colour=(0, 0, 0)):
        self.colour = colour


if __name__ == '__main__':
    main()
