import sys
import pygame
import random

pygame.init()
random.seed()

black = 0,0,0
white = 255,255,255

#set image resolution
size = width, height = 100, 100

#initialize image
screen = pygame.display.set_mode(size)
pixels = pygame.surfarray.pixels3d(screen)
screen.fill(black)

#randomly generate initial noise pattern:
def generaterandom():
    for x in range(width):
        for y in range(height):
            if random.randint(0,1) == 1:
                pixels[x,y] = white

#initialize pattern
generaterandom()

#main loop
while 1:
    thiscol = pixels[0]
    lastcol = pixels[width-1]
    nextcol = pixels[1]
    for x in range(width):


        for y in range(height):
            #calculate neighbors of each pixel
            neighbors = 0
            if ((y == 0 and all(lastcol[height-1] == black)) #above left
            or (y != 0 and all(lastcol[y-1] == black))):
                neighbors = neighbors+1
            if ((y == 0 and all(thiscol[height-1] == black)) #above
            or (y != 0 and all(thiscol[y-1] == black))):
                neighbors = neighbors+1
            if ((y == 0 and all(nextcol[height-1] == black)) #above right
            or (y != 0 and all(nextcol[y-1] == black))):
                neighbors = neighbors+1
            if (all(lastcol[y] == black)): #left
                neighbors = neighbors+1
            if (all(nextcol[y] == black)): #right
                neighbors = neighbors+1
            if ((y == height-1 and all(lastcol[0] == black)) #below left
            or (y != height-1 and all(lastcol[y+1] == black))):
                neighbors = neighbors+1
            if ((y == height-1 and all(thiscol[0] == black)) #below
            or (y != height-1 and all(thiscol[y+1] == black))):
                neighbors = neighbors+1
            if ((y == height-1 and all(nextcol[0] == black)) #below right
            or (y != height-1 and all(nextcol[y+1] == black))):
                neighbors = neighbors+1
            print(neighbors)
            #apply the rules to each pixel
            #if does not have 2 or 3 neighbors, die
            if neighbors < 2 or neighbors > 3:
                pixels[x,y] = white
            #if exactly 3 neighbors, come alive
            elif neighbors == 3:
                pixels[x,y] = black
        #copy this and previous col of pixels to reference
        thiscol = nextcol
        lastcol = thiscol
        nextcol = pixels[0]
        if x < width-2:
            nextcol = pixels[x+2]

    pygame.display.flip()
