from .settings import Settings
import pygame

pygame.init()


class ClickButton:
    def __init__(self, position, clickFunction, buttonText, backgroundColor):
        self.position = position
        self.dimensions = (Settings.BUTTON_WIDTH, Settings.BUTTON_HEIGHT)
        self.clickFunction = clickFunction
        self.buttonText = buttonText
        self.backgroundColor = backgroundColor

    def isButtonClicked(self, mousePosition):
        x, y = self.position
        width, height = self.dimensions
        mouseX, mouseY = mousePosition
        if x <= mouseX <= x + width and y <= mouseY <= y + height:
            return True

    def draw(self, screen):
        x, y = self.position
        width, height = self.dimensions

        pygame.draw.rect(
            screen,
            self.backgroundColor,
            (
                x,
                y,
                width,
                height,
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
            self.clickFunction()
