from .Player import Player


class Settings:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    BACKGROUNDCOLOR = (155, 155, 155)

    CIRCLE_DIFFERENCE = 60

    GAMEFIELD_POSITION = (223, 85)

    UNSELECTED_CIRCLE_COLOR = WHITE
    SELECTED_CIRCLE_COLOR = BLACK

    listPlayers = [
        Player(RED, "Bene", False),
        Player(YELLOW, "Yichen", False),
        Player(BLUE, "Samuel", False),
        Player(GREEN, "Pascal", False),
    ]
    NEUTRAL_FIELD_COLOR = WHITE

    WINDOW_WIDTH = 1142
    WINDOW_HEIGHT = 1008

    CURRENT_PLAYER_POSITION = (25, 150)

    DICE_POSITION = (10, 10)
    DICE_SIZE = 130
