import sys
import os
import pygame
import random

""" 
This program is intended to allow the user to draw them own simple images 
using two simple primitives of squares and circles. 

They are able to scale, move and change the colour of them using.

Once done they are able to export the image which is then cropped using the
background colour.  
"""

__author___ = "Christopher Philip Robertson"
__copyright___ = "MIT License Copyright (c) 2019"

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

MOVE_SPEED = 5
SCALE_SPEED = 5

is_colour_button_selected = False
main_screen = pygame.Surface
image_screen = pygame.Surface
selected_colour = (0, 0, 255)


def main():
    """
    The primary function which includes the
    initialisation and game loop of the tool itself.
    """
    global main_screen, image_screen, shapes_to_render, is_colour_button_selected
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
        image_screen.fill(BACKGROUND_COLOUR)
        check_for_quit()

        draw_shapes(shapes_to_render)
        draw_buttons(buttons_to_render)

        if get_input():
            cropped_surface = crop_image(image_screen, BACKGROUND_COLOUR)
            save_image(cropped_surface, "saved_image.png", os.getcwd())

        move_current_shape(shapes_to_render)
        check_button_press(buttons_to_render)

        FPS_CLOCK.tick(FPS)
        pygame.display.update()


def set_shapes():
    """Creates the default shapes to appear on the screen at the start"""
    centre_body = Circle(SCREEN_CENTRE, BLUE, 50)
    shapes_to_render.append(centre_body)

    square_head = Rectangle((SCREEN_CENTRE[0], SCREEN_CENTRE[1] - 50), WHITE, pygame.Rect(0, 0, 50, 50))
    shapes_to_render.append(square_head)


def set_buttons(font):
    """Creates the buttons and adds them to a list which renders them onto the surface"""
    save_button = generate_text(font, "Save Image", FONT_COLOUR, BUTTON_COLOUR, (75, 100))
    buttons_to_render.append((save_button[0], save_button[1], "SAVE"))

    delete_button = generate_text(font, "Delete", FONT_COLOUR, BUTTON_COLOUR, (75, 125))
    buttons_to_render.append((delete_button[0], delete_button[1], "DELETE"))

    circle_button = generate_text(font, "Circle", FONT_COLOUR, BUTTON_COLOUR, (75, 175))
    buttons_to_render.append((circle_button[0], circle_button[1], "CIRCLE"))

    square_button = generate_text(font, "Square", FONT_COLOUR, BUTTON_COLOUR, (75, 200))
    buttons_to_render.append((square_button[0], square_button[1], "SQUARE"))

    increase_size = generate_text(font, "Increase", FONT_COLOUR, BUTTON_COLOUR, (75, 250))
    buttons_to_render.append((increase_size[0], increase_size[1], "INCREASE"))

    decrease_size = generate_text(font, "Decrease", FONT_COLOUR, BUTTON_COLOUR, (75, 275))
    buttons_to_render.append((decrease_size[0], decrease_size[1], "DECREASE"))

    r_colour_button = generate_text(font, " " + str(selected_colour[0]) + " ", FONT_COLOUR, BUTTON_COLOUR, (565, 100))
    buttons_to_render.append((r_colour_button[0], r_colour_button[1], "RED"))

    g_colour_button = generate_text(font, " " + str(selected_colour[1]) + " ", FONT_COLOUR, BUTTON_COLOUR, (565, 125))
    buttons_to_render.append((g_colour_button[0], g_colour_button[1], "GREEN"))

    b_colour_button = generate_text(font, " " + str(selected_colour[2]) + " ", FONT_COLOUR, BUTTON_COLOUR, (565, 150))
    buttons_to_render.append((b_colour_button[0], b_colour_button[1], "BLUE"))


def draw_shapes(shapes):
    """Renders the shapes to a separate display surface and then blits them to the main screen too"""
    for i in range(0, len(shapes)):
        shapes[i].draw_shape()
        main_screen.blit(image_screen, (0, 0))


def draw_buttons(buttons=[]):
    """Renders the buttons to the main display surface"""
    for i in range(0, len(buttons)):
        main_screen.blit(buttons[i][0], buttons[i][1])


def save_image(image, file_name="", path=os.path):
    """Saves the image to the directory path of the project in a sub folder of Images"""
    pygame.image.save(image, str(path) + "\\Images\\" + file_name)
    print("Image has saved as: " + file_name)


def crop_image(image, background_colour=(0, 0, 0)):
    """Returns a cropped display surface"""
    # Getting the largest coordinate that it can be to scale down
    smallest_used_coordinate = image.get_size()
    largest_used_coordinate = (0, 0)

    # Loops through the image surface and crops
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

    # Giving the cropped surface the lowest position point of the image and the highest
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
    """
    Returns the Rect and Surface of a text
    Source: http://inventwithpython.com/makinggames.pdf
    """
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


