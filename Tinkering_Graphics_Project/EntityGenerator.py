import sys
import os
import pygame
import random

FPS_CLOCK = pygame.time.Clock()
FPS = 30

PROGRAM_CAPTION = "Entity Generator"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    pygame.init()

    main_screen = (pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))
    pygame.display.set_caption(PROGRAM_CAPTION)

    is_running = True

    while is_running:
        main_screen.fill(BLACK)
        check_for_quit()

        #rectangle = Rectangle((WINDOW_WIDTH * .5, WINDOW_HEIGHT * .5), WHITE, pygame.Rect(0, 0, 5, 5))
        #rectangle.draw_shape(main_screen)

        if get_input():
            image = pygame.image.load(str(os.getcwd()) + "\\Images\\" + "Cactus.png")
            save_image(image, "New_Cactus.png", os.getcwd())

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


def save_image(image, file_name="", path=os.path):
    # Saves and image to the directory path of
    # the project in a sub folder of Images
    pygame.image.save(image, str(path) + "\\Images\\" + file_name)
    print("Image has saved as: " + file_name)


def get_random_colour():
    # Returns a random colour from the entire colour spectrum
    colour = [0, 0, 0]
    for i in range(0, 2):
        colour[i] = random.randint(0, 255)

    return tuple(colour)


def draw_shapes(main_display, shapes=[]):
    for i in range(0, len(shapes)):
        pygame.draw.polygon(main_display, shapes[i].colour, shapes[i].rect)
        # Can make it blit and recentre here


def get_input():
    # Returns a boolean to state if any button has been pressed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                return True
        pygame.event.post(event)

    return False


def check_for_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate_program()
        pygame.event.post(event)


def terminate_program():
    pygame.quit()
    sys.exit()


class Shape:
    def __init__(self, position=(0, 0), colour=(0, 0, 0)):
        self.position = position
        self.colour = colour

    def draw_shape(self, main_screen=pygame.Surface):
        pass


class Rectangle(Shape):
    def __init__(self, position=(0, 0), colour=(0, 0, 0), bounds=pygame.Rect(0, 0, 0, 0)):
        super(Rectangle, self).__init__(position, colour)

        bounds.center = (position[0], position[1])
        self.bounds = bounds

    def draw_shape(self, main_screen=pygame.Surface):
        super(Rectangle, self).draw_shape(main_screen)
        pygame.draw.rect(main_screen, self.colour, self.bounds)


class Circle(Shape):
    def __init__(self, position=(0, 0), colour=(0, 0, 0), radius=0):
        super(Circle, self).__init__()
        self.radius = radius

    def draw_shape(self, main_screen=pygame.Surface):
        # COME BACK AND FIX IT NOT DRAWING
        super(Circle, self).draw_shape(main_screen)
        pygame.draw.circle(main_screen, self.colour, self.position, self.radius)


if __name__ == '__main__':
    main()
