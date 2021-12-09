from Figure import Figure


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

    def move_figure(self):
        figure = input("Choose figure 1 or 2: ")
        x = int(input('X koordinata figure: ')) - 1
        y = int(input('Y koordinata figure: ')) - 1
        if figure == "1":
            self.figure1.move(x, y)
        elif figure == "2":
            self.figure2.move(x, y)
        else:
            print('Please choose between 1 or 2.')
            self.move_figure()

