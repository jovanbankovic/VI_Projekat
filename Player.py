from Figure import Figure
from Colors import Colors


def define_first_player():
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


class Player(object):
    figure1 = None
    figure2 = None
    remainingBlueWalls = None
    remainingGreenWalls = None

    def __init__(self, first_figure_pos_x, first_figure_pos_y, second_figure_pos_x, second_figure_pos_y, remaining_walls):
        self.figure1 = Figure(first_figure_pos_x, first_figure_pos_y)
        self.figure2 = Figure(second_figure_pos_x, second_figure_pos_y)
        self.remainingBlueWalls = remaining_walls
        self.remainingGreenWalls = remaining_walls

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def move_figure(self, obj):
        print()
        figure = input(Colors.OKBLUE + "Choose figure 1 or 2: " + Colors.ENDC)
        x = int(input('Enter the ' + Colors.OKBLUE + 'X' + Colors.ENDC + ' coordinate of the figure: ')) - 1
        y = int(input('Enter the ' + Colors.OKBLUE + 'Y' + Colors.ENDC + ' coordinate of the figure: ')) - 1
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

