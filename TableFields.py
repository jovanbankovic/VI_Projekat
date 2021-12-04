from _common import matrixDimensionX, matrixDimensionY, minMatrixDimensionY, minMatrixDimensionX, maxMatrixDimensionY
from _common import maxMatrixDimensionX, minAmountOfWalls, maxAmountOfWalls, amountOfWalls
from _common import player1Position1MessageX, player1Position2MessageX, player1Position1MessageY
from _common import player1Position2MessageY, player2Position1MessageY, player2Position1MessageX
from _common import player2Position2MessageX, player2Position2MessageY, invalidPositionMessage
from interface import inputAndValidatePreGameParams, defineStartingPostionsForPlayers
from dict import dict


def calculate_if_field_is_starting_pos(i, j, position):
    for p in position:
        if (i, j) == p:
            return 1
        else:
            return 0


class Field(object):
    index: ()
    is_starting_position_player1: bool(False)
    is_starting_position_player2: bool(False)
    is_occupied_by_player1: bool(False)
    is_occupied_by_player2: bool(False)
    wallList: []

    def __init__(self, i, j, player1_starting_position, player2_starting_position):
        self.is_starting_position_player1 = bool(calculate_if_field_is_starting_pos(i, j, player1_starting_position))
        self.is_starting_position_player2 = bool(calculate_if_field_is_starting_pos(i, j, player2_starting_position))
        self.index = (i, j)
        self.is_occupied_by_player1 = bool(False)
        self.is_occupied_by_player2 = bool(False)
        self.wallList = []

    def set_field(self, index, is_starting_position_player1, is_starting_position_player2,
                  is_occupied_by_player1, is_occupied_by_player2, wall_list):
        self.index = index
        self.is_starting_position_player1 = is_starting_position_player1
        self.is_starting_position_player2 = is_starting_position_player2
        self.is_occupied_by_player1 = is_occupied_by_player1
        self.is_occupied_by_player2 = is_occupied_by_player2
        self.wallList = wall_list
        field = Field()
        return field


class TableFields(object):
    table_fields = []
    x = y = k = None

    def __init__(self):
        self.table_fields = self.table_fields
        self.x = self.x
        self.y = self.y
        self.k = self.k

    def create_game_table(self, table_fields, x, y, k):
        self.table_fields = table_fields
        self.x = x
        self.y = y
        self.k = k
        table_fields = TableFields()
        return table_fields

    def print_game_table(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.table_fields[i][j].is_occupied_by_player1:
                    print('X', end=" | ")
                if self.table_fields[i][j].is_occupied_by_player2:
                    print('O', end=" | ")
                if self.table_fields[i][j].is_starting_position_player1:
                    print('P1', end=" | ")
                if self.table_fields[i][j].is_starting_position_player2:
                    print('P2', end=" | ")
                else:
                    print(' ', end=" | ")
            print()

    def init_game_table(self):
        matrix = []
        x = y = k = None

        x = inputAndValidatePreGameParams(x, minMatrixDimensionX, maxMatrixDimensionX, matrixDimensionX)
        y = inputAndValidatePreGameParams(y, minMatrixDimensionY, maxMatrixDimensionY, matrixDimensionY)
        k = inputAndValidatePreGameParams(k, minAmountOfWalls, maxAmountOfWalls, amountOfWalls)

        dict['player1Position'] = dict['player1StartingPosition'] = [
            defineStartingPostionsForPlayers(0, x, 0, y, player1Position1MessageX, player1Position1MessageY,
                                             invalidPositionMessage),
            defineStartingPostionsForPlayers(0, x, 0, y, player1Position2MessageX, player1Position2MessageY,
                                             invalidPositionMessage)]
        dict['player2Position'] = dict['player2StartingPosition'] = [
            defineStartingPostionsForPlayers(0, x, 0, y, player2Position1MessageX, player2Position1MessageY,
                                             invalidPositionMessage),
            defineStartingPostionsForPlayers(0, x, 0, y, player2Position2MessageX, player2Position2MessageY,
                                             invalidPositionMessage)]

        dict['player1RemainingBlueWallsAmount'] = dict['player1RemainingGreenWallsAmount'] = \
            dict['player2RemainingBlueWallsAmount'] = dict['player2RemainingGreenWallsAmount'] = k

        for i in range(x):
            matrix.append(
                [Field(i, j, dict['player1StartingPosition'], dict['player2StartingPosition']) for j in range(y)])

        return self.create_game_table(matrix, x, y, k)
