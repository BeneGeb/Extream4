import pygame
from .Circle import Circle

WEISS = (255, 255, 255)


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
                    circles.append(Circle(WEISS, (startX, startY)))
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
                    circles.append(Circle(WEISS, (startX, startY)))
                startY += 83

        return circles
