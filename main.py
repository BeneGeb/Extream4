from game.Game import Game
from game.Window import Window
from game.settings import Settings
from game.Window_End import Window_Finished


def startWindow():
    Window(startGame)


def startGame():
    Game(startEndWindow)


def startEndWindow(placement):
    Window_Finished(startWindow, placement)


if __name__ == "__main__":
    Settings.setUpSettings()
    startWindow()
