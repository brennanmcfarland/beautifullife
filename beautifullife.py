import sys
import pygame
import random

pygame.init()
random.seed()

alive = 0,0,0
neighborsnone = 255,255,255
neighborsone = 200,200,200
neighborstwo = 123,123,123

#set image resolution
size = width, height = 100, 100

#initialize image
screen = pygame.display.set_mode(size)
pixels = pygame.surfarray.pixels3d(screen)

#clear the screen
def clearcells():
    screen.fill(neighborsnone)

#randomly generate initial noise pattern:
def generaterandom():
    for x in range(width):
        for y in range(height):
            if random.randint(0,3) == 1:
                pixels[x,y] = alive

#spawn a glider shape
def spawnglider(x,y):
    pixels[x,y] = alive
    pixels[x,(y-1)%height] = alive
    pixels[(x-1)%width,y] = alive
    pixels[(x-2)%width,y] = alive
    pixels[(x-1)%width,(y-2)%height] = alive


#initialize pattern
clearcells()
spawnglider(10,10)

#main loop
while 1:
    thiscol = pixels[0]
    lastcol = pixels[width-1]
    nextcol = pixels[1]
    for x in range(width):
        for y in range(height):
            #calculate neighbors of each pixel
            neighbors = 0
            if ((y == 0 and all(lastcol[height-1] == alive)) #above left
            or (y != 0 and all(lastcol[y-1] == alive))):
                neighbors = neighbors+1
            if ((y == 0 and all(thiscol[height-1] == alive)) #above
            or (y != 0 and all(thiscol[y-1] == alive))):
                neighbors = neighbors+1
            if ((y == 0 and all(nextcol[height-1] == alive)) #above right
            or (y != 0 and all(nextcol[y-1] == alive))):
                neighbors = neighbors+1
            if (all(lastcol[y] == alive)): #left
                neighbors = neighbors+1
            if (all(nextcol[y] == alive)): #right
                neighbors = neighbors+1
            if ((y == height-1 and all(lastcol[0] == alive)) #below left
            or (y != height-1 and all(lastcol[y+1] == alive))):
                neighbors = neighbors+1
            if ((y == height-1 and all(thiscol[0] == alive)) #below
            or (y != height-1 and all(thiscol[y+1] == alive))):
                neighbors = neighbors+1
            if ((y == height-1 and all(nextcol[0] == alive)) #below right
            or (y != height-1 and all(nextcol[y+1] == alive))):
                neighbors = neighbors+1
            #apply the rules to each pixel
            #if does not have 2 or 3 neighbors, die
            if neighbors == 0:
                pixels[x,y] = neighborsnone
            elif neighbors == 1:
                pixels[x,y] = neighborsone
            elif neighbors > 3:
                pixels[x,y] = neighborstwo
            #if exactly 3 neighbors, come alive
            elif neighbors == 3:
                pixels[x,y] = alive
        #copy this and previous col of pixels to reference
        lastcol = thiscol
        thiscol = nextcol
        nextcol = pixels[0]
        if x < width-2:
            nextcol = pixels[x+2]

    pygame.display.flip()
