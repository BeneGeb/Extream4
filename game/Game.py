import pygame
import time
from pygame.locals import *
from .Dice import Dice
from .Computer import Computer
from .GameField.GameField import GameField
from .Helper.GameState import *
from .settings import Settings
from .ClickButton import ClickButton


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("./Images/Extream4.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()

# Nur bei 6 darf eine Figure aus der Base raus gehen


class Game:
    def __init__(self, callBackStartEndWindow, loadedState=None, sameColorMode=None):
        self.screen = pygame.display.set_mode(
            (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.RESIZABLE
        )
        self.dice = Dice()
        if loadedState == None:
            self.gamefield = GameField()
            self.currentPlayerNumber = 0
        else:
            self.gamefield = loadedState.gameField
            self.currentPlayerNumber = loadedState.currentPlayer
        self.sameColorMode = sameColorMode
        self.gameState = GameState()
        self.currentStage = "waitingForDice"
        self.rollingProgress = 0
        self.diceTries = 0
        self.computers = self.createKi()
        self.buttons = self.createButtons()
        self.gameState = GameState()

        pygame.mixer.init()
        pygame.mixer.music.load("./Sounds/Extrem_Sound.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)
        self.musicOn = True

        self.callBackStartEndWindow = callBackStartEndWindow

        self.runGame()

    # region ButtonFunctions
    def rageQuit(self):
        print("Ragequit")

    def saveGameState(self):
        self.gameState.saveGameState(
            self.gamefield, self.currentPlayerNumber, Settings.listPlayers
        )

    def clickSoundButton(self):
        if self.musicOn:
            pygame.mixer.music.set_volume(0)
            self.musicOn = False
        else:
            pygame.mixer.music.set_volume(0.2)
            self.musicOn = True

    def clickMuteGameSounds(self):
        print("mute")

    def createButtons(self):
        allButtons = []
        allButtons.append(
            ClickButton(
                (45, 300),
                self.saveGameState,
                "Speichern",
                Settings.DARKGRAY,
            )
        )
        allButtons.append(
            ClickButton((45, 780), self.rageQuit, "RAGEQUIT", Settings.RED)
        )
        allButtons.append(
            ClickButton(
                (45, 380),
                self.clickMuteBackgroundMusic,
                "Music On",
                Settings.DARKGRAY,
            )
        )

        allButtons.append(
            ClickButton(
                (45, 460),
                self.clickMuteGameSounds,
                "Gamesound On",
                Settings.DARKGRAY,
            )
        )
        return allButtons

    def drawButtons(self):
        for button in self.buttons:
            button.draw(self.screen)

    # endregion

    def handleButtonClicks(self, mousePosition):
        for button in self.buttons:
            button.handleClick(mousePosition)

    def createKi(self):
        startFields = [40, 10, 20, 30]
        computers = []
        for num, player in enumerate(Settings.listPlayers):
            if player.isKi:
                computers.append(
                    Computer(num, self.gamefield, startFields[num]))
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
            self.diceTries = 0

    def kiHandlewWaitingForComputer(self):
        self.computers[self.currentPlayerNumber].evalNextMove(
            self.gamefield, self.dice.currentValue
        )
        self.currentStage = "waitingForDice"
        # if self.gamefield.checkWin(self.currentPlayerNumber):
        #     self.gameActive = False
        #     self.callBackStartEndWindow(self.currentPlayerNumber)

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

    # region PlayerFunctions
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
            self.diceTries = 0

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
                self.callBackStartEndWindow(
                    self.currentPlayerNumber, self.gamefield)

            if self.dice.currentValue <= 5:
                self.changePlayer()
        else:
            self.gamefield.waitClickFigureToMove(
                mousePosition, self.currentPlayerNumber, self.dice.currentValue
            )

    # endregion

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
                    self.handleButtonClicks(mousePosition)
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

            # Draw dice background
            pygame.draw.rect(
                self.screen, Settings.GRAY, [20, 20, 250, 235], border_radius=30
            )

            # Draw dice
            if self.currentStage == "rollingDice":
                self.dice.drawAnimation(
                    self.screen, self.currentPlayerNumber, self.rollingProgress
                )
            else:
                self.dice.draw(self.screen, self.currentPlayerNumber)

            # Draw GameField
            self.gamefield.draw(self.screen)

            self.drawCurrentPlayer(self.currentPlayerNumber, self.screen)

            # Draw Buttons
            self.drawButtons()

            # Update Display
            pygame.display.flip()

            # Setup refreshtimer
            clock.tick(60)

        pygame.quit()
