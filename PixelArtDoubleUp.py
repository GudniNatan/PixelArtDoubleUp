import pygame
import os

pygame.init()
window_size = window_width, window_height = 1280, 720
screen = pygame.display.set_mode(window_size)

filename = "" #No dots allowed in filename except for extension

nameonly = filename.split('.')[0]
extension = filename.split('.')[1]

image = pygame.image.load(os.path.join(filename)).convert_alpha()
image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
pygame.image.save(image, nameonly + "2x." + extension)