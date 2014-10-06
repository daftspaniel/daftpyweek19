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
pygame.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption(GameName)

pygame.time.set_timer(ANIMEVENT, 30)

surface = CreateBackground(screen)
Game = None

#------
# MAIN
#------
def main():
    
    GameState = 1
    DrawText(surface, 10, 50, "Daftspaniel Presents...", 48, (255,255,255) )
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
                    
                    cb.draw(surface)
                    cbr.draw(surface)
                    surface.unlock()
                    DrawText(surface, 210, 250, GameName, 78, (255,0,0) )
                    DrawText(surface, 211, 251, GameName, 78, (255,156,0) )
                    DrawText(surface, 212, 252, GameName, 78, (255,255,255) )
                    
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 3
                    if keystate[K_ESCAPE]==1:
                        GameState = -1

            screen.blit(surface, (0, 0))
            pygame.display.flip()
        
        elif GameState == 3: # Game on!
            
            surface.fill(pygame.Color("black"))
            pygame.display.flip()
            
            Game = CarpetGame( surface, screen, (800,600) ) 
            
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
