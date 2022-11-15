import pygame
from .Circle import Circle

WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GELB = (255, 255, 0)
GRUEN = (0, 255, 0)
BLAU = (0, 0, 255)


class GameField:
    def __init__(self):
        self.allCircles = self.loadAllCircles()

    def draw(self, screen):
        for circle in self.allCircles:
            circle.draw(screen)

    def handleClick(self, clickedPos):
        for circle in self.allCircles:
            circle.handleClick(clickedPos)

    def loadAllCircles(self):
        allCircles = []
        for circle in self.loadHorizontalRows():
            allCircles.append(circle)
        for circle in self.loadAllTeams():
            allCircles.append(circle)

        return allCircles

    def loadNeutralFieldss(self):
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
            circles.append(Circle(WEISS, (posi_x, posi_y), "neutral", j))
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
        print(j)

    def loadAllTeams(self):
        allTeams = []
        for circle in self.loadTeam((223, 85), ROT):
            allTeams.append(circle)
        for circle in self.loadTeam((963, 85), GELB):
            allTeams.append(circle)
        for circle in self.loadTeam((223, 825), GRUEN):
            allTeams.append(circle)
        for circle in self.loadTeam((963, 825), BLAU):
            allTeams.append(circle)

        return allTeams

    def loadTeam(self, startPosition, color):
        circles = []
        x, y = startPosition

        y -= 90
        helperX = x

        for i in range(2):
            y += 90
            x = helperX
            for j in range(2):
                circles.append(Circle(color, (x, y), "base-blue", 0))
                x += 90
        return circles
