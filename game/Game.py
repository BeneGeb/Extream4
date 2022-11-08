import pygame
from pygame.locals import *
from .Dice import Dice
from .figure import Figure

pygame.init()

ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)


class Game:
    def __init__(self):
        self.width = 1142
        self.height = 1008
        self.screen = pygame.display.set_mode((self.width, self.height))

    def runGame(self):
        screen = self.screen
        # Hintergrund
        bg = pygame.image.load("Spielbrett.png")
        bg = pygame.transform.scale(bg, (self.width, self.height))

        dice = Dice((0, 0), 100)
        pygame.display.set_caption("Unser erstes Pygame-Spiel")

        gameActive = True

        # Set up timer
        clock = pygame.time.Clock()

        while gameActive:
            # Hintergrund
            screen.blit(bg, (0, 0))
            # UserInteraction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    print("Spieler hat Quit-Button angeklickt")
                elif event.type == pygame.KEYDOWN:
                    print("Spieler hat Taste gedrückt")

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    dice.handleClick(pygame.mouse.get_pos())

            # Gamelogic

            # Draw Structures and Figures
            dice.draw(screen)

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()
