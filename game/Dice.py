import pygame
import random

pygame.init()


class Dice:
    def __init__(self, screen, position, size):
        self.screen = screen
        self.position = position
        self.currentValue = 6
        self.size = size
        self.loadImages()

    def loadImages(self):
        all_dice = []
        all_dice.append(None)
        for i in range(1, 7):
            nextImage = pygame.image.load("Würfel_" + str(i) + ".png")
            nextImage = pygame.transform.scale(nextImage, (self.size, self.size))
            all_dice.append(nextImage)
        self.all_dice = all_dice

    def rollDice(self):
        self.currentValue = random.randint(1, 6)

    def draw(self):
        self.screen.blit(self.all_dice[self.currentValue], (0, 0))

    def handleClick(self, clickedPos):
        diceX, diceY = self.position
        clickedX, clickedY = clickedPos

        if (
            diceX <= clickedX <= diceX + self.size
            and diceY <= clickedY <= diceY + self.size
        ):
            self.rollDice()

    def getDiceValue(self):
        return self.currentValue


screen = pygame.display.set_mode((1000, 1000))
dice = Dice(screen, (0, 0), 200)
gameActive = True

dice1 = pygame.image.load("Würfel_1.png")
dice1 = pygame.transform.scale(dice1, (100, 100))

clock = pygame.time.Clock()

while gameActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameActive = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dice.rollDice()
        elif event.type == pygame.MOUSEBUTTONUP:
            dice.handleClick(pygame.mouse.get_pos())

    dice.draw()
    pygame.display.flip()
    clock.tick(60)
