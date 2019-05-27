import pygame
from datetime import datetime


BACKGROUNDS = (
    "sprites/bg-day.png",
    "sprites/bg-night.png"
)


class Background():
    def __init__(self, screen):
        hour = datetime.now().hour
        if(hour > 18):
            bg = pygame.image.load(BACKGROUNDS[1])
        else:
            bg = pygame.image.load(BACKGROUNDS[0])
        self.image = pygame.transform.scale(bg, (320, 600))
        screen.blit(self.image, (0, 0))
