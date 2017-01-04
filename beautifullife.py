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


#randomly generate initial noise pattern:
def generaterandom():
    screen.fill(white)
    for x in range(width):
        for y in range(height):
            if random.randint(0,3) == 1:
                pixels[x,y] = black

def generatespecial():
    screen.fill(white)
    pixels[10,10] = black
    pixels[10,11] = black
    pixels[11,10] = black
    pixels[11,11] = black

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
                #print('al')
            if ((y == 0 and all(thiscol[height-1] == black)) #above
            or (y != 0 and all(thiscol[y-1] == black))):
                neighbors = neighbors+1
                #print('a')
            if ((y == 0 and all(nextcol[height-1] == black)) #above right
            or (y != 0 and all(nextcol[y-1] == black))):
                neighbors = neighbors+1
                #print('ar')
            if (all(lastcol[y] == black)): #left
                neighbors = neighbors+1
                #print('l')
            if (all(nextcol[y] == black)): #right
                neighbors = neighbors+1
                #print('r')
            if ((y == height-1 and all(lastcol[0] == black)) #below left
            or (y != height-1 and all(lastcol[y+1] == black))):
                neighbors = neighbors+1
                #print('bl')
            if ((y == height-1 and all(thiscol[0] == black)) #below
            or (y != height-1 and all(thiscol[y+1] == black))):
                neighbors = neighbors+1
                #print('b')
            if ((y == height-1 and all(nextcol[0] == black)) #below right
            or (y != height-1 and all(nextcol[y+1] == black))):
                neighbors = neighbors+1
                #print('br')
            #if neighbors > 0:
                #print(x,y,neighbors)
                #lastcolclear = True
                #for a in range(0,100):
                #    if all(lastcol[a] == black):
                #        lastcolclear = False
                #if lastcolclear == True:
                    #print('lastcolclear')
                #thiscolclear = True
                #for a in range(0,100):
                #    if all(thiscol[a] == black):
                #        thiscolclear = False
                #if thiscolclear == True:
                    #print('thiscolclear')
            #apply the rules to each pixel
            #if does not have 2 or 3 neighbors, die
            if neighbors < 2 or neighbors > 3:
                pixels[x,y] = white
            #if exactly 3 neighbors, come alive
            elif neighbors == 3:
                pixels[x,y] = black
        #copy this and previous col of pixels to reference
        lastcol = thiscol
        thiscol = nextcol
        nextcol = pixels[0]
        if x < width-2:
            nextcol = pixels[x+2]

    pygame.display.flip()
