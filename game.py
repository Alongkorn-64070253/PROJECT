import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("ALCOHOL MAN")
icon = pygame.image.load("beer.png")
pygame.display.set_icon(icon)
title_bg = pygame.image.load("bg.png")
player = pygame.image.load("player.png")

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            quit()
    screen.blit(title_bg,(0,0))
    screen.blit(player,(0,0))
    pygame.display.update()
