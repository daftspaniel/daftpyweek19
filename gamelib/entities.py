import random
import pygame
from pygame.locals import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *

TILE_WIDTH = 20
HORIZON = 180

class Player(object):
    def __init__(self, pos):
        self.Level = 1
        self.Score = 0
        self.Health = 100
        self.rect = Rect(pos[0], pos[1], 10, 25 )
        self.Hotspot = Rect(pos[0], pos[1] + 20, 10, 5 )
        self.Tiles = 30
        self.InRocket = False
    
    def Move(self, vert, hori):
        if hori!=0:
            self.rect.x += hori
        if vert!=0:
            self.rect.y += vert
        self.Hotspot = Rect(self.rect.x, self.rect.y + 20, 10, 5 )
    def Draw(self, srf):
        #pygame.draw.rect(srf, (155,155,0), self.Hotspot)
        drawMatchstickPersonsmall(srf, self.rect.topleft, Color(221,221,221))
        #drawMatchstickPersonsmall(srf, (self.rect.topleft[0]-1, self.rect.topleft[1]), Color(0,255,0))
        
class Room(object):
    
    def __init__(self, c):
        self.tiles = []
        self.col = Color(0, 0, 255)
        self.RocketRect = Rect(0,0,10,10)
    def Draw(self, srf):
        DrawGradient(srf, self.col, Rect(0,0,800,180), 8)
        pygame.draw.line(srf, self.col, (0, HORIZON) , (800,HORIZON), 1)
        self.RocketRect = drawRocket(srf, (20,300), None)
        pygame.draw.polygon(srf, Color(140, 0, 255), [(134, HORIZON), (215, HORIZON-45), (530, HORIZON)])
#TILE_WIDTH = 20

class Tile(object):
    
    def __init__(self, x, y, c1, c2):
        self.x = x
        self.y = y
        self.outcol = c1
        self.carpetcol = c2
        self.carpet = False
        self.Hotspot = Rect(x + 5, y +5, 10, 10 )
    
    def Draw(self, srf):
        pygame.draw.rect(srf, (115,115,125), self.Hotspot)
        if self.carpet:
            pygame.draw.rect(srf, self.carpetcol, Rect(self.x,self.y,TILE_WIDTH,TILE_WIDTH), 0)
        
        pygame.draw.rect(srf, self.outcol, Rect(self.x,self.y,TILE_WIDTH,TILE_WIDTH), 1)

class Beastie(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xdir = -1
        self.ydir = -1
        self.Hotspot = Rect(x, y, 30, 20 )
    def Draw(self, srf):
        pygame.draw.rect(srf, (144,238,144) , self.Hotspot)
        if self.x<66 or self.x>580: self.xdir*=-1
        if self.y<300 or self.y>500: self.ydir*=-1
        self.x += -1 * self.xdir
        self.y += -1 * self.ydir
        self.Hotspot = Rect(self.x, self.y, 30, 20 )
