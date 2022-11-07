import pygame
import random

pygame.init()


class Dice():
    def __init__(self,screen, position):
        self.screen = screen
        self.position = position
        self.currentValue = 1
        self.loadImages()
        

    def loadImages(self):
        all_dice = []
        for i in range(1,7):
            nextImage = pygame.image.load("Würfel_" + str(i) + ".png")
            print("Würfel_" + str(i) + ".png")
            nextImage = pygame.transform.scale(nextImage, (100,100))
            all_dice.append(nextImage)
        self.all_dice = all_dice

    def rollDice(self):
        dice  = random.randint( 1, 6 )
        return dice

    def draw(self):
        print(self.currentValue)
        self.screen.blit(self.all_dice[self.currentValue], self.position)

        


    
screen = pygame.display.set_mode((1000, 1000))
dice = Dice(screen, (0,0))

while True:
    dice.draw()

