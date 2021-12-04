from _common import matrixDimensionX, matrixDimensionY, minMatrixDimensionY, minMatrixDimensionX, maxMatrixDimensionY, \
    maxMatrixDimensionX, minAmountOfWalls, maxAmountOfWalls, amountOfWalls, player1Position1MessageX, \
    player1Position2MessageX, player1Position1MessageY, player1Position2MessageY, player2Position1MessageY, \
    player2Position1MessageX, player2Position2MessageX, player2Position2MessageY, invalidPositionMessage, \
    invalidPreGameParamsMessage


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


def calculate_if_field_is_starting_pos(i, j, position):
    if position[0] == (i, j) or position[1] == (i, j):
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
    gameStatuses = {
        "player1Position": None,
        "player2Position": None,
        "player1RemainingBlueWallsAmount": None,
        "player1RemainingGreenWallsAmount": None,
        "player2RemainingBlueWallsAmount": None,
        "player2RemainingGreenWallsAmount": None,
        "player1StartingPosition": None,
        "player2StartingPosition": None
    }

    def __init__(self):
        self.table_fields = self.table_fields
        self.x = self.x
        self.y = self.y
        self.k = self.k
        self.gameStatuses = self.gameStatuses

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def create_game_table(self, table_fields, x, y, k, game_statuses):
        self.table_fields = table_fields
        self.x = x
        self.y = y
        self.k = k
        self.gameStatuses = game_statuses
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
        statuses = {}

        x = input_and_validate_pre_game_params(x, minMatrixDimensionX, maxMatrixDimensionX, matrixDimensionX)
        y = input_and_validate_pre_game_params(y, minMatrixDimensionY, maxMatrixDimensionY, matrixDimensionY)
        k = input_and_validate_pre_game_params(k, minAmountOfWalls, maxAmountOfWalls, amountOfWalls)

        statuses['player1Position'] = \
            statuses['player1StartingPosition'] = \
            [define_starting_positions_for_players(0, x, 0, y, player1Position1MessageX, player1Position1MessageY,
                                                   invalidPositionMessage),
             define_starting_positions_for_players(0, x, 0, y, player1Position2MessageX, player1Position2MessageY,
                                                   invalidPositionMessage)]
        statuses['player2Position'] = \
            statuses['player2StartingPosition'] = \
            [define_starting_positions_for_players(0, x, 0, y, player2Position1MessageX, player2Position1MessageY,
                                                   invalidPositionMessage),
             define_starting_positions_for_players(0, x, 0, y, player2Position2MessageX, player2Position2MessageY,
                                                   invalidPositionMessage)]

        statuses['player1RemainingBlueWallsAmount'] = statuses['player1RemainingGreenWallsAmount'] = \
            statuses['player2RemainingBlueWallsAmount'] = statuses['player2RemainingGreenWallsAmount'] = k

        for i in range(x):
            matrix.append(
                [Field(i, j, statuses['player1StartingPosition'], statuses['player2StartingPosition']) for j in
                 range(y)])

        return self.create_game_table(matrix, x, y, k, statuses)
