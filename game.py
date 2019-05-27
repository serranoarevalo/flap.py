import pygame
import sys
from background import Background

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
icon = pygame.image.load(BIRDS[2][1])
pygame.display.set_icon(icon)


while 1:

    Background(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
