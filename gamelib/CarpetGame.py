import sys
import pygame
from pygame.locals import *

from gamelib.entities import *
from gamelib.util import *
from gamelib.gfxlib import *


class CarpetGame(object):
    
    def __init__(self, Surface, Screen, ScreenSize):
        self.Screen = Screen
        self.Surface = Surface
        self.ScreenSize = ScreenSize
        
    def MainLoop(self):
        
        self.DrawRoom()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_ESCAPE]==1:
                        return
                    elif keystate[K_w]==1:
                        pass
                    elif keystate[K_s]==1:
                        pass
                    elif keystate[K_a]==1:
                        pass
                    elif keystate[K_d]==1:
                        pass
                elif event.type == ANIMEVENT:
                    self.DrawRoom()
        
    def DrawRoom(self):
        r = Room( (0,255,0) )
        r.draw(self.Surface)
        self.Screen.blit(self.Surface, (0, 0))
        pygame.display.flip()
        
