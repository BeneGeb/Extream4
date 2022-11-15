import pygame
import math

pygame.init()


class Circle:
    def __init__(self, color, position, type, number):
        self.color = color
        self.position = position
        self.type = type
        self.number = number
        if "base" in type:
            self.manned = False
        else:
            self.manned = True

    def handleClick(self, clickedPos):
        clickedX, clickedY = clickedPos
        x, y = self.position

        sqx = (clickedX - x) ** 2
        sqy = (clickedY - y) ** 2

        if math.sqrt(sqx + sqy) < 30:
            return self
        else:
            return

    def draw(self, screen):
        x, y = self.position
        pygame.draw.circle(screen, self.color, (x, y), 30, 0)
