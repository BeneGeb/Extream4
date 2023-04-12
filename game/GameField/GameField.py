from .Circle import Circle
from .Figure import Figure
from ..Helper.GameFieldLoader import GameFieldLoader
from ..settings import Settings


class GameField:
    def __init__(self):
        gfLoader = GameFieldLoader()
        self.allCircles = gfLoader.loadAllCircles(4)
        self.allFigures = gfLoader.placeStartFigures(self.allCircles)
        self.lastClickedFigure = None
        self.lastClickedCircle = None

    def draw(self, screen):
        for circle in self.allCircles:
            circle.draw(screen)
        for figure in self.allFigures:
            figure.draw(screen)

    def waitClickFigureToMove(self, clickedPos, playerNumber):
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
            # self.showPossibleMove(clickedFigure, clickedCircle, rolledNumber)

        return clicked

    def waitClickCircleToMoveTo(self, clickedPos, playerNumber):
        clickedCircle = self.getClickedCircle(clickedPos)
        clickedFigure = None
        moved = False

        if clickedCircle:
            clickedFigure = self.getClickedFigure(clickedPos)

            if clickedFigure:
                if int(clickedFigure.player) != playerNumber:
                    emptyBaseField = self.getEmptyBaseField(clickedFigure.player)
                    self.kickFigure(clickedFigure, emptyBaseField)
                    self.moveFigure(clickedCircle.position)
                    moved = True
                else:
                    moved = False
            else:
                self.moveFigure(clickedCircle.position)
                moved = True

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

    def showPossibleMove(self, figure, circle, rolledNumber):
        currentNumber = circle.number
        newNumber = currentNumber + rolledNumber

        if "base" in circle:
            possibleField = [
                field
                for field in self.allCircles
                if field.number == newNumber
                and "base" not in field.type
                and "house" not in field.type
            ]

    def devHelper(self, clickedPos):
        for circle in self.allCircles:
            if circle.handleClick(clickedPos):
                return circle
