import pygame
import sys
import os


# finds the pixel at x,y in the image
def get_pixel(x,y,image):
    return image.get_at((x,y))


# finds the pixels in the image that match the unwanted colour
def colour_get(image):
    pixel_matrix = pygame.PixelArray(image)
    # for each pixel in the image
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = get_pixel(x, y, image)
            # check if the pixel is the unwanted colour
            if unwanted_colour == "blue":
                if pixel.b - 50 >= pixel.g + pixel.r:
                    # if it is, change it to the desired colour
                    pixel_matrix[x, y] = colour_change()
            elif unwanted_colour == "green":
                if pixel.g -50 > pixel.b and pixel.g -50 > pixel.r:
                    pixel_matrix[x, y] = colour_change()
            elif unwanted_colour == "red":
                if pixel.r - 50> pixel.b + pixel.g:
                    pixel_matrix[x, y] = colour_change()
            elif unwanted_colour == "yellow":
                if (pixel.r + pixel.g)/2 >= pixel.b + 100:
                    pixel_matrix[x, y] = colour_change()
            else:
                sys.exit("That is not a valid colour to change. ")
    return image


# changes the specified pixel into the desired colour
def colour_change():
    if desired_colour == "blue":
        new_pixel = (0, 0, 200)
    elif desired_colour == "green":
        new_pixel = (0, 200, 0)
    elif desired_colour == "red":
        new_pixel = (200, 0, 0)
    elif desired_colour == "yellow":
        new_pixel = (200, 200, 0)
    else:
        sys.exit("That is not a valid colour to change to.")
    return new_pixel


# loads the image and calls the colour get function
def image_load(filename):
    try:
        new_image = pygame.image.load(filename)
    except:
        sys.exit("That is an incorrect filepath")
    new_image = colour_get(new_image)
    return new_image


# asks the user for the image, the colour to change, and the colour to change it to.
# It then saves the colour changed image in the current directory as "colourChanged.png".
pygame.init()
image_filepath = input("enter image filepath: ")
unwanted_colour = input("Do you want to change Red, Blue, Green, or Yellow? ")
unwanted_colour = unwanted_colour.lower()
desired_colour = input("Do you want to change it to Red, Blue, Green, or Yellow? ")
desired_colour = desired_colour.lower()
pygame.image.save(image_load(image_filepath), os.getcwd() + "\\colourChanged.png")