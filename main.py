from _common import matrixDimensionX, matrixDimensionY, minMatrixDimensionY, minMatrixDimensionX, maxMatrixDimensionY
from _common import maxMatrixDimensionX, minAmountOfWalls, maxAmountOfWalls, amountOfWalls
from _common import player1Position1MessageX, player1Position2MessageX, player1Position1MessageY
from _common import player1Position2MessageY, player2Position1MessageY, player2Position1MessageX
from _common import player2Position2MessageX, player2Position2MessageY, invalidPositionMessage
from interface import initInterface, inputAndValidatePreGameParams, defineStartingPostionsForPlayers

if __name__ == '__main__':
    x = y = k = None

    x = inputAndValidatePreGameParams(x, minMatrixDimensionX, maxMatrixDimensionX, matrixDimensionX)
    y = inputAndValidatePreGameParams(y, minMatrixDimensionY, maxMatrixDimensionY, matrixDimensionY)
    k = inputAndValidatePreGameParams(k, minAmountOfWalls, maxAmountOfWalls, amountOfWalls)

    player1Positions = [defineStartingPostionsForPlayers(0, x, 0, y, player1Position1MessageX, player1Position1MessageY, invalidPositionMessage),
                        defineStartingPostionsForPlayers(0, x, 0, y, player1Position2MessageX, player1Position2MessageY, invalidPositionMessage)]
    player2Positions = [defineStartingPostionsForPlayers(0, x, 0, y, player2Position1MessageX, player2Position1MessageY, invalidPositionMessage),
                        defineStartingPostionsForPlayers(0, x, 0, y, player2Position2MessageX, player2Position2MessageY, invalidPositionMessage)]

    initInterface(int(x), int(y), int(k), player1Positions, player2Positions)

