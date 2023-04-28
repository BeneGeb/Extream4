from .Circle import Circle
from .Figure import Figure
from ..Helper.GameFieldLoader import GameFieldLoader
from ..settings import Settings
import pygame
from pygame import mixer

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

        self.houseStartFields = [40, 10, 20, 30]

    def draw(self, screen):
        for circle in self.allCircles:
            circle.draw(screen)
        for figure in self.allFigures:
            figure.draw(screen)

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
            # wenn circle ein base circle ist und die gewürfelte nummer 1= 6 ist -> nicht anzeigen
            if "base" not in clickedCircle.type or diceValue == 6:
                self.markPossibleFields(playerNumber, diceValue)

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
                    int(clickedFigure.player) != playerNumber
                    and clickedCircle == self.markedCircle
                ):
                    emptyBaseField = self.getEmptyBaseField(
                        clickedFigure.player)
                    self.kickFigure(clickedFigure, emptyBaseField)
                    self.moveFigure(clickedCircle.position)
                    moved = True
                else:
                    moved = False
            else:
                if clickedCircle == self.markedCircle[0]:
                    self.moveFigure(clickedCircle.position)
                    moved = True

        if moved:
            circleBefore, beforeColor = self.markedCircle
            circleBefore.color = beforeColor

        return moved

    def getEmptyBaseField(self, playerNumber):
        emptyBaseCircle = [
            field
            for field in self.allCircles
            if "base-" + str(playerNumber) in field.type and field.manned == False
        ]
        return emptyBaseCircle[0]

    def kickFigure(self, clickedFigure, emptyBaseField):
        clickedFigure.move(emptyBaseField.position)
        emptyBaseField.manned = True

    def moveFigure(self, newPosition):
        self.lastClickedFigure.move(newPosition)
        self.lastClickedCircle.manned = False
        self.lastClickedFigure.innerColor = Settings.UNSELECTED_CIRCLE_COLOR

        self.lastClickedFigure = None
        self.lastClickedFigure = None

        # Sound move
        Move_Sound = mixer.Sound("Aufzeichnungen.mp3")
        Move_Sound.play()

    def getClickedFigure(self, clickedPos):
        for figure in self.allFigures:
            if figure.handleClick(clickedPos):
                return figure

    def getClickedCircle(self, clickedPos):
        for circle in self.allCircles:
            if circle.handleClick(clickedPos):
                return circle

    def checkAllFiguresInBase(self, player):
        baseFields = [
            field
            for field in self.allCircles
            if "base-" + str(player) in field.type and field.manned == True
        ]
        if len(baseFields) == 4:
            return True
        else:
            return False

    def markPossibleFields(self, playerNumber, diceValue):
        self.checkIsMovePossible(playerNumber, diceValue)
        figureCircle = self.lastClickedCircle
        try:
            circleBefore, beforeColor = self.markedCircle
            circleBefore.color = beforeColor
        except:
            dummy = 1
        markedCircle = []
        if "base" in figureCircle.type:
            markedCircle = [
                circle
                for circle in self.allCircles
                if "startField-" + str(playerNumber) in circle.type
            ]
        elif "house" in figureCircle.type:
            print("house")
        else:
            currentFieldNumber = figureCircle.number
            possibleNumber = currentFieldNumber + diceValue
            if possibleNumber >= 40 and playerNumber != 0:
                possibleNumber = possibleNumber - 40
            if (
                possibleNumber >= self.houseStartFields[playerNumber]
                and currentFieldNumber < self.houseStartFields[playerNumber]
            ):
                possibleNumber = possibleNumber - \
                    self.houseStartFields[playerNumber]
                if possibleNumber <= 3:
                    markedCircle = [
                        circle
                        for circle in self.allCircles
                        if circle.number == possibleNumber
                        and "house-" + str(playerNumber) in circle.type
                    ]
            else:
                markedCircle = [
                    circle
                    for circle in self.allCircles
                    if circle.number == possibleNumber
                ]
        self.markedCircle = (markedCircle[0], markedCircle[0].color)
        markedCircle[0].color = Settings.MARKED_FIELD_COLOR

    def devHelper(self, clickedPos):
        for circle in self.allCircles:
            if circle.handleClick(clickedPos):
                return circle

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
            if self.evalPossibleMove(circle, player, diceValue) != None:
                return True

    def evalPossibleMove(self, circle, team, diceValue):
        if "base" in circle.type and diceValue != 6:
            return None
        elif "base" in circle.type and diceValue == 6:
            return [
                circle
                for circle in self.allCircles
                if "startField-" + str(team) in circle.type
            ][0]
        elif "house" in circle.type and (circle.number + diceValue) <= 3:
            return [
                circle
                for circle in self.allCircles
                if circle.number == (circle.number + diceValue)
                and "house-" + str(team) in circle.type
            ][0]
        else:
            possibleNumber = circle.number + diceValue
            if possibleNumber >= 40 and team != 0:
                possibleNumber = possibleNumber - 40
            if (
                possibleNumber >= self.houseStartFields[team]
                and circle.number < self.houseStartFields[team]
            ):
                possibleNumber = possibleNumber - self.houseStartFields[team]
                if possibleNumber <= 3:
                    return [
                        circle
                        for circle in self.allCircles
                        if circle.number == possibleNumber
                        and "house-" + str(team) in circle.type
                    ][0]
                return None
            else:
                return [
                    circle
                    for circle in self.allCircles
                    if circle.number == possibleNumber
                ][0]

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
        return True
