import pygame
import sys
from background import set_background
from base import make_platform
from bird import draw_bird

WIDTH, HEIGHT = 320, 600

pygame.init()
pygame.display.set_caption("Flap.py Bird")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_x = 0
bird_flap = 0
bird_rotation = 0
bird_y = 150
going_up = False
up_counter = 0

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    set_background(screen, WIDTH, HEIGHT)

    make_platform(screen, WIDTH, HEIGHT, base_x)

    base_x = base_x - 1

    if base_x == -336:
        base_x = 0

    draw_bird(screen, bird_flap, bird_rotation, bird_y)

    bird_flap = bird_flap + 1

    if bird_flap >= 40:
        bird_flap = 0

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE] and not going_up:
        going_up = True

    if going_up is True and not pressed[pygame.K_SPACE]:

        bird_rotation = 20

        bird_y = bird_y - 6

        if up_counter < 10:
            up_counter = up_counter + 1
        else:
            up_counter = 0
            going_up = False

    else:

        bird_y = bird_y + 4

        if bird_rotation > -15:
            bird_rotation = bird_rotation - 2.5

    pygame.display.flip()
