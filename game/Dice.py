import pygame
import random
from .settings import Settings
from pygame import mixer

pygame.init()

# Instantiate mixer
mixer.init()


class Dice:
    def __init__(self):
        self.position = Settings.DICE_POSITION
        self.currentValue = 6
        self.size = Settings.DICE_SIZE
        self.loadImages()
        self.animationValue = 4

    def loadImages(self):
        all_dice = []
        all_dice.append(None)
        for i in range(1, 7):
            nextImage = pygame.image.load(
                "./Images/DiceImages/Würfel_" + str(i) + ".png"
            )
            nextImage = pygame.transform.scale(nextImage, (self.size, self.size))
            all_dice.append(nextImage)
        self.all_dice = all_dice

    def rollDice(self):
        self.currentValue = random.randint(5, 6)
        # self.currentValue = 6
        return self.currentValue

    def drawRectAroundDice(self, screen, currentPlayerNumber):
        positionY = self.position[0]
        positionX = self.position[1]
        position = (positionY - 4, positionX - 4)
        pygame.draw.rect(
            screen,
            Settings.listPlayers[currentPlayerNumber].color,
            position + (139, 139),
            border_radius=25,
            width=5,
        )

    def draw(self, screen, currentPlayerNumber):
        screen.blit(self.all_dice[self.currentValue], self.position)
        pygame.draw.rect(
            screen,
            Settings.listPlayers[currentPlayerNumber].color,
            self.position + (130, 130),
            border_radius=20,
            width=5,
        )

    def drawAnimation(self, screen, currentPlayerNumber, animationCounter):
        if animationCounter % 8 == 0:
            self.animationValue = random.randint(1, 6)

        screen.blit(self.all_dice[self.animationValue], self.position)
        Dice.drawRectAroundDice(self, screen, currentPlayerNumber)

    def handleClick(self, clickedPos, isKi):
        diceX, diceY = self.position
        clickedX, clickedY = clickedPos

        if (
            diceX <= clickedX <= diceX + self.size
            and diceY <= clickedY <= diceY + self.size
        ) or isKi:
            # Play the music

            Dice_Sound = mixer.Sound("./Sounds/Dice_Sound1.mp3")
            Dice_Sound.play()
            return self.rollDice()

    def getDiceValue(self):
        return self.currentValue
