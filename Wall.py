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

    def deep_copy_table(self, obj, x, y):
        """
        Funkcija koja pravi kopiju polja koriscenjem biblioteke copy. Povratna vrednost funkcije je objekat TableFields
        """
        w, h = y, x
        matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(x):
            for j in range(y):
                matrix[i][j] = deepcopy(obj.table_fields[i][j])

        new_table_fields = TableFields()

        player1 = Player(None, None, None, None, None)
        new_player1 = player1.create_player(obj.player1.figure1.positionX, obj.player1.figure1.positionY,
                                            obj.player1.figure1.startingPositionX,obj.player1.figure1.startingPositionY,
                                            obj.player1.figure2.positionX, obj.player1.figure2.positionY,
                                            obj.player1.figure2.startingPositionX, obj.player1.figure2.startingPositionY
                                            )
        player2 = Player(None, None, None, None, None)
        new_player2 = player2.create_player(obj.player2.figure1.positionX, obj.player2.figure1.positionY,
                                            obj.player2.figure1.startingPositionX,obj.player2.figure1.startingPositionY,
                                            obj.player2.figure2.positionX, obj.player2.figure2.positionY,
                                            obj.player2.figure2.startingPositionX,
                                            obj.player2.figure2.startingPositionY
                                            )
        copy = new_table_fields.create_game_table(matrix, obj.x, obj.y, obj.k, new_player1, new_player2)
        return copy

    def playMove(self, obj, pos, player, figure):
        """
        Funkcija koja u zavinosti od igraca i figure postavlja X i Y koordinatu figure
        """
        if player == 'player1':
            if figure == 'figure1':
                obj.player1.figure1.positionX = pos[0]
                obj.player1.figure1.positionY = pos[1]
            elif figure == 'figure2':
                obj.player1.figure2.positionX = pos[0]
                obj.player1.figure2.positionY = pos[1]
        elif player == 'player2':
            if figure == 'figure1':
                obj.player2.figure1.positionX = pos[0]
                obj.player2.figure1.positionY = pos[1]
            elif figure == 'figure2':
                obj.player2.figure2.positionX = pos[0]
                obj.player2.figure2.positionY = pos[1]

        return obj

    def findPossibleMoves(self, obj, current_positionX, current_postionY, obj_player_figure):
        """
        Funkcija koja vraca listu mogucih poteza za svako polje. Za svaku od 8 mogucnosti, ispitujemo da li je moguce
        kretanje i ukoliko jeste i naredno polje nema Visited flag ubacujemo ga u listu mogucih poteza, dok parametar
        Visited u trenutnom polju postavljamo na True
        """
        list_of_possible_moves = []
        moves = ['levo','desno','gore','dole','dijagonalaGore_levo','dijagonalaGore_desno',
                         'dijagonalaDole_levo','dijagonalaDole_desno']

        for move in moves:
            value = obj_player_figure.isValidMove(current_positionX, current_postionY, obj, move)
            if value[0]:
                # proveriti da li postoji potez u prethodni potezi pre dodavanja
                if obj.table_fields[value[1][0]][value[1][1]].visited == False:
                    obj.table_fields[current_positionX][current_postionY].visited = True
                    list_of_possible_moves.append(value[1])

        return list_of_possible_moves


    def check_if_there_are_paths(self,obj):
        """
        Funkcija koja za oba igraca i njegove figure poziva funkcija za racunanje da li postoji put do pocetne pozicije
        """

        #make 4 copies of obj
        obj1 = self.deep_copy_table(obj, obj.x, obj.y)
        obj2 = self.deep_copy_table(obj, obj.x, obj.y)
        obj3 = self.deep_copy_table(obj, obj.x, obj.y)
        obj4 = self.deep_copy_table(obj, obj.x, obj.y)

        # first check for player 1 figure 1
        player1_figure_1 = self.calculate_closed_path_to_starting_positions(
            obj1.player2.figure1.startingPositionX,
            obj1.player2.figure1.startingPositionY,
            obj1,
            (obj1.player1.figure1.positionX, obj1.player1.figure1.positionY),
            'player1', 'figure1',obj1.player1.figure1)

        if not player1_figure_1:
            return False

        # second check for player 1 figure 2
        player1_figure_2 = self.calculate_closed_path_to_starting_positions(
            obj2.player2.figure2.startingPositionX,
            obj2.player2.figure2.startingPositionY,
            obj2,
            (obj2.player1.figure1.positionX, obj2.player1.figure1.positionY),
            'player1', 'figure1', obj2.player1.figure1)

        if not player1_figure_2:
            return False

        # second check for player 2 figure 1
        player2_figure_1 = self.calculate_closed_path_to_starting_positions(
            obj3.player1.figure1.startingPositionX,
            obj3.player1.figure1.startingPositionY,
            obj3,
            (obj3.player2.figure1.positionX, obj3.player2.figure1.positionY),
            'player2', 'figure1', obj3.player2.figure1)

        if not player2_figure_1:
            return False

        # second check for player 2 figure 2
        player2_figure_2 = self.calculate_closed_path_to_starting_positions(
            obj4.player1.figure2.startingPositionX,
            obj4.player1.figure2.startingPositionY,
            obj4,
            (obj4.player2.figure1.positionX, obj4.player2.figure1.positionY),
            'player2', 'figure1', obj4.player2.figure1)

        if not player2_figure_2:
            return False

        # if program goes here than we have paths for all starting paths
        return True


    def calculate_closed_path_to_starting_positions(self, starting_position_x, starting_position_y, obj,
                                                    currentPos, player, figure, obj_player_figure):
        """
        Funkcija koja racuna da li postoji put do pocetnih polja. Iskoristili smo rekurziju da simuliramo stablo, tako sto
        za svako polje racunamo moguce poteze. Za svaki od mogucih poteza rekurzivnim pozivom funkcije izvrsavamo isti algoritam sve
        dok ne nadje ili ne nadje put do pocetnog polja
        """

        if currentPos[0] == starting_position_x and currentPos[1] == starting_position_y:
            return True

        possibileMoves = self.findPossibleMoves(obj, currentPos[0], currentPos[1], obj_player_figure)
        if len(possibileMoves) == 0:
            return False

        find = False
        for move in possibileMoves:
            find = find or self.calculate_closed_path_to_starting_positions(starting_position_x, starting_position_y,
                                                                        self.playMove(obj, move, player, figure),
                                                                        move, player, figure, obj_player_figure )
        return find



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
                        # we make copy of whole tableField object and add new wall than we check if it has path to start position
                        obj2 = self.deep_copy_table(obj, obj.x, obj.y)
                        obj2.update_field_for_blue(x, y, y+1, wall)
                        has_path = self.check_if_there_are_paths(obj2)
                        if has_path:
                            player.remainingBlueWalls = player.remainingBlueWalls - 1
                            obj.update_field_for_blue(x, y, y+1, wall)
                        else:
                            print(Colors.WARNING + "You can't place wall there, because you are blocking the path to the starting position." + Colors.ENDC)
                            self.init_wall(obj, player)
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
                        obj2 = self.deep_copy_table(obj, obj.x, obj.y)
                        obj2.update_field_for_green(x, y, x+1, wall)
                        has_path = self.check_if_there_are_paths(obj2)
                        if has_path:
                            player.remainingGreenWalls = player.remainingGreenWalls - 1
                            obj.update_field_for_green(x, y, x+1, wall)
                        else:
                            print(Colors.WARNING + "You can't place wall there, because you are blocking the path to the starting position." + Colors.ENDC)
                            self.init_wall(obj, player)
                else:
                    print(Colors.WARNING + "You don't have any more green walls." + Colors.ENDC)
            else:
                print(Colors.WARNING + "You must choose between blue or green wall." + Colors.ENDC)
                return self.init_wall(obj, player)
        else:
            print(Colors.WARNING + 'Entered values are invalid. Please try again.' + Colors.ENDC)
            self.init_wall(obj, player)


