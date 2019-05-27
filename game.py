import pygame
from datetime import datetime


BACKGROUNDS = (
    'sprites/bg-day.png',
    'sprites/bg-night.png'
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
icon = pygame.image.load(BIRDS[2][1])
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((400, 300))
now = datetime.now()


while True:

    pygame.display.flip()
