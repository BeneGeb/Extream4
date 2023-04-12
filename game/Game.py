import pygame
from pygame.locals import *
from .Dice import Dice
from .GameField.GameField import GameField

from .settings import Settings


def setUpPygame():
    pygame.display.set_caption("Pacheesi")
    icon = pygame.image.load("Extream4.png")
    pygame.display.set_icon(icon)


setUpPygame()
pygame.init()

#Nur bei 6 darf eine Figure aus der Base raus gehen
class Game:
    def __init__(self):
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
        diceClicked = self.dice.handleClick(mouseposition)
        #If Dice not Clicked
        if diceClicked == False:
            return
        
        self.currentStage = "rollingDice"
         

    def evalDiceRolling(self):
        allFiguresInBase = self.gamefield.checkAllFiguresInBase(self.currentPlayerNumber)
        if allFiguresInBase:
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
        else:
            self.currentStage = "waitForChoosingFigure"
            
    def handleRollingDice(self):
        print(self.rollingProgress)
        if self.rollingProgress == 0:
            self.dice.rollDice()
            self.rollingProgress += 1
            return
        
        if self.rollingProgress < 100:
            self.rollingProgress += 1
            return
        
        self.evalDiceRolling()        
        self.rollingProgress = 0

    def handleWaitChooseFigure(self, mousePosition):
        if self.gamefield.waitClickFigureToMove(
            mousePosition, self.currentPlayerNumber
        ):
            self.currentStage = "waitingForPlacingFigure"

    def handleWaitForPlacingFigure(self, mousePosition):
        waitClickResult = self.gamefield.waitClickCircleToMoveTo(
                            mousePosition, self.currentPlayerNumber
                        )
        if waitClickResult:
            self.currentStage = "waitingForDice"
            if self.dice.currentValue != 6:
                self.changePlayer()
        else: 
            self.gamefield.waitClickFigureToMove(
                                mousePosition,
                                self.currentPlayerNumber,
                            )
            
            




    def runGame(self):
        gameActive = True

        # Set up timer
        clock = pygame.time.Clock()

        while gameActive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()
                    if self.currentStage == "waitingForDice":
                        self.handleWaitingForDice(mousePosition)
                    if self.currentStage == "waitForChoosingFigure":
                        self.handleWaitChooseFigure(mousePosition)
                    if self.currentStage == "waitingForPlacingFigure":
                        self.handleWaitForPlacingFigure(mousePosition)

            #Gamelogic
            if self.currentStage == "rollingDice":
                self.handleRollingDice()

            # Draw Background
            self.screen.fill(Settings.BACKGROUNDCOLOR)

            # Draw Dice 
            if self.currentStage == "rollingDice":
                self.dice.drawAnimation(self.screen, self.currentPlayerNumber, self.rollingProgress)
            else: 
                self.dice.draw(self.screen, self.currentPlayerNumber)

            # Draw GameField
            self.gamefield.draw(self.screen)

            # Update Display
            pygame.display.flip()

            # Setup refreshtimer
            clock.tick(60)

        pygame.quit()





    def runGameOld(self):
        # Create Objects
        screen = pygame.display.set_mode(
            (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.RESIZABLE
        )
        dice = Dice()
        gamefield = GameField()

        gameActive = True
        currentPlayerNumber = 0

        diceTries = 0
        diceStatus = "static"
        diceAnimationCounter = 0

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
                                    currentPlayerNumber, 4
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
                                currentPlayerNumber, 4
                            )
                        elif waitClickResult and dice.currentValue == 6:
                            currentStage = 0
                        elif waitClickResult == False:
                            gamefield.waitClickFigureToMove(
                                mousePosition,
                                currentPlayerNumber,
                                dice.currentValue,
                            )
                            currentStage = 1
                elif event.type == VIDEORESIZE:
                    Settings.adjustSettings(event.dict["size"])
            # Gamelogic

            # Draw Structures and Figures
            screen.fill(Settings.BACKGROUNDCOLOR)

            # Draw Dice
            if diceStatus == "rolling":
                dice.drawAnimation(screen, currentPlayerNumber, diceAnimationCounter)
                diceAnimationCounter += 1
                if diceAnimationCounter == 100:
                    diceStatus = "static"
            elif diceStatus == "static":
                dice.draw(screen, currentPlayerNumber)

            gamefield.draw(screen)

            self.drawCurrentPlayer(currentPlayerNumber, screen)

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()

    def runGameOlder(self):
        # Create Objects
        screen = pygame.display.set_mode(
            (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.RESIZABLE
        )
        dice = Dice()
        gamefield = GameField()

        gameActive = True

        currentStage = "waiting"
        currentPlayerNumber = 0
        previouslyRoled = False

        diceTries = 0
        diceStatus = "rolling"
        diceAnimationCounter = 0

        # Wir haben 3 Phasen in einem Zug:
        # 0: nicht gewürfelt, 1: gewürfelt und nun wird Figur ausgewählt, 2: Figur wurde gezogen
        # bei einer 6 wird am Ende auf 0 zurückgesetzt

        

        # Set up timer
        clock = pygame.time.Clock()

        while gameActive:
            screen.fill(Settings.BACKGROUNDCOLOR)
            # UserInteraction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False

            if diceStatus == "rolling":
                dice.rollDice()
                diceAnimationCounter += 1
                if diceAnimationCounter == 100:
                    diceStatus = "static"
                    previouslyRoled = True
            elif diceStatus == "static":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousePosition = pygame.mouse.get_pos()
                        if currentStage == "waiting":
                            #If Dice is clicked
                            if dice.handleClick(mousePosition):
                                if previouslyRoled == False:
                                    diceStatus =="rolling"
                                allFiguresInBase = gamefield.checkAllFiguresInBase(currentPlayerNumber)
                                if allFiguresInBase:
                                    if dice.currentValue == 6:
                                        #Player can bring figure out of base
                                        currentStage = "choosingFigure"
                                        diceTries = 0
                                        previouslyRoled = False
                                    elif diceTries < 2:
                                        #player can reroll
                                        diceTries += 1
                                        diceStatus = "rolling"
                                        diceAnimationCounter = 0
                                    else:
                                        currentPlayerNumber = self.changePlayer(currentPlayerNumber)
                                        diceTries = 0
                                else:
                                    currentStage = "choosingFigure"
                                    diceStatus = "rolling"
                                    diceAnimationCounter = 0
                                    diceTries = 0
                                    previouslyRoled = False
                        elif currentStage == "choosingFigure":
                            if gamefield.waitClickFigureToMove(
                                mousePosition, currentPlayerNumber, dice.currentValue
                            ):
                                currentStage = "placeFigure"
                        elif currentStage == "placeFigure":
                            waitClickResult = gamefield.waitClickCircleToMoveTo(
                                mousePosition, currentPlayerNumber
                            )
                            if waitClickResult and dice.currentValue != 6:
                                currentStage = 0
                                currentPlayerNumber = self.changePlayer(currentPlayerNumber)
                            elif waitClickResult and dice.currentValue == 6:
                                currentStage = 0
                            elif waitClickResult == False:
                                gamefield.waitClickFigureToMove(
                                    mousePosition,
                                    currentPlayerNumber,
                                    dice.currentValue,
                                )
                                currentStage = 1
    
            # Gamelogic
            # Draw Structures and Figures
            screen.fill(Settings.BACKGROUNDCOLOR)

            # Draw Dice
            if diceStatus == "rolling":
                dice.drawAnimation(screen, currentPlayerNumber, diceAnimationCounter)
            elif diceStatus == "static":
                dice.draw(screen, currentPlayerNumber)

            gamefield.draw(screen)

            self.drawCurrentPlayer(currentPlayerNumber, screen)

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()
