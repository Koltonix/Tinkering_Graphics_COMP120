import pygame
import os
import sys

author = "Thomas O'Leary"
copyright_license = "MIT License Copyright (c) 2019"

"""
This program is designed to take an image,
and display it as if the user was colour blind.

After the image is processed within the program,
the newly adjusted images are saved into and can be viewed within the "Colour Blind Images"
"""

# Initialising Pygame
pygame.init()


# Basic setup for constants
VALUE = 0.65

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT_COLOUR = BLACK
BASIC_FONT_SIZE = 15


# Basic setup for the screen display
screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

"""
This block of code is how the source image is taken from
the "Colour Blind Images" folder.

The users are able to easily change which picture is processed in the program
just by simply changing the original_name string value.

picture_filepath simply locates the image that will be processed.
And the image is loaded onto the original_picture variable.
"""

original_name = 'image'
picture_filepath = os.path.join('Colour Blind Images', original_name + '.jpg')
original_picture = pygame.image.load(picture_filepath).convert()


# Variables defining the Width & Height of the original picture
picture_width = original_picture.get_width()
picture_height = original_picture.get_height()

# There variables create 3 different surfaces
# All having the same width & height as the original picture
less_red_pic = pygame.Surface((picture_width, picture_height))
less_green_pic = pygame.Surface((picture_width, picture_height))
less_blue_pic = pygame.Surface((picture_width, picture_height))


def main():
    """
    This main loop allows the program to process
    the image 3 different times.

    Each loop it grabs every pixel,
    and changes the RGB value.
    """

    running = True

    while running:
        screen_display.fill(WHITE)

        for x in range(picture_width):
            for y in range(picture_height):
                for n in range(3):
                    pixel = original_picture.get_at((x, y))
                    if n <= 0:
                        less_red_pic.set_at(
                            (x, y),
                            pygame.Color(int(pixel.r * VALUE), pixel.g, pixel.b))
                        n = n + 1
                    elif n <= 1:
                        less_green_pic.set_at(
                            (x, y),
                            pygame.Color(pixel.r, int(pixel.g * VALUE), pixel.b))
                        n = n + 1
                    else:
                        less_blue_pic.set_at(
                            (x, y),
                            pygame.Color(pixel.r, pixel.g, int(pixel.b * VALUE)))

        saving_image()
        display_image()
        display_text()
        pygame.display.update()
        check_for_quit()


def saving_image():
    """
    This function simply takes all new processed images
    and saves them as separate file names to the
    "Colour Blind Images" folder.
    """
    less_red_filename = os.path.join('Colour Blind Images', original_name + ' (Less Red) ' + '.png')
    pygame.image.save(less_red_pic, less_red_filename)

    less_green_filename = os.path.join('Colour Blind Images', original_name + ' (Less Green) ' + '.png')
    pygame.image.save(less_green_pic, less_green_filename)

    less_blue_filename = os.path.join('Colour Blind Images', original_name + ' (Less Blue) ' + '.png')
    pygame.image.save(less_blue_pic, less_blue_filename)


def display_image():
    """Function that allows the newly processed images to be displayed onto the surface"""
    half_red_pic = pygame.transform.scale(less_red_pic, (int(picture_width / 2), int(picture_height / 2)))
    half_green_pic = pygame.transform.scale(less_green_pic, (int(picture_width / 2), int(picture_height / 2)))
    half_blue_pic = pygame.transform.scale(less_blue_pic, (int(picture_width / 2), int(picture_height / 2)))

    screen_display.blit(half_red_pic, (0, 0))
    screen_display.blit(half_green_pic, (400, 0))
    screen_display.blit(half_blue_pic, (0, 300))


def display_text():
    """Displays text explaining what each image is"""
    basic_font = pygame.font.Font("freesansbold.ttf", BASIC_FONT_SIZE)
    text_red_image = basic_font.render('Eyesight with reduced Red sensitivity ', True, BLACK, WHITE)
    text_green_image = basic_font.render('Eyesight with reduced Green sensitivity ', True, BLACK, WHITE)
    text_blue_image = basic_font.render('Eyesight with reduced Blue sensitivity ', True, BLACK, WHITE)

    red_text_rect = text_red_image.get_rect()
    red_text_rect.topleft = (0, 200)

    green_text_rect = text_green_image.get_rect()
    green_text_rect.topleft = (400, 200)

    blue_text_rect = text_blue_image.get_rect()
    blue_text_rect.topleft = (0, 500)

    screen_display.blit(text_red_image, red_text_rect)
    screen_display.blit(text_green_image, green_text_rect)
    screen_display.blit(text_blue_image, blue_text_rect)


def check_for_quit():
    """Checks for quit, then runs the terminate() function"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        pygame.event.post(event)


def terminate():
    """Terminates the Script"""
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
