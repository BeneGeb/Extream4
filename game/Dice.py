import pygame
import random

pygame.init()


class Dice:
    def __init__(self, position, size):
        self.position = position
        self.currentValue = 6
        self.size = size
        self.loadImages()
        self.animationValue = 4

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
        return self.currentValue

    def draw(self, screen):
        screen.blit(self.all_dice[self.currentValue], self.position)

    def drawAnimation(self, screen, animationCounter):
        if animationCounter % 8 == 0:
            self.animationValue = random.randint(1, 6)

        screen.blit(self.all_dice[self.animationValue], self.position)

    def handleClick(self, clickedPos):
        diceX, diceY = self.position
        clickedX, clickedY = clickedPos

        if (
            diceX <= clickedX <= diceX + self.size
            and diceY <= clickedY <= diceY + self.size
        ):
            return self.rollDice()

    def getDiceValue(self):
        return self.currentValue
