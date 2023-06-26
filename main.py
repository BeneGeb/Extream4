from game.Game import Game
from game.Window_new import Window
from game.settings import Settings
from game.Window_End import Window_Finished
from game.Window_Ragequit import Window_RageQuit


def startWindow():
    Window(startGame)


def startGame(loadedState=None, sameColorMode=None):
    Game(startEndWindow, loadedState, sameColorMode)


def startEndWindow(placement, gameField):
    Window_Finished(startWindow, placement, gameField)


def startRagequitWindow():
    Window_RageQuit(startWindow)


if __name__ == "__main__":
    Settings.setUpSettings()
    startWindow()
