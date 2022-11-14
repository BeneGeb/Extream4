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

    def loadAllCircles(self):
        allCircles = []
        for circle in self.loadHorizontalRows():
            allCircles.append(circle)
        for circle in self.loadVerticalColumns():
            allCircles.append(circle)
        for circle in self.loadAllTeams():
            allCircles.append(circle)

        return allCircles

    def loadHorizontalRows(self):
        circles = []
        startY = 343
        startX = 223
        helperX = startX
        for i in range(3):
            startY += 83
            startX = helperX
            for j in range(11):
                if startY != 509 or startX != 638:
                    circles.append(Circle(WEISS, (startX, startY), "neutral"))
                startX += 83

        return circles

    def loadVerticalColumns(self):
        circles = []
        startX = 472
        startY = 94
        helperY = startY
        for i in range(3):
            startX += 83
            startY = helperY
            for j in range(11):
                if startY != 509 or startX != 638:
                    circles.append(Circle(WEISS, (startX, startY), "neutral"))
                startY += 83

        return circles

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
                circles.append(Circle(color, (x, y), "base-blue"))
                x += 90
        return circles
