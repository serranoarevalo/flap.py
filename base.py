import pygame


def make_platform(screen, width, height, base_x):

    base_image = pygame.image.load("sprites/base.png")
    base_y = height - base_image.get_height()

    screen.blit(base_image, (base_x, base_y))
    screen.blit(base_image, (base_x + base_image.get_width(), base_y))
