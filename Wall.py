from Colors import Colors
from copy import copy, deepcopy

from Player import Player
from TableFields import TableFields


class Wall(object):
    wall_type = ""
    position = (0, 0)

    def __init__(self):
        self.wall_type = self.wall_type
        self.position = self.position

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def make_wall(self, wall_type, position):
        """
        Funkcija koja kreira zid i postavlja parametre
        """
        self.wall_type = wall_type
        self.position = position
        return self

    def deep_copy_table(self, table, x, y):
        w, h = y, x
        matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(x):
            for j in range(y):
                matrix[i][j] = deepcopy(table[i][j])
        return matrix

    def playMove(self, obj, pos, player, figure):
        new_table_fields = TableFields()
        field_copy = self.deep_copy_table(obj.table_fields, obj.x, obj.y)
        new_player1 = Player(obj.player1.first_figure_pos_x,
                             obj.player1.first_figure_pos_y,
                             obj.player1.second_figure_pos_x,
                             obj.player1.second_figure_pos_y,
                             obj.player1.remaining_wals)
        new_player2 = Player(obj.player2.first_figure_pos_x,
                             obj.player2.first_figure_pos_y,
                             obj.player2.second_figure_pos_x,
                             obj.player2.second_figure_pos_y,
                             obj.player2.remaining_wals)
        new_table_fields.create_game_table(field_copy, obj.x, obj.y, obj.k, new_player1, new_player2)

        if player == 'player1':
            if figure == 'figure1':
                new_table_fields.player1.figure1.positionX = pos[0]
                new_table_fields.player1.figure1.positionY = pos[1]
            elif figure == 'figure2':
                new_table_fields.player1.figure2.positionX = pos[0]
                new_table_fields.player1.figure2.positionY = pos[1]
        elif player == 'player2':
            if figure == 'figure1':
                new_table_fields.player2.figure1.positionX = pos[0]
                new_table_fields.player2.figure1.positionY = pos[1]
            elif figure == 'figure2':
                new_table_fields.player2.figure2.positionX = pos[0]
                new_table_fields.player2.figure2.positionY = pos[1]

        return new_table_fields

    def findPossibleMoves(self, obj, current_position, previous_position):
        #nalazi sve moguce poteze ki se ne vracaju u prev. pos
        #vraca listu sledecih mogucih position-a
        return

    def calculate_closed_path_to_starting_positions(self, starting_position_x, starting_position_y, matrix, currentPos, previousPos):
        """
        if startpos
            return true
        posMs = findPossMovies(matrix, currentPos, previousPos)
        if !posMs or posMs.length == 0
            return false
        bool fined = false
        foreach move in posMs
            finded = finded or calculate_closed_path_to_start_position(starting_position_x, starting_position_y, playMove(matrix, move), move, currentPosition)
        return finded
        """

    def init_wall(self, obj, player):
        """
        Funkcija koja omogucava unos pozicija gde ce se nalaziti zid i postavlja ga uz validaciju
        """
        inp = input("Select whether you want to set the blue or green wall by typing "
                    + Colors.OKBLUE + "blue" + Colors.ENDC + " or " + Colors.OKGREEN + "green" + Colors.ENDC + ": ")\
            .lower()
        try:
            x = int(input("Enter the " +
                      Colors.OKBLUE + "X" + Colors.ENDC +
                      " coordinate of the field where the wall will be located: ")) - 1

            y = int(input("Enter the " + Colors.OKBLUE +
                      "Y" + Colors.ENDC + " coordinate of the field where the wall will be located: ")) - 1
        except ValueError:
            print(Colors.WARNING + 'Value must be number. Please try again.' + Colors.ENDC)
            return self.init_wall(obj, player)

        if (0 < x < obj.x) or (0 < y < obj.y):
            pos = (x, y)
            if inp == "blue":
                if player.remainingBlueWalls > 0:
                    wall = self.make_wall(inp, pos)
                    if obj.table_fields[x][y].wallDown["type"] == "blue":
                        print(Colors.WARNING + "There is already a wall in that field." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y + 1].wallDown["type"] == "blue":
                        print(Colors.WARNING +
                              "There is already a wall in the field next to where you are trying to set up the wall."
                              + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is a green wall between." + Colors.ENDC)
                        return -1
                    else:
                        player.remainingBlueWalls = player.remainingBlueWalls - 1
                        self.calculate_closed_path_to_starting_positions(obj, pos)
                        obj.update_field_for_blue(x, y, y+1, wall)
                else:
                    print(Colors.WARNING + "You don't have any more blue walls." + Colors.ENDC)
            elif inp == "green":
                if player.remainingGreenWalls > 0:
                    wall = self.make_wall(inp, pos)
                    if obj.table_fields[x][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is already a wall in that field." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x+1][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is already wall underneath." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y].wallDown["type"] == "blue":
                        print(Colors.WARNING + "There is a blue wall between." + Colors.ENDC)
                        return -1
                    else:
                        self.calculate_closed_path_to_starting_positions(obj, pos)
                        obj.update_field_for_green(x, y, x+1, wall)
                else:
                    print(Colors.WARNING + "You don't have any more green walls." + Colors.ENDC)
            else:
                print(Colors.WARNING + "You must choose between blue or green wall." + Colors.ENDC)
                return self.init_wall(obj, player)
        else:
            print(Colors.WARNING + 'Entered values are invalid. Please try again.' + Colors.ENDC)
            self.init_wall(obj, player)


