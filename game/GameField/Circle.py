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
        if "base" in type:
            self.manned = True
        else:
            self.manned = False

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
        pygame.draw.circle(screen, self.color, (x, y), Settings.CIRCLE_SIZE, 0)