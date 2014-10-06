import random
import pygame
from pygame.locals import *

def DrawGradient(Surface, gradColor, area, step = 10):
    src = Rect(area.x, area.y, area.w, int(area.h/step) )
    
    for i in range(step):
       trg = Rect(src.x, src.y + (src.h*i), src.w, src.h  )
       bbb = gradColor.b-(i*step)
       if bbb<0:bbb=0
       pygame.draw.rect(Surface, Color(gradColor.r,gradColor.g,bbb), trg, 0)

class copperBar(object):
    
    def __init__(self, rgb = (0,0,1), y=300 ):
        self.barcolor = []
        for i in range(1, 63):
            self.barcolor.append((i*4, i*4, i*4))
        for i in range(1, 63):
            self.barcolor.append((255 - i*4, 255 - i*4, 255 - i*4))
        self.barheight = 123
        self.y = y
        self.direct = 1
        bcm = []
        for c in self.barcolor:
            bcm.append( (int(c[0] * rgb[0]), int(c[1] * rgb[1]), int(c[2] * rgb[2])) )
        self.barcolor = bcm
        
    def Draw(self, srf):
        #
        self.y += 2*self.direct
        if self.y>568 or self.y<32:
            self.direct *= -1
        for i in range(0, self.barheight):
            pygame.draw.line(srf, self.barcolor[i], (0, self.y+i), (799, self.y+i))
