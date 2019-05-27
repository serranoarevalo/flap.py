import pygame
from datetime import datetime


def set_background(screen, width, height):
    hour = datetime.now().hour
    if(hour >= 18):
        bg = pygame.image.load("sprites/bg-day.png")
    else:
        bg = pygame.image.load("sprites/bg-night.png")
    image = pygame.transform.scale(bg, (width, height))
    screen.blit(image, (0, 0))
