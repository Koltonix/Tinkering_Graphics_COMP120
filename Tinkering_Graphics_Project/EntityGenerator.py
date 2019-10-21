import sys
import os
import pygame
import random

FPS_CLOCK = pygame.time.Clock()
FPS = 30

PROGRAM_CAPTION = "Entity Generator"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
SCREEN_CENTRE = ((WINDOW_WIDTH * .5), (WINDOW_HEIGHT * .5))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BUTTON_COLOUR = WHITE
FONT_COLOUR = BLACK
BACKGROUND_COLOUR = BLACK

BASIC_FONT_SIZE = 20

shapes_to_render = []
buttons_to_render = []


def main():
    global main_screen, image_screen

    pygame.init()

    basic_font = pygame.font.Font("freesansbold.ttf", BASIC_FONT_SIZE)

    main_screen = (pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)))
    image_screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(PROGRAM_CAPTION)

    set_shapes()
    set_buttons(basic_font)

    is_running = True

    while is_running:
        main_screen.fill(BACKGROUND_COLOUR)
        check_for_quit()

        draw_shapes(shapes_to_render)
        draw_buttons(buttons_to_render)

        if get_input():
            # image = pygame.image.load(str(os.getcwd()) + "\\Images\\" + "Cactus.png")
            cropped_surface = crop_image(image_screen, BACKGROUND_COLOUR)
            save_image(cropped_surface, "saved_image.png", os.getcwd())

        check_button_press(buttons_to_render)

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


def set_shapes():
    centre_body = Circle(SCREEN_CENTRE, BLUE, 50)
    shapes_to_render.append(centre_body)

    square_head = Rectangle((SCREEN_CENTRE[0], SCREEN_CENTRE[1] - 50), WHITE, pygame.Rect(0, 0, 50, 50))
    shapes_to_render.append(square_head)

    triangle = Polygon((0, 0), RED, [(SCREEN_CENTRE[0] - 50, SCREEN_CENTRE[1] - 75),
                                     (SCREEN_CENTRE[0], SCREEN_CENTRE[1] - 125),
                                     (SCREEN_CENTRE[0] + 50, SCREEN_CENTRE[1] - 75)])

    shapes_to_render.append(triangle)


def set_buttons(font):
    save_button = generate_text(font, "Save Image", FONT_COLOUR, BUTTON_COLOUR, (75, 100))
    buttons_to_render.append((save_button[0], save_button[1], "SAVE"))

    circle_button = generate_text(font, "Circle", FONT_COLOUR, BUTTON_COLOUR, (75, 125))
    buttons_to_render.append((circle_button[0], circle_button[1], "CIRCLE"))


def draw_shapes(shapes):
    for i in range(0, len(shapes)):
        shapes[i].draw_shape()
        main_screen.blit(image_screen, (0, 0))


def draw_buttons(buttons=[]):
    for i in range(0, len(buttons)):
        main_screen.blit(buttons[i][0], buttons[i][1])


def check_button_press(buttons=[]):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(0, len(buttons)):
                if buttons[i][1].collidepoint(pygame.mouse.get_pos()):
                    if buttons[i][2] == "SAVE":
                        cropped_surface = crop_image(image_screen, BACKGROUND_COLOUR)
                        save_image(cropped_surface, "saved_image.png", os.getcwd())


def save_image(image, file_name="", path=os.path):
    # Saves and image to the directory path of
    # the project in a sub folder of Images
    pygame.image.save(image, str(path) + "\\Images\\" + file_name)
    print("Image has saved as: " + file_name)


def crop_image(image, background_colour=(0, 0, 0)):
    """Returns a cropped display surface"""
    # Getting the largest coordinate that it can be to scale down
    smallest_used_coordinate = image.get_size()
    largest_used_coordinate = (0, 0)

    for x in range(0, image.get_size()[0]):
        for y in range(0, image.get_size()[1]):
            pixel_colour = image.get_at((x, y))

            if pixel_colour != background_colour:
                # The X and Y must be separate otherwise they override one another
                if x > largest_used_coordinate[0]:
                    largest_used_coordinate = (x, largest_used_coordinate[1])
                    continue

                elif x < smallest_used_coordinate[0]:
                    smallest_used_coordinate = (x, smallest_used_coordinate[1])
                    continue

                if y > largest_used_coordinate[1]:
                    largest_used_coordinate = (largest_used_coordinate[0], y)
                    continue

                elif y < smallest_used_coordinate[1]:
                    smallest_used_coordinate = (smallest_used_coordinate[0], y)
                    continue

    surface_size = ((largest_used_coordinate[0] - smallest_used_coordinate[0]),
                    (largest_used_coordinate[1] - smallest_used_coordinate[1]))

    cropped_surface = pygame.Surface(surface_size)
    cropped_surface.blit(image, (-smallest_used_coordinate[0], -smallest_used_coordinate[1]))
    return cropped_surface


def get_random_colour():
    """Returns a random colour from the entire colour spectrum"""
    colour = [0, 0, 0]
    for i in range(0, 2):
        colour[i] = random.randint(0, 255)

    return tuple(colour)


def generate_text(font, text, colour, bg_colour, centre_point):
    """Returns the Rect and Surface of a text """
    text_display = font.render(text, True, colour, bg_colour)

    text_rect = text_display.get_rect()
    text_rect.center = centre_point

    return text_display, text_rect


def get_input():
    """Returns a boolean to state if any button has been pressed"""
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
    """
    The highest parent class that has the variables and function
    signatures for the child classes to use and adapt
    """
    def __init__(self, position=(0, 0), colour=(0, 0, 0)):
        """ A constructor for Shape that assigns required parameters """
        self.position = position
        self.colour = colour

    def draw_shape(self):
        """
        A separate function that is being declared, so that it may be used by
        the child classes, but is not being used here since Shape is generic
        """
        pass


class Rectangle(Shape):
    """
    A child class to Shape which stores more variables to
    allow the instantiation of a rectangle like shape
    """
    def __init__(self, position=(0, 0), colour=(0, 0, 0), bounds=pygame.Rect(0, 0, 0, 0)):
        """
        The constructor of the Rectangle which takes in a pygame.Rect() parameter to be
        used when creating a rectangle. It also runs the parent Shape class constructor too
        """
        super(Rectangle, self).__init__(position, colour)

        bounds.center = (position[0], position[1])
        self.bounds = bounds

    def draw_shape(self):
        super(Rectangle, self).draw_shape()
        pygame.draw.rect(image_screen, self.colour, self.bounds)


class Circle(Shape):
    def __init__(self, position=(0, 0), colour=(0, 0, 0), radius=0):
        super(Circle, self).__init__(position, colour)
        self.radius = radius

    def draw_shape(self):
        super(Circle, self).draw_shape()
        pygame.draw.circle(image_screen, self.colour, (int(self.position[0]), int(self.position[1])), self.radius)


class Polygon(Shape):
    # Position is removed since bounds deals with it
    def __init__(self, position=(0, 0), colour=(0, 0, 0), bounds=[]):
        super(Polygon, self).__init__(position, colour)
        self.bounds = bounds

    def draw_shape(self):
        super(Polygon, self).draw_shape()
        pygame.draw.polygon(image_screen, self.colour, self.bounds)


if __name__ == '__main__':
    main()
