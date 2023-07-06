import pygame
import time
from pygame.locals import *
from .Dice import Dice
from .Computer import Computer
from .GameField.GameField import GameField
from .Helper.GameState import *
from .settings import Settings
from .ClickButton import ClickButton
from .Rule import Rule
from .Helper.ListSorter import sortPlayers
from .Textbox import TextBox
from .Ressources.Rules import *


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("./Images/Extream4.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()


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
        self.rule = Rule()
        self.currentStage = "waitingForDice"
        self.rollingProgress = 0
        self.diceTries = 0
        self.computers = self.createKi()
        self.buttons = self.createButtons()
        self.gameState = GameState()
        #################################################################
        self.ruleBox = None
        if sameColorMode == None:
            self.ruleBox = TextBox(rules, (1450, 20), True)
        else:
            self.ruleBox = TextBox(extremrules, (1450, 20), True)

        pygame.mixer.init()
        pygame.mixer.music.load("./Sounds/Extrem_Sound.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)
        self.musicOn = True
        self.soundOn = True
        self.showrules = False
        self.image = pygame.image.load("./Images/Regeln.png")

        self.callBackStartEndWindow = callBackStartEndWindow

        self.runGame()

    # region ButtonFunction

    def saveGameState(self, button):
        self.gameState.saveGameState(
            self.gamefield, self.currentPlayerNumber, Settings.listPlayers
        )

    def clickMuteMusic(self, button):
        if self.musicOn:
            pygame.mixer.music.set_volume(0)
            self.musicOn = False
            button.buttonText = "Music Off"
            button.backgroundColor = Settings.RED
        else:
            pygame.mixer.music.set_volume(0.2)
            self.musicOn = True
            button.buttonText = "Music On"
            button.backgroundColor = Settings.GREEN

    def clickMuteGameSounds(self, button):
        if self.soundOn:
            self.soundOn = False
            self.gamefield.changeGameSound(self.soundOn)
            button.buttonText = "Gamesound Off"
            button.backgroundColor = Settings.RED
        else:
            self.soundOn = True
            self.gamefield.changeGameSound(self.soundOn)
            button.buttonText = "Gamesound On"
            button.backgroundColor = Settings.GREEN

    def clickRule(self, button):
        if self.showrules != True:
            self.showrules = True
        else:
            self.showrules = False

    def createButtons(self):
        allButtons = []
        allButtons.append(
            ClickButton(
                None,
                self.saveGameState,
                "Speichern",
                Settings.DARKGRAY,
            )
        )
        allButtons.append(
            ClickButton(
                None,
                self.clickRule,
                "Regeln",
                Settings.DARKGRAY,
            )
        )
        allButtons.append(
            ClickButton(
                None,
                self.clickMuteMusic,
                "Music On",
                Settings.GREEN,
            )
        )
        allButtons.append(
            ClickButton(
                None,
                self.clickMuteGameSounds,
                "Gamesound On",
                Settings.GREEN,
            )
        )

        buttonXPosition = (
            Settings.DICE_POSITION[0] -
            Settings.DICE_SIZE / 2 + Settings.CIRCLE_SIZE
        )
        buttonYPosition = (
            Settings.DICE_POSITION[1]
            + 2 * Settings.DICE_SIZE
            + Settings.CIRCLE_SIZE / 2
        )

        for button in allButtons:
            button.position = (buttonXPosition, buttonYPosition)
            buttonYPosition = buttonYPosition + 2.5 * Settings.CIRCLE_SIZE

        # Hier kommen Buttons hin, die nicht links erscheinen sollen
        return allButtons

    def drawButtons(self):
        for button in self.buttons:
            button.draw(self.screen, None)

    def handleButtonClicks(self, mousePosition):
        for button in self.buttons:
            button.handleClick(mousePosition)

    # endregion

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

        screen.blit(
            font_surface,
            (
                Settings.DICE_POSITION[0] + 10,
                Settings.DICE_POSITION[1] + Settings.DICE_SIZE * 1.1,
            ),
        )

    def drawBackgrounds(self):
        pygame.draw.rect(
            self.screen,
            Settings.GRAY,
            [
                Settings.DICE_POSITION[0] - Settings.DICE_SIZE / 2,
                Settings.DICE_POSITION[1] - Settings.DICE_SIZE / 2,
                Settings.DICE_SIZE * 2,
                Settings.DICE_SIZE * 2,
            ],
            border_radius=30,
        )
        centerPositionX, centerPositionY = Settings.GAMEFIELD_POSITION
        topleftCirclePositionX = centerPositionX - 6 * Settings.CIRCLE_DIFFERENCE
        topleftCirclePositionY = centerPositionY - 6 * Settings.CIRCLE_DIFFERENCE
        rectangleSize = 12 * Settings.CIRCLE_DIFFERENCE
        pygame.draw.rect(
            self.screen,
            Settings.DARKGRAY,
            [
                topleftCirclePositionX,
                topleftCirclePositionY,
                rectangleSize,
                rectangleSize,
            ],
            border_radius=30,
            width=5,
        )

        pygame.draw.rect(
            self.screen,
            Settings.GRAY,
            [
                topleftCirclePositionX + 5,
                topleftCirclePositionY + 5,
                rectangleSize - 10,
                rectangleSize - 10,
            ],
            border_radius=25,
        )
        for i in range(0, 4):
            pygame.draw.rect(
                self.screen,
                Settings.DARKGRAY,
                [
                    topleftCirclePositionX + Settings.CIRCLE_SIZE,
                    topleftCirclePositionY + Settings.CIRCLE_SIZE,
                    6 * Settings.CIRCLE_SIZE,
                    6 * Settings.CIRCLE_SIZE,
                ],
                border_radius=30,
            )
            if i == 0:
                topleftCirclePositionX = (
                    topleftCirclePositionX + 9 * Settings.CIRCLE_DIFFERENCE
                )
            if i == 1:
                topleftCirclePositionY = (
                    topleftCirclePositionY + 9 * Settings.CIRCLE_DIFFERENCE
                )
            if i == 2:
                topleftCirclePositionX = (
                    topleftCirclePositionX - 9 * Settings.CIRCLE_DIFFERENCE
                )
        pygame.draw.rect(
            self.screen,
            Settings.GRAY,
            [
                Settings.DICE_POSITION[0] - Settings.DICE_SIZE / 2,
                Settings.DICE_POSITION[1] + 2 * Settings.DICE_SIZE,
                Settings.DICE_SIZE * 2,
                325,
            ],
            border_radius=30,
        )

    # region KIFunctions
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
        self.dice.handleClick((0, 0), True, self.soundOn)
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
        if self.gamefield.checkWin(self.currentPlayerNumber):
            self.gameActive = False
            self.callBackStartEndWindow(
                self.currentPlayerNumber, self.gamefield)
        if self.dice.currentValue <= 5:
            self.changePlayer()

    # endregion
    # region PlayerFunctions
    def handleWaitingForDice(self, mouseposition):
        diceClicked = self.dice.handleClick(mouseposition, False, self.soundOn)
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
        waitClickFigure = self.gamefield.waitClickFigureToMove(
            mousePosition,
            self.currentPlayerNumber,
            self.dice.currentValue,
            self.sameColorMode,
        )
        if "clicked" in waitClickFigure:
            self.currentStage = "waitingForPlacingFigure"
        elif "change" in waitClickFigure:
            self.changePlayer()
            self.currentStage = "waitingForDice"

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
            waitClick = self.gamefield.waitClickFigureToMove(
                mousePosition,
                self.currentPlayerNumber,
                self.dice.currentValue,
                self.sameColorMode,
            )
            if "change" in waitClick:
                self.changePlayer()
                self.currentStage = "waitingForDice"

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
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and Settings.listPlayers[self.currentPlayerNumber].isKi
                ):
                    mousePosition = pygame.mouse.get_pos()
                    self.handleButtonClicks(mousePosition)
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
            self.drawBackgrounds()

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

            # Draw Rules

            if self.showrules:
                pygame.draw.rect(
                    self.screen,
                    Settings.WHITE,
                    (1440, 0, 500, 1000),
                    border_radius=20,
                )
                self.ruleBox.draw(self.screen)

            # Update Display
            pygame.display.flip()

            # Setup refreshtimer
            clock.tick(60)

        pygame.quit()
