import pygame
from .Circle import Circle
from .Figure import Figure

WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GELB = (255, 255, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)


class GameField:
    def __init__(self, numberOfPlayers):
        self.allCircles = self.loadAllCircles(numberOfPlayers)
        self.allFigures = self.placeStartFigures()
        self.lastClicked = None
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

    def resetLastClickedFigure(self):
        self.lastClickedFigure = None

    def loadAllCircles(self, numberOfPlayers):
        allCircles = []
        for circle in self.loadNeutralFields():
            allCircles.append(circle)
        for circle in self.loadAllTeams(numberOfPlayers):
            allCircles.append(circle)
        for circle in self.Homefield_horizontal():
            allCircles.append(circle)
        for circle in self.Homefield_vertikal():
            allCircles.append(circle)

        return allCircles

    def loadNeutralFields(self):
        circles = []
        startY = 426
        startX = 140
        addiere = 83
        j = 0

        for i in range(5):
            startX += addiere
            if i == 0:
                circles.append(Circle(ROT, (startX, startY), "neutral", j))
                j += 1
                continue
            circles.append(Circle(WEISS, (startX, startY), "neutral", j))
            j += 1
        for i in range(4):
            startY -= addiere
            circles.append(Circle(WEISS, (startX, startY), "neutral", j))
            j += 1
        for i in range(2):
            startX += addiere
            if i == 1:
                circles.append(Circle(GELB, (startX, startY), "neutral", j))
                j += 1
                break
            circles.append(Circle(WEISS, (startX, startY), "neutral", j))
            j += 1
        self.loadSecondQuarter(startX, startY, addiere, circles, j)

        return circles

    def loadSecondQuarter(self, posi_x, posi_y, addiere, circles, j):
        for i in range(4):
            posi_y += addiere
            circles.append(
                Circle(
                    WEISS,
                    (posi_x, posi_y),
                    "neutral",
                    j,
                )
            )
            j += 1
        for i in range(4):
            posi_x += addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1
        for i in range(2):
            posi_y += addiere
            if i == 1:
                circles.append(Circle(BLAU, (posi_x, posi_y), "neutral", j))
                j += 1
                break
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1

        self.loadThirdQuarter(posi_x, posi_y, addiere, circles, j)

    def loadThirdQuarter(self, posi_x, posi_y, addiere, circles, j):
        for i in range(4):
            posi_x -= addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1
        for i in range(4):
            posi_y += addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1
        for i in range(2):
            posi_x -= addiere
            if i == 1:
                circles.append(Circle(GRUEN, (posi_x, posi_y), "neutral", j))
                j += 1
                break
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1

        self.loadFourthQuarter(posi_x, posi_y, addiere, circles, j)

    def loadFourthQuarter(self, posi_x, posi_y, addiere, circles, j):
        for i in range(4):
            posi_y -= addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1
        for i in range(4):
            posi_x -= addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1
        for i in range(1):
            posi_y -= addiere
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
            j += 1

    def Homefield_horizontal(self):
        circles = []
        start_X = 223
        start_Y = 509
        blue = 3
        red = 0
        for i in range(9):
            start_X += 83
            if i < 4:
                circles.append(Circle(ROT, (start_X, start_Y), "house", red))
                red += 1
            if i > 4:
                circles.append(Circle(BLAU, (start_X, start_Y), "house", blue))
                blue -= 1
        return circles

    def Homefield_vertikal(self):
        circles = []
        start_X = 638
        start_Y = 94
        yellow = 0
        green = 3
        for i in range(9):
            start_Y += 83
            if i < 4:
                circles.append(Circle(GELB, (start_X, start_Y), "house", yellow))
                yellow += 1
            if i > 4:
                circles.append(Circle(GRUEN, (start_X, start_Y), "house", green))
                green -= 1
        return circles

    def loadAllTeams(self, numberOfPlayers):
        allTeams = []
        for player in range(0, numberOfPlayers):
            if player == 0:
                for circle in self.loadTeam((223, 85), ROT, player):
                    allTeams.append(circle)
            if player == 1:
                for circle in self.loadTeam((963, 85), GELB, player):
                    allTeams.append(circle)
            if player == 2:
                for circle in self.loadTeam((963, 825), BLAU, player):
                    allTeams.append(circle)
            if player == 3:
                for circle in self.loadTeam((223, 825), GRUEN, player):
                    allTeams.append(circle)

        return allTeams

    def loadTeam(self, startPosition, color, team):
        circles = []
        x, y = startPosition
        number = 0
        y -= 90
        helperX = x

        for i in range(2):
            y += 90
            x = helperX
            for j in range(2):
                circles.append(Circle(color, (x, y), "base-" + str(team), number))
                x += 90
                number += 1
        return circles

    def placeStartFigures(self):
        allFigures = []
        baseFields = [field for field in self.allCircles if "base-" in field.type]
        for baseField in baseFields:
            allFigures.append(
                Figure(baseField.color, baseField.type[5:], baseField.position)
            )

        return allFigures
