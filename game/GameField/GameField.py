from .Circle import Circle
from .Figure import Figure
from ..Helper.GameFieldLoader import GameFieldLoader


WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GELB = (255, 255, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)


class GameField:
    def __init__(self, numberOfPlayers):
        gfLoader = GameFieldLoader()
        self.allCircles = gfLoader.loadAllCircles(numberOfPlayers)
        self.allFigures = gfLoader.placeStartFigures(self.allCircles)
        self.lastClickedFigure = None
        self.lastClickedCircle = None

    def draw(self, screen):
        for circle in self.allCircles:
            circle.draw(screen)
        for figure in self.allFigures:
            figure.draw(screen)

    def handleClick(self, clickedPos, player, currenStage):
        clickedFigure = None
        clickedCircle = None
        clicked = False

        for circle in self.allCircles:
            if circle.handleClick(clickedPos):
                clickedCircle = circle.handleClick(clickedPos)
                clicked = True

        for figure in self.allFigures:
            if figure.handleClick(clickedPos) and int(figure.player) == player:
                clickedFigure = figure.handleClick(clickedPos)
                clickedFigure.innerColor = SCHWARZ
                clicked = True

        # position der Figur wird geändert
        if isinstance(self.lastClicked, Figure) and isinstance(clickedCircle, Circle):
            self.lastClicked.move(clickedCircle.position)
            self.lastClickedCircle.manned = False

        self.lastClickedCircle = clickedCircle
        self.lastClicked = clickedFigure

        return clicked

    def waitClickFigureToMove(self, clickedPos, playerNumber):
        clickedFigure = self.getClickedFigure(clickedPos)
        clickedCircle = None
        clicked = False

        if clickedFigure and int(clickedFigure.player) == playerNumber:
            clicked = True
            clickedCircle = self.getClickedCircle(clickedPos)
            if self.lastClickedFigure:
                self.lastClickedFigure.innerColor = WEISS
                clickedFigure.innerColor = SCHWARZ
            else:
                clickedFigure.innerColor = SCHWARZ
            self.lastClickedFigure = clickedFigure
            self.lastClickedCircle = clickedCircle

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
        self.lastClickedFigure.innerColor = WEISS

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
