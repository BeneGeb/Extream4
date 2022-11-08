import pygame

pygame.init()


class Figure:
    def __init__(self, team, position):
        self.team = team
        self.position = position
        # self.loadImage(team)

    def loadImage(self, color):
        image = pygame.image.load("Figure_" + color + ".png")
        image = pygame.transform.scale(image)
        self.image = image

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, (255, 140, 0), pygame.Rect(x, y, 60, 60))
        # screen.blit(self.image, (x,y))

    def move(self, newPosition):
        self.position = newPosition
