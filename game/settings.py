from .Player import Player
from screeninfo import get_monitors


class Settings:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    ORANGE = (255, 165, 0)
    GRAY = (128, 128, 128)
    DARKGRAY = (89, 89, 89)
    BACKGROUNDCOLOR = (155, 155, 155)

    CIRCLE_DIFFERENCE = 80
    CIRCLE_SIZE = 30

    FIGURE_SIZE = 28

    GAMEFIELD_POSITION = (970, 500)

    UNSELECTED_CIRCLE_COLOR = WHITE
    SELECTED_CIRCLE_COLOR = BLACK

    listPlayers = [
        Player(RED, "Player 1", False),
        Player(YELLOW, "Player 2", False),
        Player(BLUE, "Player 3", False),
        Player(GREEN, "Player 4", False),
    ]
    NEUTRAL_FIELD_COLOR = WHITE
    MARKED_FIELD_COLOR = ORANGE

    WINDOW_WIDTH = 1142
    WINDOW_HEIGHT = 1008

    COLOR_DISTANCE = 100

    CURRENT_PLAYER_POSITION = (90, 210)

    DICE_POSITION = (80, 60)
    DICE_SIZE = 130

    RECT_x_Position = 45
    RECT_y_Position = 300
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 60

    def setUpSettings():
        monitor = [monitor for monitor in get_monitors() if monitor.is_primary]
        Settings.WINDOW_WIDTH = monitor[0].width
        Settings.WINDOW_HEIGHT = monitor[0].height - 63

        Settings.GAMEFIELD_POSITION = (
            monitor[0].width // 2,
            (monitor[0].height - 63) // 2,
        )

    def adjustSettings(size):
        Settings.WINDOW_WIDTH = size[0]
        Settings.WINDOW_HEIGHT = size[1]

        Settings.GAMEFIELD_POSITION = (
            size[0] // 2,
            (size[1] - 63) // 2,
        )
