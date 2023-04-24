from game.Game import Game
from game.Window import Window
from game.settings import Settings
from game.Window_End import Window_Finished


def startWindow():
    Window(startGame)


def startGame():
    Game(startEndWindow)


def startEndWindow():
    Window_Finished(startWindow)


if __name__ == "__main__":
    Settings.setUpSettings()
    startWindow()
