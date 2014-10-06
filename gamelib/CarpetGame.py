import sys
import pygame
from pygame.locals import *

from gamelib.entities import *
from gamelib.util import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *


class CarpetGame(object):
    
    def __init__(self, Surface, Screen, ScreenSize):
        self.Screen = Screen
        self.Surface = Surface
        self.ScreenSize = ScreenSize
        self.StatusBar = copperBar( (0,1,0), 540 )
        self.StatusBar.direct = 0
        self.sounda= pygame.mixer.Sound("snd/laytile.wav")
        
    def MainLoop(self):
        
        self.p1 = Player( (210,300) )
        self.CreateRoom(1)
        self.DrawRoom()
        pygame.key.set_repeat(1, 10)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_ESCAPE]==1:
                        return
                    if keystate[K_w]==1:
                        self.p1.Move(-1,0)
                    elif keystate[K_s]==1:
                        self.p1.Move(1,0)
                    if keystate[K_a]==1:
                        self.p1.Move(0,-1)
                    elif keystate[K_d]==1:
                        self.p1.Move(0,1)
                elif event.type == ANIMEVENT:
                    self.DrawRoom()
                    self.CheckTiles()
                    
    def CreateRoom(self, level):
        self.TheRoom = Room( (0,255,0) )
        
        self.TheTiles = []
        
        for j in range(10):
            for i in range(10):
                t = Tile( 320 + TILE_WIDTH*i, 240 + TILE_WIDTH*j, (85,0,0), (20+(i*j*2),20+(i*3+j*2),64))
                self.TheTiles.append(t)
    
    def CheckTiles(self):
        for t in self.TheTiles:
            if t.carpet == False and t.Hotspot.colliderect(self.p1.Hotspot):
                t.carpet = True
                self.sounda.play()

    def DrawRoom(self):
        self.Surface.fill(pygame.Color("black"))
        
        #gfx
        self.Surface.lock()
        
        self.TheRoom.Draw(self.Surface)
        for t in self.TheTiles:
            t.Draw(self.Surface)
        self.StatusBar.Draw(self.Surface)
        self.p1.Draw(self.Surface)
        self.Surface.unlock()
        #Txt
        #Flip
        self.Screen.blit(self.Surface, (0, 0))
        pygame.display.flip()
        
