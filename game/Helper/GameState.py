import pickle
from ..settings import Settings

filePath = "lastSavedGame"


class GameState:
    def saveGameState(self, gameField, currentPlayer, listPlayers):

        self.gameField = gameField
        self.gameField.explosion_images = None
        self.currentPlayer = currentPlayer
        self.listPlayers = listPlayers

        with open(filePath, "wb") as datei:
            pickle.dump(self, datei)

    def loadGameState(self):

        with open(filePath, "rb") as datei:
            load_object = pickle.load(datei)
        return load_object
