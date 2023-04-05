import pygame
from pygame.locals import *
from .Dice import Dice
from .GameField.GameField import GameField

from .settings import Settings


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("Würfel_1.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()


class Game:
    def __init__(self):
        self.width = Settings.WINDOW_WIDTH
        self.height = Settings.WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dice = Dice(Settings.DICE_POSITION, Settings.DICE_SIZE)

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
            Settings.listPlayers[currentPlayerNumber].name,
            True,
            Settings.listPlayers[currentPlayerNumber].color,
        )
        screen.blit(font_surface, Settings.CURRENT_PLAYER_POSITION)

    def runGame(self):
        screen = self.screen
        screen.fill(Settings.BACKGROUNDCOLOR)

        gameActive = True
        currentPlayerNumber = 0
        numberOfPlayers = len(Settings.listPlayers)

        diceTries = 0
        diceStatus = "static"
        diceAnimationCounter = 0

        gamefield = GameField(numberOfPlayers)

        # Wir haben 3 Phasen in einem Zug:
        # 0: nicht gewürfelt, 1: gewürfelt und nun wird Figur ausgewählt, 2: Figur wurde gezogen
        # bei einer 6 wird am Ende auf 0 zurückgesetzt

        currentStage = 0

        # Set up timer
        clock = pygame.time.Clock()

        while gameActive:
            screen.fill(Settings.BACKGROUNDCOLOR)
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
                        if self.dice.handleClick(mousePosition):
                            if (
                                gamefield.checkAllFiguresInBase(currentPlayerNumber)
                                and self.dice.currentValue == 6
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
                            mousePosition, currentPlayerNumber, self.dice.currentValue
                        ):
                            currentStage = 2
                    elif currentStage == 2:
                        waitClickResult = gamefield.waitClickCircleToMoveTo(
                            mousePosition, currentPlayerNumber
                        )
                        if waitClickResult and self.dice.currentValue != 6:
                            currentStage = 0
                            currentPlayerNumber = self.changePlayer(
                                currentPlayerNumber, numberOfPlayers
                            )
                        elif waitClickResult and self.dice.currentValue == 6:
                            currentStage = 0
                        elif waitClickResult == False:
                            gamefield.waitClickFigureToMove(
                                mousePosition,
                                currentPlayerNumber,
                                self.dice.currentValue,
                            )
                            currentStage = 1

            # Gamelogic

            # Draw Structures and Figures

            # Draw Dice
            if diceStatus == "rolling":
                self.dice.drawAnimation(screen, currentPlayerNumber, diceAnimationCounter)
                diceAnimationCounter += 1
                if diceAnimationCounter == 100:
                    diceStatus = "static"
            elif diceStatus == "static":
                self.dice.draw(screen, currentPlayerNumber)

            gamefield.draw(screen)

            self.drawCurrentPlayer(currentPlayerNumber, screen)

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()
