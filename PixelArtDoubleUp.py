import os, sys

os.environ["SDL_VIDEODRIVER"] = "dummy"
 
 
import pygame.transform
 
 
if 1:
    #some platforms might need to init the display for some parts of pygame.
    import pygame.display
    pygame.display.init()
    screen = pygame.display.set_mode((1,1))

filename = "" #No dots allowed in filename except for extension

nameonly = filename.split('.')[0]
extension = filename.split('.')[1]

image = pygame.image.load(os.path.join(filename)).convert_alpha()
image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
pygame.image.save(image, nameonly + "2x." + extension)
