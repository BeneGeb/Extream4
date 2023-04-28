class Computer:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber

    def getAllFigures(self, allFigures):
        return [figure for figure in allFigures if figure.player == self.playerNumber]

    def evalNextMove(self, gameField):
        self.allTeamFigure = self.getAllFigures(gameField.allFigures)
