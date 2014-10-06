import random
import pygame
from pygame.locals import *
from gamelib.gfxlib import *

TILE_WIDTH = 50
HORIZON = 180

class Room(object):
    
    def __init__(self, c):
        self.tiles = []
        self.col = Color(0, 0, 255)
    def draw(self, srf):
        DrawGradient(srf, self.col, Rect(0,0,800,180), 20)
        pygame.draw.line(srf, self.col, (0, HORIZON) , (800,HORIZON), 1)
         
class Tile(object):
    
    def __init__(self, x, y, c1, c2):
        self.x = x
        self.y = y
        self.outcol = c1
        self.carpetcol = c2
        self.carpet = False

    def draw(self, srf):
        if self.carpet:
            pygame.draw.rect(Surface, c2, Rect(x,y,TILE_WIDTH,TILE_WIDTH), 0)
        else:
            pygame.draw.rect(Surface, c1, Rect(x,y,50,50), 1)
            
        
