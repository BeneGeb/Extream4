from .settings import Settings
import pygame
from pygame import mixer

pygame.init()
mixer.init()


class ClickButton:
    def __init__(self, position, clickFunction, buttonText, backgroundColor, size=None, visible=True):
        self.position = position
        if size == None:
            self.dimensions = (Settings.BUTTON_WIDTH, Settings.BUTTON_HEIGHT)
        else:
            self.dimensions = size
        self.clickFunction = clickFunction
        self.visible = visible
        self.buttonText = buttonText
        self.backgroundColor = backgroundColor
        self.animationCounter = 0

    def isButtonClicked(self, mousePosition):
        x, y = self.position
        width, height = self.dimensions
        mouseX, mouseY = mousePosition
        if x <= mouseX <= x + width and y <= mouseY <= y + height:
            return True

    def draw(self, screen):
        if not self.visible:
            return
        x, y = self.position
        width, height = self.dimensions

        if self.animationCounter > 0:
            self.animationCounter = self.animationCounter - 0.2
        else:
            self.animationCounter = 0
        pygame.draw.rect(
            screen,
            self.backgroundColor,
            (
                x + self.animationCounter,
                y + self.animationCounter,
                width - self.animationCounter * 2,
                height - self.animationCounter * 2,
            ),
            border_radius=20,
        )
        small_font = pygame.font.SysFont("comicsansms", 25)
        text = small_font.render(self.buttonText, True, Settings.BLACK)
        text_x = x + (width - text.get_width()) // 2
        text_y = y + (height - text.get_height()) // 2
        screen.blit(text, (text_x, text_y))

    def handleClick(self, mousePosition):
        if self.isButtonClicked(mousePosition):
            Button_Sound = mixer.Sound("./Sounds/Menü_Klick_Sound3.mp3")
            Button_Sound.play()
            self.animationCounter = 2
            self.clickFunction(self)
