import sys
import math
import pygame
from pygame.locals import *

from gamelib.util import *
from gamelib.gfxlib import *
from gamelib.gfxgame import *
from gamelib.CarpetGame import *

# Globals.
ScreenSize = [800,600]
Debug = False
#GameName = "One Room"
GameName = "ONE ROOM"

# Standard Init.

#pygame.mixer.init()
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print ("No joysticks")
    ajoystick = None
else:
    ajoystick = pygame.joystick.Joystick(0)
    ajoystick.init()

screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption(GameName)

pygame.time.set_timer(ANIMEVENT, 30)

surface = CreateBackground(screen)
Game = None

#------
# MAIN
#------
def main():
    #pygame.mixer.music.load("snd/menu.mp3")
    #pygame.mixer.music.play(-1)
    
    GameState = 1
    DrawText(surface, 10, 50, "Daftspaniel Presents...", 48, (255,255,255) )
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    
    for k in range(9):
        DrawGradient(surface, Color(125, 0, 111 + k*3), Rect(0,0,800,600))
        DrawText(surface, 210, 250, GameName[:k], 78, (255,0,0) )
        DrawText(surface, 211, 251, GameName[:k], 78, (255,156,0) )
        DrawText(surface, 212, 252, GameName[:k], 78, (245,245,245) )
        pygame.time.wait(300)
        screen.blit(surface, (0, 0))
        pygame.display.flip()
    
    cb = copperBar()
    cbr = copperBar( (1,0,0), 50 )
    backcol = 255
    dudex = 0
    
    while GameState!=-1:

        if GameState == 1:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == ANIMEVENT:
                    #surface.fill(pygame.Color("black"))
                    surface.lock()
                    backcol += 1
                    dudex += 1
                    dudey = int(math.sin(dudex/20) * 120)
                    if backcol>255:backcol=0
                    if dudex>820:dudex=-10
                    DrawGradient(surface, Color(125, 0, backcol), Rect(0,0,800,600))
                    drawMatchstickPerson(surface, (dudex, 280 + dudey), Color(RND(255),255,0))
                    
                    cb.Draw(surface)
                    cbr.Draw(surface)
                    surface.unlock()
                    DrawText(surface, 210, 250, GameName, 78, (255,0,0) )
                    DrawText(surface, 211, 251, GameName, 78, (255,156,0) )
                    DrawText(surface, 212, 252, GameName, 78, (255,255,255) )
                    
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 3
                        pygame.mixer.music.stop()
                    if keystate[K_ESCAPE]==1:
                        GameState = -1

            screen.blit(surface, (0, 0))
            pygame.display.flip()
        
        elif GameState == 3: # Game on!
            
            surface.fill(pygame.Color("black"))
            pygame.display.flip()
            
            Game = CarpetGame( surface, screen, (800,600), ajoystick ) 
            
            while GameState == 3:
                print("Game on")
                Game.MainLoop()
                GameState = 4
            
        elif GameState == 4: # Game over!
            
            print("Game over")
            surface.fill(pygame.Color("black"))
            DrawText(surface, 10, 50, "Game Over", 48, (255,0,0) )
            
            while GameState == 4:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        keystate = pygame.key.get_pressed()
                        if keystate[K_SPACE]:
                            GameState = 1
                    elif event.type == ANIMEVENT:
                        screen.blit(surface, (0, 0))
                        pygame.display.flip()

        elif GameState == 5: # Game Win

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == ANIMEVENT:
                    surface.fill(pygame.Color("black"))
                    DrawText(surface, 10, 50, "Well Done!", 48, (255,0,0) )
                    
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 1
                        
            screen.blit(GameBG, (0, 0))
            pygame.display.flip()
