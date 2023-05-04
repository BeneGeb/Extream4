import pygame
import time
from pygame.locals import *
from .Dice import Dice
from .Computer import Computer
from .GameField.GameField import GameField

from .settings import Settings


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("Extream4.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()

# Nur bei 6 darf eine Figure aus der Base raus gehen
class Game:
    def __init__(self, callBackStartEndWindow):
        self.screen = pygame.display.set_mode(
            (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.RESIZABLE
        )
        self.dice = Dice()
        self.gamefield = GameField()
        self.currentPlayerNumber = 0
        self.currentStage = "waitingForDice"
        self.rollingProgress = 0
        self.diceTries = 0
        self.currentPlayerNumber = 0
        self.computers = self.createKi()

        self.callBackStartEndWindow = callBackStartEndWindow

        self.runGame()

    def createKi(self):
        computers = []
        for num, player in enumerate(Settings.listPlayers):
            if player.isKi:
                computers.append(Computer(num, self.gamefield))
            else:
                computers.append(None)
        return computers

    def kiDiceRolling(self):
        self.dice.handleClick((0, 0), True)
        self.currentStage = "rollingDice"

    def kiEvalDiceRolling(self):
        if not self.gamefield.checkIsMovePossible(
            self.currentPlayerNumber, self.dice.currentValue
        ):
            if self.dice.currentValue == 6:
                self.currentStage = "waitForComputer"
                self.diceTries = 0
            elif self.diceTries < 2:
                self.currentStage = "waitingForDice"
                self.diceTries += 1
            elif self.diceTries == 2:
                self.changePlayer()
                self.diceTries = 0
                self.currentStage = "waitingForDice"
        else:
            self.currentStage = "waitForComputer"

    def kiHandlewWaitingForComputer(self):
        self.computers[self.currentPlayerNumber].evalNextMove(
            self.gamefield, self.dice.currentValue
        )
        self.currentStage = "waitingForDice"
        if self.gamefield.checkWin(self.currentPlayerNumber):
            self.gameActive = False
            self.callBackStartEndWindow(self.currentPlayerNumber)

        if self.dice.currentValue <= 5:
            self.changePlayer()

    def changePlayer(self):
        if self.currentPlayerNumber < 4 - 1:
            self.currentPlayerNumber += 1
        else:
            self.currentPlayerNumber = 0

    def drawCurrentPlayer(self, currentPlayerNumber, screen):
        font = pygame.font.Font(None, 40)
        font_surface = font.render(
            Settings.listPlayers[currentPlayerNumber].name,
            True,
            Settings.listPlayers[currentPlayerNumber].color,
        )
        screen.blit(font_surface, Settings.CURRENT_PLAYER_POSITION)

    def handleWaitingForDice(self, mouseposition):
        diceClicked = self.dice.handleClick(mouseposition, False)
        # If Dice not Clicked
        if diceClicked == None:
            return

        self.currentStage = "rollingDice"

    def evalDiceRolling(self):
        if not self.gamefield.checkIsMovePossible(
            self.currentPlayerNumber, self.dice.currentValue
        ):
            if self.dice.currentValue == 6:
                self.currentStage = "waitForChoosingFigure"
                self.diceTries = 0
            elif self.diceTries < 2:
                self.currentStage = "waitingForDice"
                self.diceTries += 1
            elif self.diceTries == 2:
                self.changePlayer()
                self.diceTries = 0
                self.currentStage = "waitingForDice"
                time.sleep(1)
        else:
            self.currentStage = "waitForChoosingFigure"

    def handleRollingDice(self):
        if self.rollingProgress == 0:
            self.dice.rollDice()
            self.rollingProgress += 1
            return

        if self.rollingProgress < 100:
            self.rollingProgress += 1
            return

        if Settings.listPlayers[self.currentPlayerNumber].isKi:
            self.kiEvalDiceRolling()
        else:
            self.evalDiceRolling()
        self.rollingProgress = 0

    def handleWaitChooseFigure(self, mousePosition):
        if self.gamefield.waitClickFigureToMove(
            mousePosition, self.currentPlayerNumber, self.dice.currentValue
        ):
            self.currentStage = "waitingForPlacingFigure"

    def handleWaitForPlacingFigure(self, mousePosition):
        waitClickResult = self.gamefield.waitClickCircleToMoveTo(
            mousePosition, self.currentPlayerNumber, self.dice.currentValue
        )
        if waitClickResult:
            self.currentStage = "waitingForDice"
            if self.gamefield.checkWin(self.currentPlayerNumber):
                self.gameActive = False
                self.callBackStartEndWindow(self.currentPlayerNumber)

            if self.dice.currentValue <= 5:
                self.changePlayer()
        else:
            self.gamefield.waitClickFigureToMove(
                mousePosition, self.currentPlayerNumber, self.dice.currentValue
            )

    def runGame(self):
        self.gameActive = True

        # Set up timer
        clock = pygame.time.Clock()

        while self.gameActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameActive = False
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and not Settings.listPlayers[self.currentPlayerNumber].isKi
                ):
                    mousePosition = pygame.mouse.get_pos()
                    self.gamefield.getClickedCircle(mousePosition)
                    if self.currentStage == "waitingForDice":
                        self.handleWaitingForDice(mousePosition)
                    elif self.currentStage == "waitForChoosingFigure":
                        self.handleWaitChooseFigure(mousePosition)
                    elif self.currentStage == "waitingForPlacingFigure":
                        self.handleWaitForPlacingFigure(mousePosition)
            if Settings.listPlayers[self.currentPlayerNumber].isKi:
                if self.currentStage == "waitingForDice":
                    self.kiDiceRolling()
                    time.sleep(1)
                elif self.currentStage == "waitForComputer":
                    self.kiHandlewWaitingForComputer()
                    time.sleep(1)

            # Gamelogic
            if self.currentStage == "rollingDice":
                self.handleRollingDice()

            # Draw Background
            self.screen.fill(Settings.BACKGROUNDCOLOR)

            # Draw Dice
            if self.currentStage == "rollingDice":
                self.dice.drawAnimation(
                    self.screen, self.currentPlayerNumber, self.rollingProgress
                )
            else:
                self.dice.draw(self.screen, self.currentPlayerNumber)

            # Draw GameField
            self.gamefield.draw(self.screen)

            self.drawCurrentPlayer(self.currentPlayerNumber, self.screen)

            # Update Display
            pygame.display.flip()

            # Setup refreshtimer
            clock.tick(60)

        pygame.quit()
