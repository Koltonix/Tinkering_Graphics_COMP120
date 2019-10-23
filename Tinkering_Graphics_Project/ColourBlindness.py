# Contract #5 by Thomas O'Leary
# TO231922

import pygame
import os

"""
This program is designed to take an image,
and display it as if the user was colour blind.

After the image is processed within the program,
the newly adjusted images are saved into and can be viewed within the "Colour Blind Images"
"""

# Initialising Pygame
pygame.init()

# Basic setup for the screen display
screen_display = pygame.display.set_mode((800, 600))

# This constant is created so that Users are able to adjust how much
# the colours change value
VALUE = 0.65

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


if __name__ == "__main__":
    main()
