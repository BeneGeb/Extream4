import pygame
import math
from ..settings import Settings

pygame.init()


class Circle:
    def __init__(self, color, position, type, number):
        self.color = color
        self.position = position
        self.type = type
        self.number = number
        self.marked = False

    def handleClick(self, clickedPos):
        clickedX, clickedY = clickedPos
        x, y = self.position

        sqx = (clickedX - x) ** 2
        sqy = (clickedY - y) ** 2

        if math.sqrt(sqx + sqy) < Settings.CIRCLE_SIZE:
            return self
        else:
            return False

    def draw(self, screen):
        x, y = self.position
        if self.marked:
            pygame.draw.circle(
                screen, Settings.BLACK, (x, y), Settings.CIRCLE_SIZE + 3, 0
            )
            pygame.draw.circle(screen, self.color, (x, y), Settings.CIRCLE_SIZE - 3, 0)
        else:
            pygame.draw.circle(screen, self.color, (x, y), Settings.CIRCLE_SIZE, 0)

    def getProgess(self):
        if "base" in self.type:
            return 0
        if "house" in self.type:
            return self.number + 40 + 1
        else:
            progress = self.number - 30 + 1
            if progress <= 0:
                return 40 - 30 + self.number + 1
            return progress
