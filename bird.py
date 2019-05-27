import pygame


def draw_bird(screen, count, rotation):

    down, middle, up = pygame.image.load("sprites/bird-one.png"), pygame.image.load(
        "sprites/bird-two.png"), pygame.image.load("sprites/bird-three.png")

    if count < 10:
        image = down
    elif count < 20 or count >= 30:
        image = middle
    elif count < 30:
        image = up

    image = pygame.transform.rotate(image, rotation)
    screen.blit(image, (70, 150))
