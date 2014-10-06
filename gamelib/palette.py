import pygame
import sys
from pygame.locals import *
from gfxlib import *
from gfxgame import *
Dude = [ Color(0,0,55), Color(50,0,145), Color(0,0,255) ]
Background = [ Color(11,65,60), Color(17,155,80), Color(139,207,136)]

ColourChart = [Dude, Background]

if __name__=="__main__":
    WINSIZE = 640,680
    
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption("Colour Palette for PyWeek19")
    pygame.init()

    y = 0
    w = 50
    
    for r in ColourChart:
        x = 0
        y += w
        for c in r:
            x += w
            pygame.draw.rect(screen, c, Rect(x, y, w, w ), 0)
    
    DrawGradient(screen, Color(0, 0, 255), Rect(0,0,640,480), 20)
    drawMatchstickPerson(screen, (100, 200), Color(0,255,0))
    cb = copperBar()
    cb.Draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
