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
        for circle in self.loadAllTeams():
            allCircles.append(circle)

        return allCircles

    def loadHorizontalRows(self):
        circles = []
        startY = 426
        startX = 140
        addiere = 83
        helperX = startX
        j = 0
        for i in range(4):
           startX += addiere
           circles.append(Circle(WEISS, (startX, startY), "neutral",j))
           j += 1
        for i in range(4):
            startY -= addiere
            circles.append(Circle(WEISS, (startX, startY), "neutral",j))
            j += 1
        for i in range(2):
           startX += addiere
           circles.append(Circle(WEISS, (startX, startY), "neutral",j))
           j +=1
        print(j)
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
                circles.append(Circle(color, (x, y), "base-blue",0))
                x += 90
        return circles
