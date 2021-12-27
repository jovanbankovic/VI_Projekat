from Colors import Colors
from TableFields import deep_copy_table, generate_matrix_for_visible


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

    def playMove(self, obj, pos, player, figure,visibleParamsMatrix):
        """
        Funkcija koja u zavinosti od igraca i figure postavlja X i Y koordinatu figure
        """
        obj = deep_copy_table(obj, obj.x, obj.y)

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

        visibleParamsMatrix[pos[0]][pos[1]] = 1
        return obj

    def findPossibleMoves(self, obj, current_positionX, current_postionY, player, figure, visibleParamsMatrix):
        """
        Funkcija koja vraca listu mogucih poteza za svako polje. Za svaku od 8 mogucnosti, ispitujemo da li je moguce
        kretanje i ukoliko jeste i naredno polje nema Visited flag ubacujemo ga u listu mogucih poteza, dok parametar
        Visited u trenutnom polju postavljamo na True
        """
        list_of_possible_moves = []
        moves = ['levo','desno','gore','dole','dijagonalaGore_levo','dijagonalaGore_desno',
                         'dijagonalaDole_levo','dijagonalaDole_desno']

        if player == 'player1':
            if figure == 'figure1':
                player_figure = obj.player1.figure1
            elif figure == 'figure2':
                player_figure = obj.player1.figure2
        elif player == 'player2':
            if figure == 'figure1':
                player_figure = obj.player2.figure1
            elif figure == 'figure2':
                player_figure = obj.player2.figure2

        for move in moves:
            value = player_figure.isValidMove(current_positionX, current_postionY, obj, move)
            if value[0]:
                # proveriti da li postoji potez u prethodni potezi pre dodavanja
                if visibleParamsMatrix[value[1][0]][value[1][1]] == 0:
                    list_of_possible_moves.append(value[1])

        return list_of_possible_moves, visibleParamsMatrix


    def check_if_there_are_paths(self,obj):
        """
        Funkcija koja za oba igraca i njegove figure poziva funkcija za racunanje da li postoji put do pocetne pozicije
        """
        visibleParamsMatrix1 = generate_matrix_for_visible(obj.x, obj.y)
        visibleParamsMatrix2 = generate_matrix_for_visible(obj.x, obj.y)
        visibleParamsMatrix3 = generate_matrix_for_visible(obj.x, obj.y)
        visibleParamsMatrix4 = generate_matrix_for_visible(obj.x, obj.y)

        # first check for player 1 figure 1
        player1_figure_1 = self.calculate_closed_path_to_starting_positions(
            obj.player2.figure2.startingPositionX,
            obj.player2.figure2.startingPositionY,
            obj,
            (obj.player1.figure1.positionX, obj.player1.figure1.positionY),
            'player1', 'figure1', visibleParamsMatrix1)

        if not player1_figure_1:
            return False

        # second check for player 1 figure 2
        player1_figure_2 = self.calculate_closed_path_to_starting_positions(
            obj.player2.figure1.startingPositionX,
            obj.player2.figure1.startingPositionY,
            obj,
            (obj.player1.figure1.positionX, obj.player1.figure1.positionY),
            'player1', 'figure1', visibleParamsMatrix2)

        if not player1_figure_2:
            return False

        # second check for player 2 figure 1
        player2_figure_1 = self.calculate_closed_path_to_starting_positions(
            obj.player1.figure1.startingPositionX,
            obj.player1.figure1.startingPositionY,
            obj,
            (obj.player2.figure1.positionX, obj.player2.figure1.positionY),
            'player2', 'figure1', visibleParamsMatrix3)

        if not player2_figure_1:
            return False

        # second check for player 2 figure 2
        player2_figure_2 = self.calculate_closed_path_to_starting_positions(
            obj.player1.figure2.startingPositionX,
            obj.player1.figure2.startingPositionY,
            obj,
            (obj.player2.figure1.positionX, obj.player2.figure1.positionY),
            'player2', 'figure1', visibleParamsMatrix4)

        if not player2_figure_2:
            return False

        # if program goes here than we have paths for all starting paths
        return True


    def calculate_closed_path_to_starting_positions(self, starting_position_x, starting_position_y, obj,
                                                    currentPos, player, figure, visibleParamsMatrix):
        """
        Funkcija koja racuna da li postoji put do pocetnih polja. Iskoristili smo rekurziju da simuliramo stablo, tako sto
        za svako polje racunamo moguce poteze. Za svaki od mogucih poteza rekurzivnim pozivom funkcije izvrsavamo isti algoritam sve
        dok ne nadje ili ne nadje put do pocetnog polja
        """

        if currentPos[0] == starting_position_x and currentPos[1] == starting_position_y:
            return True

        possibileMoves = self.findPossibleMoves(obj, currentPos[0], currentPos[1], player, figure, visibleParamsMatrix)
        if len(possibileMoves[0]) == 0:
            return False

        find = False
        for move in possibileMoves[0]:
            find = find or self.calculate_closed_path_to_starting_positions(starting_position_x, starting_position_y,
                                                                        self.playMove(obj, move, player, figure, visibleParamsMatrix),
                                                                        move, player, figure,
                                                                        possibileMoves[1])
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
                        copiedMatrix = deep_copy_table(obj, obj.x, obj.y)
                        visibleParamsMatrix = generate_matrix_for_visible(copiedMatrix.x, copiedMatrix.y)
                        copiedMatrix.update_field_for_blue(x, y, y+1, wall)
                        has_path = self.check_if_there_are_paths(obj)
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
                        obj2 = deep_copy_table(obj, obj.x, obj.y)
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


