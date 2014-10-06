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
        self.soundb= pygame.mixer.Sound("snd/tileup.wav")
        
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
        self.Beasties = []
        
        self.TilesDone = 0
        for j in range(10):
            for i in range(10):
                t = Tile( 320 + TILE_WIDTH*i, 240 + TILE_WIDTH*j, (55,0,0), (170+(i*3 + j*4),20+(i*8+j*8),0))
                self.TheTiles.append(t)
        
        self.Beasties.append(Beastie(300 + RND(100), 310))
        self.Beasties.append(Beastie(400 + RND(100), 390))
        self.Beasties.append(Beastie(500 + RND(100), 430))
        
    def CheckTiles(self):
        
        if self.TheRoom.RocketRect.colliderect(self.p1.Hotspot):
            self.p1.Tiles = 30
            if not self.InRocket:
                self.soundb.play()
            self.InRocket = True
        else:
            self.InRocket = False
            
        if self.p1.Tiles==0: return
            
        for t in self.TheTiles:
            if t.carpet == False and t.Hotspot.colliderect(self.p1.Hotspot):
                t.carpet = True
                self.sounda.play()
                self.TilesDone+=1
                self.p1.Tiles -= 1

    def DrawRoom(self):
        self.Surface.fill(pygame.Color("black"))
        
        #gfx
        self.Surface.lock()
        
        self.TheRoom.Draw(self.Surface)
        for t in self.TheTiles:
            t.Draw(self.Surface)
        for b in self.Beasties:
            b.Draw(self.Surface)
        self.StatusBar.Draw(self.Surface)
        
        self.p1.Draw(self.Surface)
        self.Surface.unlock()
        
        #Txt
        DrawText(self.Surface, 120, 570, "Progress : " + str(self.TilesDone) + " / " + str(len(self.TheTiles)), 24, (240,240,240) )
        DrawText(self.Surface, 20, 570, "Level : " + str(self.p1.Level), 24, (240,240,240) )
        DrawText(self.Surface, 320, 570, "Tiles : " + str(self.p1.Tiles), 24, (240,240,0) )
        if self.p1.Tiles==0:
            pygame.draw.rect(self.Surface, (255,255,255), (395,567,75,20))
            DrawText(self.Surface, 399, 570, "RELOAD", 24, (240,0,0) )
        DrawText(self.Surface, 520, 570, "Score : " + str(self.p1.Score), 24, (240,240,240) )
        DrawText(self.Surface, 620, 570, "Health : " + str(self.p1.Health), 24, (240,240,240) )
        
        #Flip
        self.Screen.blit(self.Surface, (0, 0))
        pygame.display.flip()
        
