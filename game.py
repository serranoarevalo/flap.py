import pygame
import sys
from datetime import datetime


BACKGROUNDS = (
    "sprites/bg-day.png",
    "sprites/bg-night.png"
)

BIRDS = (
    (
        "sprites/blue-one.png",
        "sprites/blue-two.png",
        "sprites/blue-three.png"
    ),
    (
        "sprites/red-one.png",
        "sprites/red-two.png",
        "sprites/red-three.png"
    ),
    (
        "sprites/yellow-one.png",
        "sprites/yellow-two.png",
        "sprites/yellow-three.png"
    ),

)


pygame.init()
pygame.display.set_caption("Flap.py Bird")
screen = pygame.display.set_mode((320, 600))
now = datetime.now()
icon = pygame.image.load(BIRDS[2][1])
pygame.display.set_icon(icon)


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if(now.hour > 18):
        bg = pygame.image.load(BACKGROUNDS[1])
    else:
        bg = pygame.image.load(BACKGROUNDS[0])

    bg = pygame.transform.scale(bg, (320, 600))
    screen.blit(bg, (0, 0))

    pygame.display.flip()
