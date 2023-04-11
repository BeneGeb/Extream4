from .Player import Player
from screeninfo import get_monitors


class Settings:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
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

    WINDOW_WIDTH = 1142
    WINDOW_HEIGHT = 1008

    COLOR_DISTANCE = 150

    CURRENT_PLAYER_POSITION = (25, 150)

    DICE_POSITION = (10, 10)
    DICE_SIZE = 130

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
