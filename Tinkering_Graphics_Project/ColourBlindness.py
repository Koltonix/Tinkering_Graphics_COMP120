import pygame
import os

pygame.init()

screen_display = pygame.display.set_mode((800, 600))

VALUE = 0.65

original_name = 'rgb'
picture_filepath = os.path.join('Colour Blind Images', original_name + '.jpg')
original_picture = pygame.image.load(picture_filepath).convert()

picture_width = original_picture.get_width()
picture_height = original_picture.get_height()

less_red_pic = pygame.Surface((picture_width, picture_height))
less_green_pic = pygame.Surface((picture_width, picture_height))
less_blue_pic = pygame.Surface((picture_width, picture_height))

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


less_red_filename = os.path.join('Colour Blind Images', original_name + ' (Less Red) ' + '.png')
pygame.image.save(less_red_pic, less_red_filename)

less_green_filename = os.path.join('Colour Blind Images', original_name + ' (Less Green) ' + '.png')
pygame.image.save(less_green_pic, less_green_filename)

less_blue_filename = os.path.join('Colour Blind Images', original_name + ' (Less Blue) ' + '.png')
pygame.image.save(less_blue_pic, less_blue_filename)
