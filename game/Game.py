import pygame
from pygame.locals import *

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

class Game:
    def runGame(self):
        screen = pygame.display.set_mode((1142, 1008))
        
        #Hintergrund
        bg = pygame.image.load("Spielbrett.png")
        bg = pygame.transform.scale(bg,(1142,1008))

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
                    print("Spieler hast Maus angeklickt")

            # Gamelogic

            # Fill Display
            #screen.fill(WEISS)

            # Draw Structures and Figures

            # Update Disply
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()


