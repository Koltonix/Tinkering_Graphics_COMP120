import pygame


# Returns the position of a pixel in a surface
def get_pixel(x,y,surface):
    return surface.get_at((x,y))


# Changes the colour of each pixel to be more red/green/blue as indicated by the user
def colour_change(surface):
    pixel_matrix = pygame.PixelArray(surface)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            value = get_Pixel(x, y, surface)
            if desired_colour == "Blue":
                pixel_matrix[x, y] = (value.b, value.g * 0.5, value.r * 0.5)
            elif desired_colour == "Green":
                pixel_matrix[x, y] = (value.b * 0.5, value.g, value.r*0.5)
            elif desired_colour == "Red":
                pixel_matrix[x, y] = (value.b * 0.5, value.g * 0.5, value.r)
    return surface


# Loads an image from a filepath and call colour_change
def image_load(filename,surface):
    newimage = pygame.image.load(filename)
    newimage = colour_change(newimage)
    surface.blit(newimage,(0,0))


# the main body of code
pygame.init()
image_filepath = input("enter image filepath: ")
desired_colour = input("Red, Blue or Green? ")
main_window = pygame.display.set_mode((750,750))
running = True
surface1 = pygame.Surface((750, 750))
main_window.blit(surface1,(0,0))
image_load(image_filepath,surface1)

