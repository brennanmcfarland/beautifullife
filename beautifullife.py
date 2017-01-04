import sys
import pygame
import random

pygame.init()
random.seed()

black = 0,0,0

#set image resolution
size = width, height = 1920, 1080

#initialize image
screen = pygame.display.set_mode(size)
pixels = pygame.surfarray.pixels3d(screen)
screen.fill(black)

#randomly generate initial noise pattern:
def generaterandom():
    for x in range(width):
        for y in range(height):
            if random.randint(0,1) == 1:
                pixels[x,y] = 255,255,255

#initialize pattern
generaterandom()

#main loop
while 1:
    for x in range(width):
        #copy this and previous col of pixels to reference
        thisrow = pixels[x]
        lastrow = pixels[height-1]
        if x != 0:
        lastrow = pixels[x-1]

        for y in range(height):
            #apply the rules to each pixel

    pygame.display.flip()
