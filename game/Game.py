import pygame
from pygame.locals import *
from .Dice import Dice
from .GameField.GameField import GameField
import tkinter


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("Würfel_1.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()

ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)


class Game:
    def __init__(self, width, height, allPlayer):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.allPlayer = allPlayer

    def changePlayer(self, currentPlayerNumber, numberOfPlayers):
        if currentPlayerNumber < numberOfPlayers - 1:
            currentPlayerNumber += 1
        else:
            currentPlayerNumber = 0
        print("Next Player")
        return currentPlayerNumber

    def drawCurrentPlayer(self, currentPlayerNumber, screen):
        font = pygame.font.Font(None, 40)
        font_surface = font.render(
            self.allPlayer[currentPlayerNumber], True, pygame.Color("white")
        )
        screen.blit(font_surface, (0, 150))

    def runGame(self):
        screen = self.screen
        allPlayer = self.allPlayer
        screen.fill((155, 155, 155))

        gameActive = True
        currentPlayerNumber = 0
        numberOfPlayers = len(allPlayer)
        diceTries = 0
        diceStatus = "static"
        diceAnimationCounter = 0

        dice = Dice((0, 0), 130)
        gamefield = GameField(numberOfPlayers)

        # Wir haben 3 Phasen in einem Zug:
        # 0: nicht gewürfelt, 1: gewürfelt und nun wird Figur ausgewählt, 2: Figur wurde gezogen
        # bei einer 6 wird am Ende auf 0 zurückgesetzt

        currentStage = 0

        # Set up timer
        clock = pygame.time.Clock()

        while gameActive:
            screen.fill((155, 155, 155))
            # UserInteraction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    print("Spieler hat Quit-Button angeklickt")
                elif event.type == pygame.KEYDOWN:
                    print("Spieler hat Taste gedrückt")

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()
                    gamefield.devHelper(mousePosition)
                    if currentStage == 0:
                        # Es wurde noch nicht gewürfelt
                        if dice.handleClick(mousePosition):
                            if (
                                gamefield.checkAllFiguresInBase(currentPlayerNumber)
                                and dice.currentValue == 6
                            ):
                                currentStage += 1
                                diceTries = 0
                            elif (
                                gamefield.checkAllFiguresInBase(currentPlayerNumber)
                                and diceTries < 2
                            ):
                                diceTries += 1
                            elif (
                                gamefield.checkAllFiguresInBase(currentPlayerNumber)
                                and diceTries > 1
                            ):
                                currentPlayerNumber = self.changePlayer(
                                    currentPlayerNumber, numberOfPlayers
                                )
                                diceTries = 0
                            else:
                                currentStage += 1
                                diceTries = 0
                            diceStatus = "rolling"
                            diceAnimationCounter = 0
                            print("rolled Dice")
                    elif currentStage == 1:
                        if gamefield.waitClickFigureToMove(
                            mousePosition, currentPlayerNumber, dice.currentValue
                        ):
                            currentStage = 2
                    elif currentStage == 2:
                        waitClickResult = gamefield.waitClickCircleToMoveTo(
                            mousePosition, currentPlayerNumber
                        )
                        if waitClickResult and dice.currentValue != 6:
                            currentStage = 0
                            currentPlayerNumber = self.changePlayer(
                                currentPlayerNumber, numberOfPlayers
                            )
                        elif waitClickResult and dice.currentValue == 6:
                            currentStage = 0
                        elif waitClickResult == False:
                            gamefield.waitClickFigureToMove(
                                mousePosition, currentPlayerNumber, dice.currentValue
                            )
                            currentStage = 1

                    # elif currentStage == 2:
                    # if gamefield.handleClick(
                    #     mousePosition, currentPlayerNumber, currentStage
                    # ):
                    #     if currentStage == 1:
                    #         currentStage += 1
                    #     elif currentStage == 2 and dice.currentValue != 6:
                    #         currentStage = 0
                    #         currentPlayerNumber = self.changePlayer(
                    #             currentPlayerNumber, numberOfPlayers
                    #         )
                    #     elif currentStage == 2 and dice.currentValue == 6:
                    #         currentStage = 0

            # Gamelogic

            # Draw Structures and Figures
            if diceStatus == "rolling":
                dice.drawAnimation(screen, diceAnimationCounter)
                diceAnimationCounter += 1
                if diceAnimationCounter == 100:
                    diceStatus = "static"
            elif diceStatus == "static":
                dice.draw(screen)

            gamefield.draw(screen)

            self.drawCurrentPlayer(currentPlayerNumber, screen)

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()
