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


def define_starting_x_position(min_x, max_x, first_position_message, invalid):
    x = int(input(first_position_message))
    if x < min_x or x > max_x:
        print(invalid)
        define_starting_x_position(min_x, max_x, first_position_message, invalid)
    else:
        return x - 1


def define_starting_y_position(min_y, max_y, second_position_message, invalid):
    y = int(input(second_position_message))
    if y < min_y or y > max_y:
        print(invalid)
        define_starting_x_position(min_y, max_y, second_position_message, invalid)
    else:
        return y - 1


class Field(object):
    index: ()
    wallUp: {}
    wallDown: {}
    wallLeft: {}
    wallRight: {}

    def __init__(self, i, j):
        self.index = (i, j)
        self.wallUp = {
            "type": ''
        }
        self.wallDown = {
            "type": ''
        }
        self.wallLeft = {
            "type": ''
        }
        self.wallRight = {
            "type": ''
        }

    def set_field(self, wallUp, wallDown, wallLeft, wallRight):
        self.wallUp = wallUp
        self.wallDown = wallDown
        self.wallLeft = wallLeft
        self.wallRight = wallRight
        return self


class TableFields(object):
    table_fields = []
    x = y = k = None
    player1 = None
    player2 = None

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

    def update_field_for_blue(self, x, y, k, wall):

        # for current down
        self.table_fields[x][y].wallDown["type"] = wall.wall_type
        self.table_fields[x][k].wallDown["type"] = wall.wall_type
        # for fields below we need to put up field
        self.table_fields[x+1][y].wallUp["type"] = wall.wall_type
        self.table_fields[x+1][k].wallUp["type"] = wall.wall_type

        test = self.table_fields

    def update_field_for_green(self, x, y, k, wall):
        # for current down
        self.table_fields[x][y].wallRight["type"] = wall.wall_type
        self.table_fields[k][y].wallRight["type"] = wall.wall_type
        # for fields below we need to put up field
        self.table_fields[x][y+1].wallLeft["type"] = wall.wall_type
        self.table_fields[k][k+1].wallLeft["type"] = wall.wall_type

        test = self.table_fields

    def is_game_over(self):
        if ((self.player1.figure1.positionX == self.player2.figure1.startingPositionX and self.player1.figure1.positionY == self.player2.figure1.startingPositionY)
            or (self.player1.figure1.positionX == self.player2.figure2.startingPositionX and self.player1.figure1.positionY == self.player2.figure2.startingPositionY)
            or (self.player1.figure2.positionX == self.player2.figure1.startingPositionX and self.player1.figure2.positionY == self.player2.figure1.startingPositionY)
            or (self.player1.figure2.positionX == self.player2.figure2.startingPositionX and self.player1.figure2.positionY == self.player2.figure2.startingPositionY)):
            return 1
        elif ((self.player2.figure1.positionX == self.player1.figure1.startingPositionX and self.player2.figure1.positionY == self.player1.figure1.startingPositionY)
            or (self.player2.figure1.positionX == self.player1.figure2.startingPositionX and self.player2.figure1.positionY == self.player1.figure2.startingPositionY)
            or (self.player2.figure2.positionX == self.player1.figure1.startingPositionX and self.player2.figure2.positionY == self.player1.figure1.startingPositionY)
            or (self.player2.figure2.positionX == self.player1.figure2.startingPositionX and self.player2.figure2.positionY == self.player1.figure2.startingPositionY)):
            return 2

    def print_game_table(self):
        print("   ", end="")
        for j in range(self.y):
            print("%4s" % hex(j + 1).split('x')[-1].upper(), end="")
        print('    ')
        print("   ", end="")
        for j in range(self.y):
            print("%4s" % "═", end="")

        for i in range(self.x):
            print("\n%4s╟" % hex(i + 1).split('x')[-1].upper(), end="")
            for j in range(self.y):

                # <!-- PROVERA DAL JE IGRAC NA PROTIVNICKOM POLJU DA SE ON ODSTAMPA

                if (self.player1.figure1.positionX == i and self.player1.figure1.positionY == j) \
                        or (self.player1.figure2.positionX == i and self.player1.figure2.positionY == j):
                    if j == self.y - 1:
                        print("%1s" % " ✘", end="")
                    else:
                        if self.table_fields[i][j].wallRight["type"] == "green":
                            print("%1s" % " ✘", end=" ║")
                        else:
                            print("%1s" % " ✘", end=" │")
                elif (self.player1.figure1.startingPositionX == i and self.player1.figure1.startingPositionY == j)\
                        or (self.player1.figure2.startingPositionX == i and self.player1.figure2.startingPositionY == j):
                    if j == self.y - 1:
                        print("%1s" % " ◆", end="")
                    else:
                        if self.table_fields[i][j].wallRight["type"] == "green":
                            print("%1s" % " ◆", end=" ║")
                        else:
                            print("%1s" % " ◆", end=" │")
                elif (self.player2.figure1.positionX == i and self.player2.figure1.positionY == j) \
                        or (self.player2.figure2.positionX == i and self.player2.figure2.positionY == j):
                    if j == self.y - 1:
                        print("%1s" % " ⚫", end="")
                    else:
                        if self.table_fields[i][j].wallRight["type"] == "green":
                            print("%1s" % " ⚫", end=" ║")
                        else:
                            print("%1s" % " ⚫", end=" │")
                elif (self.player2.figure1.startingPositionX == i and self.player2.figure1.startingPositionY == j)\
                        or (self.player2.figure2.startingPositionX == i and self.player2.figure2.startingPositionY == j):
                    if j == self.y - 1:
                        print("%1s" % " ◇", end="")
                    else:
                        if self.table_fields[i][j].wallRight["type"] == "green":
                            print("%1s" % " ◇", end=" ║")
                        else:
                            print("%1s" % " ◇", end=" │")
                else:
                    if j == self.y - 1:
                        print("%1s" % "  ", end="")
                    else:
                        if self.table_fields[i][j].wallRight["type"] == "green":
                            print("%1s" % " ", end=" ║")
                        else:
                            print("%1s" % " ", end="  │")

            print("%2s" % "╢", end="%s" % hex(i + 1).split('x')[-1].upper())
            print()
            print("   ", end="")
            for j in range(self.y):
                if i < self.x - 1:
                    if self.table_fields[i][j].wallDown["type"] == "blue":
                        print("%4s" % "═", end='')
                    else:
                        print("%4s" % "─", end='')

        for j in range(self.y):
            print("%4s" % "═", end="")

        print()
        print("   ", end="")
        for j in range(self.y):
            print("%4s" % hex(j + 1).split('x')[-1].upper(), end="")

    def init_game_table(self):
        matrix = []
        x = y = k = None

        x = input_and_validate_pre_game_params(x, minMatrixDimensionX, maxMatrixDimensionX, matrixDimensionX)
        y = input_and_validate_pre_game_params(y, minMatrixDimensionY, maxMatrixDimensionY, matrixDimensionY)
        k = input_and_validate_pre_game_params(k, minAmountOfWalls, maxAmountOfWalls, amountOfWalls)

        player1_figure1_x = define_starting_x_position(0, x, player1Position1MessageX, invalidPreGameParamsMessage)
        player1_figure1_y = define_starting_y_position(0, y, player1Position1MessageY, invalidPreGameParamsMessage)

        player1_figure2_x = define_starting_x_position(0, x, player1Position2MessageX, invalidPreGameParamsMessage)
        player1_figure2_y = define_starting_y_position(0, y, player1Position2MessageY, invalidPreGameParamsMessage)

        player2_figure1_x = define_starting_x_position(0, x, player2Position1MessageX, invalidPreGameParamsMessage)
        player2_figure1_y = define_starting_y_position(0, y, player2Position1MessageY, invalidPreGameParamsMessage)

        player2_figure2_x = define_starting_x_position(0, x, player2Position2MessageX, invalidPreGameParamsMessage)
        player2_figure2_y = define_starting_y_position(0, y, player2Position2MessageY, invalidPreGameParamsMessage)

        player1 = Player(player1_figure1_x, player1_figure1_y, player1_figure2_x, player1_figure2_y, k)
        player2 = Player(player2_figure1_x, player2_figure1_y, player2_figure2_x, player2_figure2_y, k)

        for i in range(x):
            matrix.append([Field(i, j) for j in range(y)])

        return self.create_game_table(matrix, x, y, k, player1, player2)
