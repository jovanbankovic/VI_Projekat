from _common import matrixDimensionX, matrixDimensionY, minMatrixDimensionY, minMatrixDimensionX, maxMatrixDimensionY, \
    maxMatrixDimensionX, minAmountOfWalls, maxAmountOfWalls, amountOfWalls, player1Position1MessageX, \
    player1Position2MessageX, player1Position1MessageY, player1Position2MessageY, player2Position1MessageY, \
    player2Position1MessageX, player2Position2MessageX, player2Position2MessageY, invalidPositionMessage, \
    invalidPreGameParamsMessage
from Player import Player


def input_and_validate_pre_game_params(value, min_value, max_value, input_message):
    value = int(input(input_message))
    if value < min_value or value > max_value:
        print(invalidPreGameParamsMessage)
        input_and_validate_pre_game_params(value, min_value, max_value, input_message)
    else:
        return value


def define_starting_positions_for_players(min_x, max_x, min_y, max_y, first_position_message,
                                          second_position_message, invalid_position_params):
    first_position = int(input(first_position_message))
    second_position = int(input(second_position_message))
    if first_position < min_x or first_position > max_x and second_position < min_y or second_position > max_y:
        print(invalid_position_params)
        define_starting_positions_for_players(min_x, max_x, min_y, max_y, first_position_message,
                                              second_position_message, invalid_position_params)
    else:
        return first_position, second_position


class Field(object):
    index: ()
    wallList: []

    def __init__(self, i, j):
        self.index = (i, j)
        self.wallList = []

    def set_field(self, index, wall_list):
        self.index = index
        self.wallList = wall_list
        field = Field()
        return field


class TableFields(object):
    table_fields = []
    x = y = k = None
    player1 = Player()
    player2 = Player()

    def __init__(self):
        self.table_fields = self.table_fields
        self.x = self.x
        self.y = self.y
        self.k = self.k
        self.player1 = self.player1
        self.player2 = self.player2

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def create_game_table(self, table_fields, x, y, k, player1, player2):
        self.table_fields = table_fields
        self.x = x
        self.y = y
        self.k = k
        self.player1 = player1
        self.player2 = player2
        table_fields = TableFields()
        return table_fields

    def print_game_table(self):
        print("   ", end="")
        for j in range(self.x):
            print("%4s" % hex(j + 1).split('x')[-1].upper(), end="")
        print('    ')
        print("   ", end="")
        for j in range(self.x):
            print("%4s" % "═", end="")

        for i in range(self.y):
            print("\n%4s╟" % hex(i + 1).split('x')[-1].upper(), end="")
            for j in range(self.x):

                # <!-- DODATI STAMPANJE ZIDOVA !

                if self.player1.figurePositions[0] == (i, j) or self.player1.figurePositions[1] == (i, j):
                    if j == self.x - 1:
                        print("%1s" % " X", end="")
                    else:
                        print("%1s" % " X", end=" │")

                elif self.player1.startingPosition[0] == (i, j) or self.player1.startingPosition[1] == (i, j):
                    if j == self.x - 1:
                        print("%1s" % " S", end="")
                    else:
                        print("%1s" % " S", end=" │")

                elif self.player2.figurePositions[0] == (i, j) or self.player2.figurePositions[1] == (i, j):
                    if j == self.x - 1:
                        print("%1s" % " O", end="")
                    else:
                        print("%1s" % " O", end=" │")

                elif self.player2.startingPosition[0] == (i, j) or self.player2.startingPosition[1] == (i, j):
                    if j == self.x - 1:
                        print("%1s" % " S", end="")
                    else:
                        print("%1s" % " S", end=" │")

                else:
                    if j == self.x - 1:
                        print("%1s" % "  ", end="")
                    else:
                        print("%1s" % " ", end="  │")

            print("%2s" % "╢", end="%s" % hex(i + 1).split('x')[-1].upper())
            print()
            print("   ", end="")
            if (i < self.y - 1):
                for j in range(self.x):
                    print("%4s" % "─", end='')

        for j in range(self.x):
            print("%4s" % "═", end="")

        print()
        print("   ", end="")
        for j in range(self.x):
            print("%4s" % hex(j + 1).split('x')[-1].upper(), end="")

    def init_game_table(self):
        matrix = []
        x = y = k = None
        player1 = Player()
        player2 = Player()

        x = input_and_validate_pre_game_params(x, minMatrixDimensionX, maxMatrixDimensionX, matrixDimensionX)
        y = input_and_validate_pre_game_params(y, minMatrixDimensionY, maxMatrixDimensionY, matrixDimensionY)
        k = input_and_validate_pre_game_params(k, minAmountOfWalls, maxAmountOfWalls, amountOfWalls)

        player1.figurePositions = \
            player1.startingPosition = \
            [define_starting_positions_for_players(0, x, 0, y, player1Position1MessageX, player1Position1MessageY,
                                                   invalidPositionMessage),
             define_starting_positions_for_players(0, x, 0, y, player1Position2MessageX, player1Position2MessageY,
                                                   invalidPositionMessage)]
        player2.figurePositions = \
            player2.startingPosition = \
            [define_starting_positions_for_players(0, x, 0, y, player2Position1MessageX, player2Position1MessageY,
                                                   invalidPositionMessage),
             define_starting_positions_for_players(0, x, 0, y, player2Position2MessageX, player2Position2MessageY,
                                                   invalidPositionMessage)]

        player1.remainingBlueWalls = player1.remainingBlueWalls = \
            player2.remainingBlueWalls = player2.remainingGreenWalls = k

        for i in range(x):
            matrix.append([Field(i, j) for j in range(y)])

        return self.create_game_table(matrix, x, y, k, player1, player2)
