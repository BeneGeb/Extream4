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
    for circle in loadAllTeams():
        allCircles.append(circle)
    # for circle in Homefield_horizontal():
    #     allCircles.append(circle)
    # for circle in Homefield_vertikal():
    #     allCircles.append(circle)

    return allCircles


def loadNeutralFields():
    circles = []
    firstDirections = ["right", "down", "left", "up"]
    secondDirections = ["up", "right", "down", "left"]
    settingX, settingY = Settings.GAMEFIELD_POSITION
    settingY += 4 * Settings.CIRCLE_DIFFERENCE
    position = (settingX, settingY)

    for i in range(0, 4):
        position, resCircles = loadQuarter(
            position,
            firstDirections[i],
            secondDirections[i],
            Settings.listPlayers[i].color,
            0,
        )
        for circle in resCircles:
            circles.append(circle)
        position = evalPosition(firstDirections[i], position)

    return circles


def loadQuarter(
    startPosition, firstDirection, secondDirection, startColor, startNumber
):
    circles = []
    position = startPosition

    for i in range(startNumber, startNumber + 5):
        if i == 0:
            circles.append(Circle(startColor, position, "neutral", i))
        else:
            position = evalPosition(firstDirection, position)
            circles.append(Circle(Settings.NEUTRAL_FIELD_COLOR, position, "neutral", i))

    startNumber += 5

    for i in range(startNumber, startNumber + 4):
        position = evalPosition(secondDirection, position)
        circles.append(Circle(Settings.NEUTRAL_FIELD_COLOR, position, "neutral", i))
    startNumber += 4

    position = evalPosition(firstDirection, position)
    circles.append(
        Circle(Settings.NEUTRAL_FIELD_COLOR, position, "neutral", startNumber)
    )

    return (position, circles)


def evalPosition(direction, position):
    posX, posY = position
    if direction == "right":
        posX += Settings.CIRCLE_DIFFERENCE
    if direction == "left":
        posX -= Settings.CIRCLE_DIFFERENCE
    if direction == "up":
        posY -= Settings.CIRCLE_DIFFERENCE
    if direction == "down":
        posY += Settings.CIRCLE_DIFFERENCE

    return (posX, posY)


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


def loadAllTeams():
    allTeams = []
    position = Settings.GAMEFIELD_POSITION
    for i in range(0, 4):
        for circle in loadTeam(position, Settings.listPlayers[i].color, i):
            allTeams.append(circle)
        position = evalTeamPosition(position, i)
    return allTeams


def evalTeamPosition(position, number):
    x, y = position
    if number == 0:
        x += 9 * Settings.CIRCLE_DIFFERENCE
    if number == 1:
        y += 9 * Settings.CIRCLE_DIFFERENCE
    if number == 2:
        x -= 9 * Settings.CIRCLE_DIFFERENCE

    return (x, y)


def loadTeam(startPosition, color, team):
    circles = []
    x, y = startPosition
    number = 0
    y -= Settings.CIRCLE_DIFFERENCE
    helperX = x

    for i in range(2):
        y += Settings.CIRCLE_DIFFERENCE
        x = helperX
        for j in range(2):
            circles.append(Circle(color, (x, y), "base-" + str(team), number))
            x += Settings.CIRCLE_DIFFERENCE
            number += 1
    return circles


class GameFieldLoader:
    placeStartFigures = staticmethod(placeStartFigures)
    loadAllCircles = staticmethod(loadAllCircles)
