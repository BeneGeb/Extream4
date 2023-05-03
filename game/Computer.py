class Computer:
    def __init__(self, playerNumber, gameField):
        self.playerNumber = playerNumber
        self.startField = [
            circle
            for circle in gameField.allCircles
            if "startField-" + str(playerNumber) in circle.type
        ][0]

    def getAllFigures(self, allFigures):
        return [figure for figure in allFigures if figure.player == self.playerNumber]

    def getMannedCircles(self, allCircles, allTeamFigures):
        mannedCircles = []
        for figure in allTeamFigures:
            circle = [
                circle for circle in allCircles if circle.position == figure.position
            ][0]
            mannedCircles.append((circle, figure))
        return mannedCircles

    def getFigureFromFieldNumber(self, fieldNumber, allMannedCirclesAndFigures):
        matchingField = [
            figure
            for circle, figure in allMannedCirclesAndFigures
            if circle.number == fieldNumber and "house" not in circle.type
        ]
        return matchingField[0]

    def evalNextMove(self, gameField, diceValue):
        allTeamFigures = self.getAllFigures(gameField.allFigures)
        allMannedCirclesAndFigures = self.getMannedCircles(
            gameField.allCircles, allTeamFigures
        )

        figureInBase = [
            figure
            for circle, figure in allMannedCirclesAndFigures
            if "base" in circle.type
        ]
        if len(figureInBase) > 1 and not self.isFieldManned(
            allMannedCirclesAndFigures, self.startField.position
        ):
            gameField.moveFigure(figureInBase[0], self.startField.position)
        elif self.isFieldManned(allMannedCirclesAndFigures, self.startField.position):
            figure = self.getFigureFromFieldNumber(
                self.startField.position, allMannedCirclesAndFigures
            )
            print(figure)
            # gameField.moveFigure()

    def isFieldManned(self, allMannedCircles, position):
        matchingField = [
            circle for circle, figure in allMannedCircles if circle.position == position
        ]
        if len(matchingField) > 0:
            return True
        else:
            return False
