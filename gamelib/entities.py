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
        self.Hurting = False
        self.Moving = False
        self.Anim = 0
    
    def Move(self, vert, hori):
        self.Moving = False
        if hori!=0:
            self.rect.x += hori
            self.Moving = True
        if vert!=0:
            self.rect.y += vert
            self.Moving = True
        self.Hotspot = Rect(self.rect.x, self.rect.y + 20, 10, 5 )
        self.Anim += 1
        if self.Anim>3:self.Anim=0
                
    def Draw(self, srf):
        #pygame.draw.rect(srf, (155,155,0), self.Hotspot)
        fc = Color(221,221,221)
        if self.Hurting:
            fc = Color(255,0,0)
        if self.Moving == False:
            self.Anim = 0
        drawMatchstickPersonsmall(srf, self.rect.topleft, fc, self.Anim )
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
        pygame.draw.polygon(srf, Color(155, 255, 214), [(534, HORIZON), (555, HORIZON-165), (610, HORIZON)])
        pygame.draw.polygon(srf, Color(225, 209, 212), [(634, HORIZON), (666, HORIZON-99), (696, HORIZON)])
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
        self.Damage = 5
        
    def Draw(self, srf):
        self.c_body = (144,238,144) 
        pygame.draw.rect(srf, self.c_body , self.Hotspot)
        pygame.draw.rect(srf, (255,255,0) , Rect(self.x, self.y, 10, 10 ))
        pygame.draw.rect(srf, (255,255,0) , Rect(self.x + 12, self.y, 10, 10 ))
        pygame.draw.rect(srf, (0,0,0) , (self.x + 3, self.y + 3, 2 ,2))
        pygame.draw.rect(srf, (0,0,0) , (self.x + 12 + 3, self.y + 3, 2 ,2) )
        
        if self.x<66 or self.x>580: self.xdir*=-1
        if self.y<300 or self.y>500: self.ydir*=-1
        self.x += -1 * self.xdir
        self.y += -1 * self.ydir
        self.Hotspot = Rect(self.x, self.y, 30, 20 )
        pygame.draw.rect(srf, (255,255,255) , self.Hotspot, 1)

class Laser(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xdir = -1
        self.ydir = -1
        self.Hotspot = Rect(x, y, 30, 30 )
        self.Damage = 5
        
    def Draw(self, srf):
        self.c_body = (11,238,11) 
        pygame.draw.rect(srf, self.c_body , self.Hotspot)
        #pygame.draw.rect(srf, (255,255,0) , Rect(self.x, self.y, 10, 10 ))
        #pygame.draw.rect(srf, (255,255,0) , Rect(self.x + 12, self.y, 10, 10 ))
        #pygame.draw.rect(srf, (0,0,0) , (self.x + 3, self.y + 3, 2 ,2))
        #pygame.draw.rect(srf, (0,0,0) , (self.x + 12 + 3, self.y + 3, 2 ,2) )
        
        #if self.x<66 or self.x>580: self.xdir*=-1
        #if self.y<300 or self.y>500: self.ydir*=-1
        #self.x += -1 * self.xdir
        #self.y += -1 * self.ydir
        self.Hotspot = Rect(self.x, self.y, 30, 30 )
        pygame.draw.rect(srf, self.c_body , self.Hotspot, 1)
