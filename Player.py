from Figure import Figure


def define_first_player():
    print('Choose the first player.')
    print('Type Me if you want to go first.')
    print('Type Computer if you want computer to play first.')
    choice = input('> ')
    if choice == 'Me':
        return 1
    elif choice == 'Computer':
        return 2
    else:
        print('Invalid choice of first player. Try again. ')
        define_first_player()


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
        figure = input("Choose figure 1 or 2: ")
        x = int(input('X koordinata figure: ')) - 1
        y = int(input('Y koordinata figure: ')) - 1
        if figure == "1":
            return_val = self.figure1.move(x, y, obj)
            if return_val == -1:
                self.move_figure(obj)
        elif figure == "2":
            return_val = self.figure2.move(x, y, obj)
            if return_val == -1:
                self.move_figure(obj)
        else:
            print('Please choose between 1 or 2.')
            self.move_figure(obj)

