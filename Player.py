from Figure import Figure
from Colors import Colors


def define_first_player():
    """
    Funkcija koja odredjuje prvog igraca izmedju igraca i kompjutera
    """
    print(Colors.OKBLUE + 'Choose the first player.' + Colors.ENDC)
    print('Type ' + Colors.OKBLUE + 'Me' + Colors.ENDC + ' if you want to go first.')
    print('Type ' + Colors.OKBLUE + 'Computer' + Colors.ENDC + ' if you want computer to play first.')
    choice = input('> ').lower()
    if choice == 'me':
        return 1
    elif choice == 'computer':
        return 2
    else:
        print(Colors.FAIL + 'Invalid choice of first player. Try again. ' + Colors.ENDC)
        return define_first_player()


def define_first_turn_between_players():
    """
    Funkcija koja odredjuje prvog izmedju dva igraca
    """
    print(Colors.OKBLUE + 'Choose the first player.' + Colors.ENDC)
    print('Type ' + Colors.OKBLUE + 'Me' + Colors.ENDC + ' if you want to go first.')
    print('Type ' + Colors.OKBLUE + 'Computer' + Colors.ENDC + ' if you want Computer to go first.')
    choice = input('> ').lower()
    if choice == 'computer':
        return 1, True
    elif choice == 'me':
        return 2, True
    else:
        print(Colors.FAIL + 'Invalid choice of first player. Try again. ' + Colors.ENDC)
        return define_first_turn_between_players()

MAX, MIN = 1000, -1000

def switch_turns(turn, obj, wall_obj):
    """
    Funkcija koja poziva funkcije za odigravanje partije u zavisnosti od redosleda
    """
    from Node import Node
    match turn[0]:
        case 1:
            if turn[1] is True:
                figure = 'player1'
                is_player_first = False
            else:
                figure = 'player2'
                is_player_first = True

                print(Colors.FAIL + 'Computer is playing...' + Colors.ENDC)
                # wall_obj.init_wall(obj, obj.player1)
                # obj.print_game_table()
                # obj.player1.move_figure(obj)
                node = Node()
                bra = node.min_max(obj, 1, True, MIN, MAX, figure)

                obj.table_fields = bra[1].table_fields
                obj.player1 = bra[1].player1
                obj.player2 = bra[1].player2

                obj.print_game_table()
            return 2, is_player_first
        case 2:
            if turn[1] is True:
                figure = 'player1'
                is_computer_first = False
            else:
                figure = 'player2'
                is_computer_first = True

            print(Colors.FAIL + 'Player is playing...' + Colors.ENDC)
            if figure == 'player1':
                wall_obj.init_wall(obj, obj.player1)
                obj.print_game_table()
                obj.player1.move_figure(obj)
            else:
                wall_obj.init_wall(obj, obj.player2)
                obj.print_game_table()
                obj.player2.move_figure(obj)
            obj.print_game_table()
            return 1, is_computer_first


def play_turn(obj, wall_obj, first_player_choice):
    """
    Fukcija koja proverava zavrsetak igre, obavestava o pobedniku i poziva fuknkciju za odigravanje poteza ukoliko igra nije zavrsena
    """
    is_game_over = obj.is_game_over()
    players_turn = None
    if is_game_over == 1:
        obj.announce_winner(is_game_over)
    elif is_game_over == 2:
        obj.announce_winner(is_game_over)
    elif is_game_over != 1 or is_game_over != 2:
        print()
        if players_turn is None:
            players_turn = switch_turns(first_player_choice, obj, wall_obj)
        else:
            players_turn = switch_turns(players_turn, obj, wall_obj)
        play_turn(obj, wall_obj, players_turn)

def choose_singleplayer_or_multiplayer():
    print(Colors.OKBLUE + 'Choose between singleplayer or multiplayer.' + Colors.ENDC)
    print('Type ' + Colors.OKBLUE + 'Singleplayer' + Colors.ENDC + ' if you want Singleplayer to go first.')
    print('Type ' + Colors.OKBLUE + 'Multiplayer' + Colors.ENDC + ' if you want Multiplayer to go first.')
    choice = input('> ').lower()
    if choice == 'singleplayer':
        return 1
    elif choice == 'multiplayer':
        return 2
    else:
        print(Colors.FAIL + 'Invalid choice. Try again. ' + Colors.ENDC)
        return choose_singleplayer_or_multiplayer()


class Player(object):
    figure1 = None
    figure2 = None
    remainingBlueWalls = None
    remainingGreenWalls = None

    def __init__(self, first_figure_pos_x, first_figure_pos_y, second_figure_pos_x, second_figure_pos_y, remaining_walls):
        self.figure1 = Figure(first_figure_pos_x, first_figure_pos_y, first_figure_pos_x, first_figure_pos_y)
        self.figure2 = Figure(second_figure_pos_x, second_figure_pos_y, second_figure_pos_x, second_figure_pos_y)
        self.remainingBlueWalls = remaining_walls
        self.remainingGreenWalls = remaining_walls

    def __deepcopy__(self, memodict={}):
         player_copy = Player(self.figure1.positionX, self.figure1.positionY, self.figure2.positionX,
                              self.figure2.positionY, self.remainingBlueWalls)
         return player_copy
    def create_player(self, first_figure_pos_x, first_figure_pos_y,start_figure1_pos_x, start_figure1_pos_y,
                      second_figure_pos_x, second_figure_pos_y, start_figure2_pos_x, start_figure2_pos_y):
        self.figure1 = Figure(first_figure_pos_x, first_figure_pos_y,start_figure1_pos_x, start_figure1_pos_y)
        self.figure2 = Figure(second_figure_pos_x, second_figure_pos_y,start_figure2_pos_x, start_figure2_pos_y)
        self.remainingBlueWalls = 9
        self.remainingGreenWalls = 9
        return self

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def move_figure(self, obj):
        """
        Funkcija koja omogucava unos parametara za pomeraj figure i poziva funkciju za pomeraj iz Figure klase
        """
        print()
        figure = input(Colors.OKBLUE + "Choose figure 1 or 2: " + Colors.ENDC)
        try:
            x = int(input('Enter the ' + Colors.OKBLUE + 'X' + Colors.ENDC + ' coordinate of the figure: ')) - 1
            y = int(input('Enter the ' + Colors.OKBLUE + 'Y' + Colors.ENDC + ' coordinate of the figure: ')) - 1
        except ValueError:
            print(Colors.WARNING + 'Value must be number. Please try again.' + Colors.ENDC)
            return self.move_figure(obj)

        if (0 < x < obj.x) or (0 < y < obj.y):
            if figure == "1":
                return_val = self.figure1.move(x, y, obj)
                if return_val == -1:
                    return self.move_figure(obj)
            elif figure == "2":
                return_val = self.figure2.move(x, y, obj)
                if return_val == -1:
                    return self.move_figure(obj)
            else:
                print(Colors.FAIL + 'Please choose between 1 or 2.' + Colors.ENDC)
                return self.move_figure(obj)
        else:
            print(Colors.WARNING + 'Entered values are invalid. Please try again.' + Colors.ENDC)
            return self.move_figure(obj)
