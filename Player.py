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

    def move_figure1(self):
        x = int(input('X koordinata prve figure: ')) - 1
        y = int(input('Y koordinata prve figure: ')) - 1
        self.figure1.move_figure(x, y)

    def move_figure2(self):
        x = int(input('X koordinata druge figure: ')) - 1
        y = int(input('Y koordinata druge figure: ')) - 1
        self.figure2.move_figure(x, y)