def check_button_press(buttons=[]):
    """Checks for an onscreen button press which invokes an event"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(0, len(buttons)):
                if buttons[i][1].collidepoint(pygame.mouse.get_pos()):
                    trigger_button_events(buttons[i][2])
                    continue

                elif i == len(buttons) - 1:
                    global is_colour_button_selected
                    is_colour_button_selected = False


def move_current_shape(shapes=[]):
    """Moves the last object in the array depending on the player input of WASD"""
    if len(shapes) > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Moving Up
                if event.key == pygame.K_w:
                    shape_pos = shapes[len(shapes) - 1].position
                    shapes[len(shapes) - 1].position = shape_pos[0], shape_pos[1] - MOVE_SPEED

                # Moving Down
                elif event.key == pygame.K_s:
                    shape_pos = shapes[len(shapes) - 1].position
                    shapes[len(shapes) - 1].position = shape_pos[0], shape_pos[1] + MOVE_SPEED

                # Moving Left
                elif event.key == pygame.K_a:
                    shape_pos = shapes[len(shapes) - 1].position
                    shapes[len(shapes) - 1].position = shape_pos[0] - MOVE_SPEED, shape_pos[1]

                # Moving Right
                elif event.key == pygame.K_d:
                    shape_pos = shapes[len(shapes) - 1].position
                    shapes[len(shapes) - 1].position = shape_pos[0] + MOVE_SPEED, shape_pos[1]

            pygame.event.post(event)


def trigger_button_events(event=""):
    """Invokes the functions depending on the event type"""
    if event == "SAVE":
        cropped_surface = crop_image(image_screen, BACKGROUND_COLOUR)
        save_image(cropped_surface, "saved_image.png", os.getcwd())

    if event == "DELETE":
        if len(shapes_to_render) > 0:
            shape_to_delete = shapes_to_render[len(shapes_to_render) - 1]
            shapes_to_render.remove(shape_to_delete)

    elif event == "CIRCLE":
        circle = Circle(SCREEN_CENTRE, selected_colour, 30)
        shapes_to_render.append(circle)

    elif event == "SQUARE":
        square = Rectangle(SCREEN_CENTRE, selected_colour, pygame.Rect(0, 0, 50, 50))
        shapes_to_render.append(square)

    elif event == "INCREASE":
        shapes_to_render[len(shapes_to_render) - 1].set_size(SCALE_SPEED)

    elif event == "DECREASE":
        shapes_to_render[len(shapes_to_render) - 1].set_size(-SCALE_SPEED)

    elif event == "RED" or event == "GREEN" or event == "BLUE":
        global is_colour_button_selected
        is_colour_button_selected = True


def check_for_quit():
    """
    A simple loop to check when the quit event has passed
    Source: http://inventwithpython.com/makinggames.pdf
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate_program()
        pygame.event.post(event)


def terminate_program():
    """Closes the program in pygame and the system"""
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

    def set_size(self, size=0):
        """
        A separate function that is being declared so that the child classes
        may use it in their own individual way, but with the same result
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

        bounds.center = position
        self.bounds = bounds

    def draw_shape(self):
        """The overridden function of Shape.draw_shape which uses the position and bounds to draw"""
        super(Rectangle, self).draw_shape()
        self.bounds.center = self.position
        pygame.draw.rect(image_screen, self.colour, self.bounds)

    def set_size(self, size=0):
        """The overridden function of Shape.set_size which uses bounds to set its size"""
        super(Rectangle, self).set_size(size)
        self.bounds = pygame.Rect(self.bounds[0], self.bounds[1], self.bounds[2] + size, self.bounds[3] + size)


class Circle(Shape):
    """A child class to Shape which stores a radius to be drawn"""
    def __init__(self, position=(0, 0), colour=(0, 0, 0), radius=0):
        super(Circle, self).__init__(position, colour)
        self.radius = radius

    def draw_shape(self):
        """The overridden function of Shape.draw_shape which uses the radius and position to draw"""
        super(Circle, self).draw_shape()
        pygame.draw.circle(image_screen, self.colour, (int(self.position[0]), int(self.position[1])), self.radius)

    def set_size(self, size=0):
        """The overridden function of Shape.set_Size which just affects its radius to set its size"""
        super(Circle, self).set_size(size)
        self.radius += size


class Polygon(Shape):
    """Child class of Shape which stores a list of positions bounds to be drawn"""
    def __init__(self, position=(0, 0), colour=(0, 0, 0), bounds=[]):
        """Constructor of the Polygon class which takes in an additional bounds list of positions"""
        super(Polygon, self).__init__(position, colour)
        self.bounds = bounds

    def draw_shape(self):
        """The overridden function of Shape.draw_shape which uses the position bounds list to draw itself"""
        super(Polygon, self).draw_shape()
        pygame.draw.polygon(image_screen, self.colour, self.bounds)


if __name__ == '__main__':
    main()
