import pygame
from pygame.locals import *
import random

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Würfel Klasse

# WürfelAugenbilder mit Skalierung
dice1 = pygame.image.load("Würfel_1.png")
dice1 = pygame.transform.scale(dice1, (100,100))
dice2 = pygame.image.load("Würfel_2.png")
dice2 = pygame.transform.scale(dice2, (100,100))
dice3 = pygame.image.load("Würfel_3.png")
dice3 = pygame.transform.scale(dice3, (100,100))
dice4 = pygame.image.load("Würfel_4.png")
dice4 = pygame.transform.scale(dice4, (100,100))
dice5 = pygame.image.load("Würfel_5.png")
dice5 = pygame.transform.scale(dice5, (100,100))
dice6 = pygame.image.load("Würfel_6.png")
dice6 = pygame.transform.scale(dice6, (100,100))

# Liste der Würfelaugen
all_dice = [ None, dice1, dice2, dice3, dice4, dice5, dice6 ]
pygame.display.set_icon( dice6 )

def Wuerfelwurf():
    wurf   = random.randint( 1, 6 )

    return wurf



class Game:
    def runGame(self):
        wurf = 0
        wuerfelaugen = None
        laenge = 1142
        breite = 1008
        screen = pygame.display.set_mode((laenge, breite))
        
        #Hintergrund
        bg = pygame.image.load("Spielbrett.png")
        bg = pygame.transform.scale(bg,(laenge, breite))

        pygame.display.set_caption("Unser erstes Pygame-Spiel")

        gameActive = True

        # Set up timer
        clock = pygame.time.Clock()


        while gameActive:
            # Hintergrund
            screen.blit(bg,(0,0))
            # UserInteraction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    print("Spieler hat Quit-Button angeklickt")
                elif event.type == pygame.KEYDOWN:
                    print("Spieler hat Taste gedrückt")

                
                    if event.key == pygame.K_RIGHT:
                        print("Spieler hat Pfeiltaste rechts gedrückt")
                    elif event.key == pygame.K_LEFT:
                        print("Spieler hat Pfeiltaste links gedrückt")
                    elif event.key == pygame.K_UP:
                        print("Spieler hat Pfeiltaste hoch gedrückt")
                    elif event.key == pygame.K_DOWN:
                        print("Spieler hat Pfeiltaste runter gedrückt")
                    elif event.key == pygame.K_SPACE:
                        print("Spieler hat Leertaste gedrückt")

                    elif event.key == pygame.K_w:
                        print("Spieler hat Taste w gedrückt")
                    elif event.key == pygame.K_a:
                        print("Spieler hat Taste a gedrückt")
                    elif event.key == pygame.K_s:
                        print("Spieler hat Taste s gedrückt")
                    elif event.key == pygame.K_d:
                        print("Spieler hat Taste d gedrückt")

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    wurf = Wuerfelwurf()
                    wuerfelaugen = all_dice[wurf]
                    print(f"Spieler hat {wurf} gerollt")
                
            # Würfelbild und Koordinaten des Würfels
            if ( wuerfelaugen != None ):
                screen.blit( wuerfelaugen, ( 0, 0) ) 

            # Gamelogic

            

            # Draw Structures and Figures

            # Update Disply
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()


