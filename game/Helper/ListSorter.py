def sortPlayers(allCircles, allFigures, allPlayers):
    playerList = []
    for i, player in enumerate(allPlayers):
        playerfigures = [figure for figure in allFigures if figure.player == i]
        mannedCircles = getMannedCircles(allCircles, playerfigures)
        progress = getProgressForOnePlayer(mannedCircles, player.startfield)
        entry = (player, progress)
        print(entry)
        playerList.append(entry)
    playerList.sort(key=lambda entry: entry[1], reverse=True)
    return playerList


def getProgressForOnePlayer(allCircles, startField):
    progress = 0
    for circle in allCircles:
        progress = progress + getProgessOneFigure(circle, startField)
    return progress


def getProgessOneFigure(circle, startField):
    if "base" in circle.type:
        return 0
    if "house" in circle.type:
        return circle.number + 40 + 1
    else:
        progress = circle.number - startField + 1
        if progress <= 0:
            return 40 - startField + circle.number + 1
        return progress


def getMannedCircles(allCircles, allTeamFigures):
    mannedCircles = []
    for figure in allTeamFigures:
        circle = [
            circle for circle in allCircles if circle.position == figure.position
        ][0]
        mannedCircles.append(circle)
    return mannedCircles
