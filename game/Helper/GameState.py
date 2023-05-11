import pickle
from ..settings import Settings


class GameState:

    def saveGameState(self, gameField, currentPlayer, listPlayers):
        dateiname = "Save"
        self.gameField = gameField
        self.gameField.explosion_images = None
        self.currentPlayer = currentPlayer
        self.listPlayers = listPlayers

        with open(dateiname, "wb") as datei:
            pickle.dump(self, datei)

    def loadGameState(self):

        dateiname = "Save"
        with open(dateiname, "rb") as datei:
            load_object = pickle.load(datei)
            # print(load_object.listPlayers)
        return load_object
