import pygame

pygame.init()


class Circle:
    def __init__(self, color, position, type,number):
        self.color = color
        self.position = position
        self.type = type
        self.number = number

    def draw(self, screen):
        x, y = self.position
        pygame.draw.circle(screen, self.color, (x, y), 30, 0)
