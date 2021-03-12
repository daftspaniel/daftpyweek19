import sys
import pygame
from pygame.locals import *

from gamelib.entities import *
from gamelib.util import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *
from gamelib.levelmaker import LevelMaker


class CarpetGame(object):

    def __init__(self, Surface, Screen, ScreenSize, Ajoystick, sndmanager):
        self.Screen = Screen
        self.Surface = Surface
        self.ScreenSize = ScreenSize
        self.Gamepad = Ajoystick
        self.StatusBar = copperBar((0, 1, 0), 540)
        self.StatusBar.direct = 0
        self.SND = sndmanager
        self.LM = LevelMaker()
        self.StartPos = (110, 300)
        self.Pause = False

    def MainLoop(self):

        self.p1 = Player(self.StartPos)
        self.p1.Level = 1
        self.CreateRoom(self.p1.Level)
        self.DrawRoom()
        pygame.key.set_repeat(1, 10)

        while self.p1.Health > 0:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_ESCAPE] == 1:
                        return

                    if self.Pause:
                        if keystate[K_o] == 1:
                            self.Pause = False
                    else:
                        if keystate[K_w] == 1:
                            self.p1.Move(-1, 0)
                        elif keystate[K_s] == 1:
                            self.p1.Move(1, 0)
                        if keystate[K_a] == 1:
                            self.p1.Move(0, -1)
                        elif keystate[K_d] == 1:
                            self.p1.Move(0, 1)
                        elif keystate[K_p] == 1:
                            self.Pause = True
                            print("Pause")
                        elif keystate[K_i] == 1:
                            self.p1.Health = 999
                            print("CHEAT!")

                elif event.type == ANIMEVENT:

                    self.DrawRoom()

                elif event.type == LOGICEVENT:

                    if not self.Pause:
                        self.CheckTiles()
                        for l in self.Lasers:
                            l.Move()

                        # #Gamepad
                        # h_axis = self.Gamepad.get_axis(0)
                        # v_axis = self.Gamepad.get_axis(1)
                        # a_button = self.Gamepad.get_button(0)

                        # if h_axis<0:
                        #     self.p1.Move(0,-2)
                        # elif h_axis>0:
                        #     self.p1.Move(0,2)
                        # if v_axis<0:
                        #     self.p1.Move(-2,0)
                        # elif v_axis>0:
                        #     self.p1.Move(2,0)

                        # Beaties
                        for b in self.Beasties:
                            b.Move()
        pygame.time.wait(1500)

    def CreateRoom(self, level):
        self.TheRoom = Room((0, 255, 0))

        self.TheTiles = []
        self.Beasties = []
        self.Lasers = []
        self.TilesDone = 0
        self.p1.Pos(self.StartPos)
        self.p1.Tiles = 30

        self.LM.CreateRoom(level, self.TheTiles, self.Beasties, self.Lasers)

    def CheckTiles(self):

        if self.TilesDone == len(self.TheTiles) and len(self.TheTiles) > 0:
            self.SND.Play("Done")
            pygame.time.wait(1500)
            self.p1.Level += 1
            self.CreateRoom(self.p1.Level)

        # Restock Carpet Tiles
        if self.TheRoom.RocketRect.colliderect(self.p1.Hotspot):
            self.p1.Tiles = 30
            if not self.InRocket:
                self.SND.Play("Reload")
            self.InRocket = True
        else:
            self.InRocket = False

        # Beasties
        self.p1.Hurting = False
        for b in self.Beasties:
            if b.Hotspot.colliderect(self.p1.rect):
                self.p1.Health -= b.Damage
                self.SND.Play("Hurt")
                self.p1.Hurting = True

        for l in self.Lasers:
            if l.Hotspot.colliderect(self.p1.rect):
                self.p1.Health -= l.Damage
                self.SND.Play("Hurt")
            if l.Firing:
                if l.LaserRect.colliderect(self.p1.rect):
                    self.p1.Health -= l.Damage
                    self.SND.Play("Hurt")
        # for l in self.Lasers:
            # if l.Firing:
                # self.SND.Play("Laser")

        # Tiles
        if self.p1.Tiles == 0:
            return

        for t in self.TheTiles:
            if t.carpet == False and t.Hotspot.colliderect(self.p1.Hotspot):
                t.carpet = True
                self.SND.Play("LayTile")
                self.TilesDone += 1
                self.p1.Tiles -= 1
                self.p1.Score += 10
                if self.p1.Tiles == 0:
                    self.SND.Play("TilesOut")

    def DrawRoom(self):
        self.Surface.fill(pygame.Color("black"))

        # gfx
        self.Surface.lock()

        self.TheRoom.Draw(self.Surface)
        for t in self.TheTiles:
            t.Draw(self.Surface)
        for b in self.Beasties:
            b.Draw(self.Surface)
        for l in self.Lasers:
            l.Draw(self.Surface)
        self.StatusBar.Draw(self.Surface)

        self.p1.Draw(self.Surface)
        self.Surface.unlock()

        # Txt
        DrawText(self.Surface, 120, 570, "Progress : " + str(self.TilesDone) +
                 " / " + str(len(self.TheTiles)), 24, (240, 240, 240))
        DrawText(self.Surface, 20, 570, "Level : " +
                 str(self.p1.Level), 24, (240, 240, 240))
        DrawText(self.Surface, 320, 570, "Tiles : " +
                 str(self.p1.Tiles), 24, (240, 240, 0))
        if self.p1.Tiles == 0:
            pygame.draw.rect(self.Surface, (255, 255, 255), (395, 567, 75, 20))
            DrawText(self.Surface, 399, 570, "RELOAD", 24, (240, 0, 0))
        DrawText(self.Surface, 520, 570, "Score : " +
                 str(self.p1.Score), 24, (240, 240, 240))
        if self.p1.Hurting or self.p1.Health < 10:
            pygame.draw.rect(self.Surface, (255, 0, 0), (610, 560, 125, 40))
        DrawText(self.Surface, 620, 570, "Health : " +
                 str(self.p1.Health), 24, (240, 240, 240))

        # Flip
        self.Screen.blit(self.Surface, (0, 0))
        pygame.display.flip()
