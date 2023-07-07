import pygame
from .settings import Settings


class TextBox:
    def __init__(self, text, position, visible):
        self.text = text
        self.lines = self.generateSprites()
        self.position = position
        self.visible = visible

    def generateSprites(self):
        lines = []
        current_string = ""

        for char in self.text:
            if char == "\n":
                # Wenn das Zeichen "\n" erreicht wird, füge den aktuellen Teilstring zur Liste hinzu
                lines.append(current_string)
                current_string = ""  # Setze den Teilstring zurück
            else:
                current_string += char

        if current_string != "":
            lines.append(current_string)

        txts = []
        for line in lines:
            # Schriftgröße
            font = pygame.font.Font(None, 30)
            txt = font.render(line, True, Settings.BLACK)
            txts.append(txt)
        return txts

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(
            screen,
            Settings.WHITE,
            (x - 5, y - 20, 450, len(self.lines) * 25 + 40),
            border_radius=20,
        )
        if self.visible:
            for i, line in enumerate(self.lines):
                # Zeilenabstand
                screen.blit(line, (x, y + 25 * i))
