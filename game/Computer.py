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
        matchingFigure = [
            figure
            for circle, figure in allMannedCirclesAndFigures
            if circle.number == fieldNumber and "house" not in circle.type
        ]
        return matchingFigure[0]

    def getFieldFromPosition(self, position, allMannedCirclesAndFigures):
        machingField = [
            circle
            for circle, figure in allMannedCirclesAndFigures
            if circle.position == position
        ]
        return machingField[0]

    def getFieldFromNumber(self, number, allCircles):
        matchingField = [circle for circle in allCircles if circle.number == number]
        return matchingField[0]

    # Es wird folgende Priorität für das Verhalten des computers gesetzt
    # 1. Wenn eine Figure auf dem Startfeld steht wird diese wegbewegt
    # 2. Wenn eine 6 gewürfelt wird, wird eine Figur aus der Base bewegt
    # 3. Die am weitesten vorne stehende Figur wird bewegt
    def evalNextMove(self, gameField, diceValue):
        allTeamFigures = self.getAllFigures(gameField.allFigures)
        allMannedCirclesAndFigures = self.getMannedCircles(
            gameField.allCircles, allTeamFigures
        )
        allMannedCirclesAndFigures = self.sortFigures(allMannedCirclesAndFigures)
        figureInBase = [
            figure
            for circle, figure in allMannedCirclesAndFigures
            if "base" in circle.type
        ]

        # Ist eine eigene Figur auf dem Startfield
        if self.isFieldManned(allMannedCirclesAndFigures, self.startField.position):
            figureToMove = self.getFigureFromFieldNumber(
                self.startField.number, allMannedCirclesAndFigures
            )
            newField = self.getFieldFromNumber(
                self.startField.number + diceValue, gameField.allCircles
            )
            if not self.isFieldManned(allMannedCirclesAndFigures, newField.position):
                gameField.kiMoveFigure(
                    figureToMove, newField.position, self.playerNumber
                )
        # Ist eine Figur in der Base und ein Startfeld frei
        elif (
            len(figureInBase) > 1
            and not self.isFieldManned(
                allMannedCirclesAndFigures, self.startField.position
            )
            and diceValue == 6
        ):
            gameField.kiMoveFigure(
                figureInBase[0], self.startField.position, self.playerNumber
            )
        # Es wird wenn möglich die vorderste Figur bewegt
        # Fehlt noch die Berechnung des nächsten Feldes
        else:
            currCircle, currFigure = allMannedCirclesAndFigures[0]
            newField = self.getNextField(currCircle, diceValue, gameField.allCircles)
            gameField.kiMoveFigure(currFigure, newField.position, self.playerNumber)

    def getNextField(self, currCircle, diceValue, allCircles):
        if currCircle.number + diceValue > 39:
            number = currCircle.number + diceValue - 39
            return self.getFieldFromNumber(number, allCircles)
        return self.getFieldFromNumber(currCircle.number + diceValue, allCircles)

    def sortFigures(self, allMannedCirclesAndFigures):
        allMannedCirclesAndFigures.sort(
            key=lambda entry: self.getProgess(entry[0]), reverse=True
        )
        return allMannedCirclesAndFigures

    def getProgess(self, circle):
        if "base" in circle.type:
            return 0
        if "house" in circle.type:
            return circle.number + 40 + 1
        else:
            progress = circle.number - self.startField.number + 1
            if progress <= 0:
                return 40 - self.startField.number + circle.number + 1
            return progress

    def isFieldManned(self, allMannedCircles, position):
        matchingField = [
            circle for circle, figure in allMannedCircles if circle.position == position
        ]
        if len(matchingField) > 0:
            return True
        else:
            return False
