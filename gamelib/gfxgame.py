import random
import pygame
from pygame.locals import *
                    
def drawMatchstickPersonsmall(surface, pos, colour, leg = 0):
    pygame.draw.circle(surface, (0,0,255), (pos[0]+4, pos[1]+4) , 5, 0)
    pygame.draw.circle(surface, colour, (pos[0]+5, pos[1]+5) , 5, 0)
    pygame.draw.line(surface, colour, (pos[0]+5, pos[1]+10) , (pos[0]+5, pos[1]+20), 1)
    pygame.draw.line(surface, (0,0,255), (pos[0]+4, pos[1]+10) , (pos[0]+4, pos[1]+20), 1)
    
    pygame.draw.line(surface, (0,0,255), (pos[0]-leg, pos[1]+14) , (pos[0]+10+leg, pos[1]+14), 1)
    #pygame.draw.line(surface, colour, (pos[0]-leg, pos[1]+15) , (pos[0]+10+leg, pos[1]+15), 1)
    
    pygame.draw.line(surface, colour, (pos[0]+10 + leg, pos[1]+25) , (pos[0]+5, pos[1]+20), 1)
    pygame.draw.line(surface, colour, (pos[0]  - leg, pos[1]+25) , (pos[0]+5, pos[1]+20), 1)

def drawMatchstickPerson(surface, pos, colour):
    pygame.draw.circle(surface, colour, (pos[0]+10, pos[1]+10) , 10, 1)
    pygame.draw.line(surface, colour, (pos[0]+10, pos[1]+20) , (pos[0]+10, pos[1]+40), 1)
    pygame.draw.line(surface, (0,0,255), (pos[0]+11, pos[1]+20) , (pos[0]+11, pos[1]+40), 1)
    
    pygame.draw.line(surface, colour, (pos[0], pos[1]+25) , (pos[0]+20, pos[1]+25), 1)
    
    pygame.draw.line(surface, colour, (pos[0]+20, pos[1]+50) , (pos[0]+10, pos[1]+40), 1)
    pygame.draw.line(surface, colour, (pos[0], pos[1]+50) , (pos[0]+10, pos[1]+40), 1)

def drawRocket(sfc, pos, colour):
    pygame.draw.polygon(sfc, Color(141, 141, 141), [(pos[0]-5, pos[1]), (pos[0]+15, pos[1]-15), (pos[0]+35, pos[1])])
    pygame.draw.polygon(sfc, Color(235, 235, 155), [(pos[0], pos[1]+60), (pos[0]+15, pos[1]+45), (pos[0]+30, pos[1]+60)])
    pygame.draw.rect(sfc, Color(255, 0, 2), (pos[0], pos[1], 5,50), 0)
    pygame.draw.rect(sfc, Color(205, 0, 2), (pos[0]+5, pos[1], 25,50), 0)
    pygame.draw.rect(sfc, Color(165, 0, 2), (pos[0]+8, pos[1], 2,50), 0)
    pygame.draw.rect(sfc, Color(165, 0, 2), (pos[0]+10, pos[1], 1,50), 0)
    #pygame.draw.rect(sfc, Color(155, 0, 2), (pos[0], pos[1], 30,50), 1)
    #pygame.draw.rect(sfc, (255,255,255), (pos[0], pos[1]-15, 30, 80))
    return Rect(pos[0], pos[1]-15, 30, 80)
 
