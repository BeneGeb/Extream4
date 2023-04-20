from game.GameField.Circle import Circle
from game.GameField.Figure import Figure
from ..settings import Settings


def placeStartFigures(allCircles):
    allFigures = []
    baseFields = [field for field in allCircles if "base-" in field.type]
    for baseField in baseFields:
        allFigures.append(
            Figure(baseField.color, int(baseField.type[5:]), baseField.position)
        )

    return allFigures


def loadAllCircles():
    allCircles = []
    for circle in loadCentralFields():
        allCircles.append(circle)
    for circle in loadAllTeams():
        allCircles.append(circle)

    return allCircles


def loadCentralFields():
    circles = []
    firstDirections = ["right", "down", "left", "up"]
    secondDirections = ["up", "right", "down", "left"]
    startX, startY = Settings.GAMEFIELD_POSITION

    startX -= 5 * Settings.CIRCLE_DIFFERENCE
    startY -= Settings.CIRCLE_DIFFERENCE

    position = (startX, startY)

    for i in range(0, 4):
        secondColor = 0 if i == 3 else i + 1
        position, resCircles = loadQuarter(
            position,
            firstDirections[i],
            secondDirections[i],
            Settings.listPlayers[i].color,
            Settings.listPlayers[secondColor].color,
            i * 10,
            i,
        )
        for circle in resCircles:
            circles.append(circle)
        position = evalPosition(firstDirections[i], position)

    return circles


def loadQuarter(
    startPosition,
    firstDirection,
    secondDirection,
    startColor,
    secondColor,
    startNumber,
    startTeam,
):
    circles = []
    position = startPosition

    for i in range(startNumber, startNumber + 5):
        if i == startNumber:
            circles.append(
                Circle(startColor, position, "startField-" + str(startTeam), i)
            )
        else:
            position = evalPosition(firstDirection, position)
            circles.append(Circle(Settings.NEUTRAL_FIELD_COLOR, position, "neutral", i))
    startNumber += 5

    basePosition = evalPosition(firstDirection, position)
    houseTeam = startTeam + 1
    if houseTeam == 4:
        houseTeam = 0
    for i in range(3, -1, -1):
        circles.append(Circle(secondColor, basePosition, "house-" + str(houseTeam), i))
        basePosition = evalPosition(secondDirection, basePosition)

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


def loadAllTeams():
    allTeams = []
    startX, startY = Settings.GAMEFIELD_POSITION
    startX -= 5 * Settings.CIRCLE_DIFFERENCE
    startY -= 5 * Settings.CIRCLE_DIFFERENCE
    position = (startX, startY)
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
