
import pickle
from ..settings import Settings


def saveGameState(gameField, currentPlayer):
    dateiname = "Save"

    with open(dateiname, "wb") as datei:
        pickle.dump(gameField, datei)


def loadGameState():

    dateiname = "Save"
    with open(dateiname, "rb") as datei:
        print("halloooo")
        load_object = pickle.load(datei)
        print(load_object.houseStartFields)
