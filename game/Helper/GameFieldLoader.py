from game.GameField.Circle import Circle
from game.GameField.Figure import Figure
from ..settings import Settings


def placeStartFigures(allCircles):
    allFigures = []
    baseFields = [field for field in allCircles if "base-" in field.type]
    for baseField in baseFields:
        allFigures.append(
            Figure(baseField.color, baseField.type[5:], baseField.position)
        )

    return allFigures


def loadAllCircles(numberOfPlayers):
    allCircles = []
    for circle in loadNeutralFields():
        allCircles.append(circle)
    for circle in loadAllTeams(numberOfPlayers):
        allCircles.append(circle)
    for circle in Homefield_horizontal():
        allCircles.append(circle)
    for circle in Homefield_vertikal():
        allCircles.append(circle)

    return allCircles


def loadNeutralFields():
    circles = []
    startY = 426
    startX = 140
    addiere = 83
    j = 0

    for i in range(5):
        startX += addiere
        if i == 0:
            circles.append(
                Circle(Settings.listPlayers[0].color, (startX, startY), "neutral", j)
            )
            j += 1
            continue
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (startX, startY), "neutral", j)
        )
        j += 1
    for i in range(4):
        startY -= addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (startX, startY), "neutral", j)
        )
        j += 1
    for i in range(2):
        startX += addiere
        if i == 1:
            circles.append(
                Circle(Settings.listPlayers[1].color, (startX, startY), "neutral", j)
            )
            j += 1
            break
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (startX, startY), "neutral", j)
        )
        j += 1
    loadSecondQuarter(startX, startY, addiere, circles, j)

    return circles


def loadSecondQuarter(posi_x, posi_y, addiere, circles, j):
    for i in range(4):
        posi_y += addiere
        circles.append(
            Circle(
                Settings.NEUTRAL_FIELD_COLOR,
                (posi_x, posi_y),
                "neutral",
                j,
            )
        )
        j += 1
    for i in range(4):
        posi_x += addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1
    for i in range(2):
        posi_y += addiere
        if i == 1:
            circles.append(
                Circle(Settings.listPlayers[2].color, (posi_x, posi_y), "neutral", j)
            )
            j += 1
            break
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1

    loadThirdQuarter(posi_x, posi_y, addiere, circles, j)


def loadThirdQuarter(posi_x, posi_y, addiere, circles, j):
    for i in range(4):
        posi_x -= addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1
    for i in range(4):
        posi_y += addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1
    for i in range(2):
        posi_x -= addiere
        if i == 1:
            circles.append(
                Circle(Settings.listPlayers[3].color, (posi_x, posi_y), "neutral", j)
            )
            j += 1
            break
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1

    loadFourthQuarter(posi_x, posi_y, addiere, circles, j)


def loadFourthQuarter(posi_x, posi_y, addiere, circles, j):
    for i in range(4):
        posi_y -= addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1
    for i in range(4):
        posi_x -= addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1
    for i in range(1):
        posi_y -= addiere
        circles.append(
            Circle(Settings.NEUTRAL_FIELD_COLOR, (posi_x, posi_y), "neutral", j)
        )
        j += 1


def Homefield_horizontal():
    circles = []
    start_X = 223
    start_Y = 509
    blue = 3
    red = 0
    for i in range(9):
        start_X += 83
        if i < 4:
            circles.append(
                Circle(
                    Settings.listPlayers[0].color, (start_X, start_Y), "house-0", red
                )
            )
            red += 1
        if i > 4:
            circles.append(
                Circle(
                    Settings.listPlayers[2].color, (start_X, start_Y), "house-2", blue
                )
            )
            blue -= 1
    return circles


def Homefield_vertikal():
    circles = []
    start_X = 638
    start_Y = 94
    yellow = 0
    green = 3
    for i in range(9):
        start_Y += 83
        if i < 4:
            circles.append(
                Circle(
                    Settings.listPlayers[1].color, (start_X, start_Y), "house-1", yellow
                )
            )
            yellow += 1
        if i > 4:
            circles.append(
                Circle(
                    Settings.listPlayers[3].color, (start_X, start_Y), "house-3", green
                )
            )
            green -= 1
    return circles


def loadAllTeams(numberOfPlayers):
    allTeams = []
    for player in range(0, numberOfPlayers):
        if player == 0:
            for circle in loadTeam((223, 85), Settings.listPlayers[0].color, player):
                allTeams.append(circle)
        if player == 1:
            for circle in loadTeam((963, 85), Settings.listPlayers[1].color, player):
                allTeams.append(circle)
        if player == 2:
            for circle in loadTeam((963, 825), Settings.listPlayers[2].color, player):
                allTeams.append(circle)
        if player == 3:
            for circle in loadTeam((223, 825), Settings.listPlayers[3].color, player):
                allTeams.append(circle)

    return allTeams


def loadTeam(startPosition, color, team):
    circles = []
    x, y = startPosition
    number = 0
    y -= 90
    helperX = x

    for i in range(2):
        y += 90
        x = helperX
        for j in range(2):
            circles.append(Circle(color, (x, y), "base-" + str(team), number))
            x += 90
            number += 1
    return circles


class GameFieldLoader:
    placeStartFigures = staticmethod(placeStartFigures)
    loadAllCircles = staticmethod(loadAllCircles)
