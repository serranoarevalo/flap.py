import pygame
import sys
from background import set_background
from base import make_platform

WIDTH, HEIGHT = 320, 600

pygame.init()
pygame.display.set_caption("Flap.py Bird")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_x = 0

while 1:

    set_background(screen, WIDTH, HEIGHT)

    make_platform(screen, WIDTH, HEIGHT, base_x)

    base_x = base_x - 1

    if(base_x == -336):
        base_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
