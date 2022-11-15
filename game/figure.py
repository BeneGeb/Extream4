import pygame

pygame.init()

WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)


class Figure:
    def __init__(self, color, team, position):
        self.color = color
        self.team = team
        self.position = position
        self.loadImage(team)

    def loadImage(self, color):
        image = pygame.image.load("Spielfigur_" + color + ".png")
        image = pygame.transform.scale(image, (30, 30))
        self.image = image

    def draw(self, screen):
        x, y = self.position
        pygame.draw.circle(screen, SCHWARZ, (x, y), 24, 0)
        pygame.draw.circle(screen, self.color, (x, y), 22, 0)
        pygame.draw.circle(screen, SCHWARZ, (x, y), 12, 0)
        pygame.draw.circle(screen, WEISS, (x, y), 10, 0)

    def move(self, newPosition):
        self.position = newPosition
