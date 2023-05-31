import pygame
from ..Helper.GameFieldLoader import GameFieldLoader
from ..settings import Settings
from pygame import mixer
import os
from ..Helper.GameState import *

pygame.init()

# Instantiate mixer
mixer.init()
# Überprüfung für Base, ob dort noch welche davor stehen


class GameField:
    def __init__(self):
        gfLoader = GameFieldLoader()
        self.allCircles = gfLoader.loadAllCircles()
        self.allFigures = gfLoader.placeStartFigures(self.allCircles)
        self.lastClickedFigure = None
        self.lastClickedCircle = None
        self.markedCircle = None

        self.houseStartFields = [40, 10, 20, 30]
        self.explosion_images = [
            pygame.image.load(os.path.join(f"./Images/ExplosionFrames/frame_{i}.png"))
            for i in range(23)
        ]
        self.explosion_frame_count = 0
        self.explosion_update_count = 0
        self.explosion_update_rate = (
            3  # Adjust this value to control the animation speed
        )
        self.explosion_running = False

    def update_explosion(self):
        self.explosion_images = [
            pygame.image.load(os.path.join(f"./Images/ExplosionFrames/frame_{i}.png"))
            for i in range(23)
        ]
        if self.explosion_running:
            self.explosion_update_count += 1
            if self.explosion_update_count >= self.explosion_update_rate:
                self.explosion_frame_count += 1
                self.explosion_update_count = 0
                if self.explosion_frame_count >= len(self.explosion_images):
                    self.explosion_running = False
                    self.explosion_frame_count = 0
        else:
            self.explosion = None

    def changeGameSound(self, SoundOn):
        if SoundOn:
            pygame.mixer.pause()

        else:
            pygame.mixer.unpause()

    def draw(self, screen):
        self.explosion_images = [
            pygame.image.load(os.path.join(f"./Images/ExplosionFrames/frame_{i}.png"))
            for i in range(23)
        ]

        for circle in self.allCircles:
            circle.draw(screen)
        for figure in self.allFigures:
            figure.draw(screen)

        if self.explosion_running:
            screen.blit(
                self.explosion_images[self.explosion_frame_count],
                ((480 + 960) // 2, (30 + 960) // 2),
            )
            self.update_explosion()

    # region clickHandler

    def getClickedFigure(self, clickedPos):
        for figure in self.allFigures:
            if figure.handleClick(clickedPos):
                return figure

    def getClickedCircle(self, clickedPos):
        for circle in self.allCircles:
            if circle.handleClick(clickedPos):
                return circle

    # endregion
    # region FigureMoving
    def kickFigure(self, clickedFigure, emptyBaseField):
        clickedFigure.move(emptyBaseField.position)
        Explo_Sound = mixer.Sound("./Sounds/Explosion.mp3")
        Explo_Sound.play()

        self.explosion_running = True
        self.explosion_frame_count = 0

    def moveFigure(self, figure, newPosition):
        Move_Sound = mixer.Sound("./Sounds/Move.mp3")
        Move_Sound.play()
        figure.move(newPosition)
        figure.innerColor = Settings.UNSELECTED_CIRCLE_COLOR

        self.lastClickedFigure = None
        self.lastClickedFigure = None

    def kiMoveFigure(self, figure, newPosition, playerNumber):
        matchingFigure = [
            figure for figure in self.allFigures if figure.position == newPosition
        ]
        if len(matchingFigure) > 0:
            self.kickFigure(
                matchingFigure[0], self.getEmptyBaseField(matchingFigure[0].player)
            )
        self.moveFigure(figure, newPosition)

    # endregion
    # region Functions for Round system
    def waitClickFigureToMove(self, clickedPos, playerNumber, diceValue):
        clickedFigure = self.getClickedFigure(clickedPos)
        clickedCircle = None
        clicked = False

        if clickedFigure and int(clickedFigure.player) == playerNumber:
            clicked = True
            clickedCircle = self.getClickedCircle(clickedPos)
            if self.lastClickedFigure:
                self.lastClickedFigure.innerColor = Settings.UNSELECTED_CIRCLE_COLOR
                clickedFigure.innerColor = Settings.SELECTED_CIRCLE_COLOR
            else:
                clickedFigure.innerColor = Settings.SELECTED_CIRCLE_COLOR
            self.lastClickedFigure = clickedFigure
            self.lastClickedCircle = clickedCircle

            self.markPossibleCircle(clickedCircle, playerNumber, diceValue)

        return clicked

    def waitClickCircleToMoveTo(self, clickedPos, playerNumber, diceValue):
        clickedCircle = self.getClickedCircle(clickedPos)
        clickedFigure = None
        moved = False

        if clickedCircle:
            if "base" in self.lastClickedCircle.type and diceValue != 6:
                return False
            clickedFigure = self.getClickedFigure(clickedPos)

            if clickedFigure:
                if (
                    int(clickedFigure.player)
                    != playerNumber
                    # and clickedCircle == self.markedCircle
                ):
                    emptyBaseField = self.getEmptyBaseField(clickedFigure.player)
                    self.kickFigure(clickedFigure, emptyBaseField)
                    self.moveFigure(self.lastClickedFigure, clickedCircle.position)
                    moved = True
                else:
                    moved = False
            else:
                # if clickedCircle == self.markedCircle:
                self.moveFigure(self.lastClickedFigure, clickedCircle.position)
                moved = True

        if moved:
            if self.markedCircle:
                self.markedCircle.marked = False

        return moved

    def getEmptyBaseField(self, playerNumber):
        teamFiguresPositions = [
            figure.position
            for figure in self.allFigures
            if figure.player == playerNumber
        ]
        for field in self.allCircles:
            if (
                "base-" + str(playerNumber) in field.type
                and field.position not in teamFiguresPositions
            ):
                return field

    # endregion
    def checkAllFiguresInBase(self, playerNumber):
        teamFiguresPositions = [
            figure.position
            for figure in self.allFigures
            if figure.player == playerNumber
        ]
        for field in self.allCircles:
            if (
                "base-" + str(playerNumber) in field.type
                and field.position not in teamFiguresPositions
            ):
                return False
        return True

    def markPossibleCircle(self, circle, playerNumber, diceValue):
        if self.markedCircle != None:
            self.markedCircle.marked = False
        markedCircle = self.evalPossibleMove(circle, playerNumber, diceValue)
        if markedCircle:
            markedCircle.marked = True
            self.markedCircle = markedCircle

    # region CheckPossibleMoves
    def checkIsMovePossible(self, player, diceValue):
        allTeamFigures = [
            figure for figure in self.allFigures if figure.player == player
        ]
        for figure in allTeamFigures:
            circle = [
                circle
                for circle in self.allCircles
                if circle.position == figure.position
            ][0]
            newField = self.evalPossibleMove(circle, player, diceValue)
            if newField != None:
                if not self.isFieldManned(newField.position, player):
                    return True
        return False

    def evalPossibleMove(self, circle, team, diceValue):
        possibleNumber = circle.number + diceValue
        if possibleNumber > 39:
            possibleNumber = possibleNumber - 40
        if "base" in circle.type and diceValue != 6:
            return None
        elif "base" in circle.type and diceValue == 6:
            return self.findFieldOnType("startField-" + str(team))
        elif "startField" in circle.type:
            return self.findFieldOnNumber(possibleNumber)
        # Wenn man sich ganz normal bewegt
        elif "neutral" in circle.type and (
            (circle.number + diceValue) < self.houseStartFields[team]
            or circle.number > self.houseStartFields[team]
        ):
            return self.findFieldOnNumber(possibleNumber)
        # Wenn man auf ienem normalen Feld ist aber in ein Haus Feld rein muss
        elif (
            "neutral" in circle.type
            and (circle.number + diceValue) >= self.houseStartFields[team]
            and circle.number < self.houseStartFields[team]
        ):
            houseFieldNumber = (circle.number + diceValue) - self.houseStartFields[team]
            if houseFieldNumber <= 3:
                if self.checkHouseFigures(team, houseFieldNumber):
                    return self.findField(houseFieldNumber, "house-" + str(team))
                else:
                    return None
            return None
        elif "house" in circle.type:
            houseFieldNumber = possibleNumber
            if houseFieldNumber > 3:
                return None
            elif houseFieldNumber <= 3:
                if self.checkHouseFigures(team, houseFieldNumber):
                    return self.findField(houseFieldNumber, "house-" + str(team))
                else:
                    return None

    def isFieldManned(self, position, playerNumber):
        allTeamFiguresPositions = [
            figure.position
            for figure in self.allFigures
            if figure.player == playerNumber
        ]
        matchingField = [
            circle for circle in self.allCircles if circle.position == position
        ]
        if matchingField[0].position in allTeamFiguresPositions:
            return True
        return False

    def checkHouseFigures(self, team, newNumber):
        teamFigures = [figure for figure in self.allFigures if figure.player == team]
        circlesToCheck = [
            circle
            for circle in self.allCircles
            if "house-" + str(team) in circle.type and circle.number <= newNumber
        ]

        for circle in circlesToCheck:
            matchingFigure = [
                figure for figure in teamFigures if figure.position == circle.position
            ]
            if len(matchingFigure):
                return False
        return True

    def findField(self, number, type):
        return [
            circle
            for circle in self.allCircles
            if circle.number == number and type in circle.type
        ][0]

    def findFieldOnType(self, type):
        return [circle for circle in self.allCircles if type in circle.type][0]

    def findFieldOnNumber(self, number):
        return [circle for circle in self.allCircles if circle.number == number][0]

    # endregion

    def checkWin(self, playerNumber):
        teamBaseFields = [
            circle
            for circle in self.allCircles
            if "house-" + str(playerNumber) in circle.type
        ]
        teamFigures = [
            figure for figure in self.allFigures if figure.player == playerNumber
        ]
        for circle in teamBaseFields:
            matchingField = [
                figure for figure in teamFigures if circle.position == figure.position
            ]
            if len(matchingField) == 0:
                return False
        # self.playerNumberCheckCounter(playerNumber)
        self.placementlist = self.placement()
        return True

    def playerNumberCheckCounter(self, playernumber):
        teamBaseFields = [
            circle.position
            for circle in self.allCircles
            if "house-" + str(playernumber) in circle.type
        ]
        teamFigures = [
            figure.position
            for figure in self.allFigures
            if figure.player == playernumber
        ]
        counter = 0
        for entry in teamBaseFields:
            if entry in teamFigures:
                counter += 1
        return counter

    def placement(self):
        placementList = []
        for i in range(4):
            x = self.playerNumberCheckCounter(i)

            placementList.append(x)
        return placementList
