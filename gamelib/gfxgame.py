import random
import pygame
from pygame.locals import *
                    
def drawMatchstickPersonsmall(surface, pos, colour):
    pygame.draw.circle(surface, colour, (pos[0]+5, pos[1]+5) , 5, 0)
    pygame.draw.line(surface, colour, (pos[0]+5, pos[1]+10) , (pos[0]+5, pos[1]+20), 1)
    
    pygame.draw.line(surface, colour, (pos[0], pos[1]+15) , (pos[0]+10, pos[1]+15), 1)
    
    pygame.draw.line(surface, colour, (pos[0]+10, pos[1]+25) , (pos[0]+5, pos[1]+20), 1)
    pygame.draw.line(surface, colour, (pos[0], pos[1]+25) , (pos[0]+5, pos[1]+20), 1)

def drawMatchstickPerson(surface, pos, colour):
    pygame.draw.circle(surface, colour, (pos[0]+10, pos[1]+10) , 10, 1)
    pygame.draw.line(surface, colour, (pos[0]+10, pos[1]+20) , (pos[0]+10, pos[1]+40), 1)
    
    pygame.draw.line(surface, colour, (pos[0], pos[1]+25) , (pos[0]+20, pos[1]+25), 1)
    
    pygame.draw.line(surface, colour, (pos[0]+20, pos[1]+50) , (pos[0]+10, pos[1]+40), 1)
    pygame.draw.line(surface, colour, (pos[0], pos[1]+50) , (pos[0]+10, pos[1]+40), 1)
