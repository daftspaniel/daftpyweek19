import sys
import os

import pygame
from pygame.locals import *

class sndman(object):
    
    def __init__(self):
        self.sounda= self.Load("laytile.wav")
        self.soundb= self.Load("tileup.wav")
        self.tilesout = self.Load("outoftiles.wav")
        self.hurt_sfx = self.Load("hurt.wav")
        self.laser_sfx = self.Load("laser.wav")
        self.leveldone = self.Load("leveldone.wav")
    
    def Load(self, filename):
        return pygame.mixer.Sound( os.path.join("snd", filename) )
    
    def Play(self, name):
        
        if name=="LayTile":
            self.sounda.play()
        elif name=="Reload":
            self.soundb.play()
        elif name=="TilesOut":
            self.tilesout.play()
        elif name=="Laser":
            self.laser_sfx.play()
        elif name=="Hurt":
            self.hurt_sfx.play()
        elif name=="Done":
            self.leveldone.play()
