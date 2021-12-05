class Player(object):
    figurePositions = None
    remainingBlueWalls = None
    remainingGreenWalls = None
    startingPosition = None

    def __init__(self):
        self.figurePositions = self.figurePositions
        self.remainingBlueWalls = self. remainingBlueWalls
        self.remainingGreenWalls = self.remainingGreenWalls
        self.startingPosition = self.startingPosition

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def create_player(self, figure_positions, remaining_blue, remaining_green, starting_pos):
        self.figurePositions = figure_positions
        self.remainingBlueWalls = remaining_blue
        self.remainingGreenWalls = remaining_green
        self.startingPosition = starting_pos
        player = Player()
        return player

    def move_player(self, new_position):
        self.figurePositions = new_position
