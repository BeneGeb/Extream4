import pygame

pygame.init()


class Figure:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, (255, 140, 0), pygame.Rect(x, y, 60, 60))

    def move(self, newPosition):
        self.position = newPosition
