import pygame
import math

pygame.init()

WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)


class Figure:
    def __init__(self, color, team, position):
        self.color = color
        self.team = team
        self.position = position

    def draw(self, screen):
        x, y = self.position
        pygame.draw.circle(screen, SCHWARZ, (x, y), 24, 0)
        pygame.draw.circle(screen, self.color, (x, y), 22, 0)
        pygame.draw.circle(screen, SCHWARZ, (x, y), 12, 0)
        pygame.draw.circle(screen, WEISS, (x, y), 10, 0)

    def move(self, newPosition):
        self.position = newPosition

    def handleClick(self, clickedPos):
        clickedX, clickedY = clickedPos
        x, y = self.position

        sqx = (clickedX - x) ** 2
        sqy = (clickedY - y) ** 2

        if math.sqrt(sqx + sqy) < 22:
            return self
        else:
            return
