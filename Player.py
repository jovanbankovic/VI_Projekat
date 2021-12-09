class Player(object):
    figurePositions = None
    remainingBlueWalls = None
    remainingGreenWalls = None
    startingPosition = None
    figure1PositionX = None
    figure1PositionY = None
    figure2PositionX = None
    figure2PositionY = None

    def __init__(self):
        self.figurePositions = self.figurePositions
        self.remainingBlueWalls = self. remainingBlueWalls
        self.remainingGreenWalls = self.remainingGreenWalls
        self.startingPosition = self.startingPosition
        self.figure1PositionX = self.figure1PositionX
        self.figure1PositionY = self.figure1PositionY
        self.figure2PositionX = self.figure2PositionX
        self.figure2PositionY = self.figure2PositionY

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def create_player(self, figure_positions, remaining_blue, remaining_green, starting_pos):
        self.figurePositions = figure_positions
        self.remainingBlueWalls = remaining_blue
        self.remainingGreenWalls = remaining_green
        self.startingPosition = starting_pos
        self.figure1PositionX = self.figurePositions[0][0]
        self.figure1PositionY = self.figurePositions[0][1]
        self.figure2PositionX = self.figurePositions[1][0]
        self.figure2PositionY = self.figurePositions[1][1]
        player = Player()
        return player

    def determine_direction(self, x, y,figure_x, figure_y ):
        diff_x = x - figure_x
        diff_y = y - figure_y
        if diff_x == 0:
            if diff_y == 2:
                return "desno"
            elif diff_y == -2:
                return "levo"
            else:
                return "error"
        elif diff_y == 0:
            if diff_x == 2:
                return "dole"
            elif diff_x == -2:
                return "gore"
            else:
                return "error"
        elif diff_x == -1:
            if diff_y == -1:
                return "dijagonalaGore_levo"
            elif diff_y == 1:
                return "dijagonalaGore_desno"
            else:
                return "error"
        elif diff_x == 1:
            if diff_y == -1:
                return "dijagonalaDole_levo"
            elif diff_y == 1:
                return "dijagonalaDole_desno"
            else:
                return "error"
        else:
            return "error"



    def move_player(self):
        figure = input("Choose figure 1 or 2: ")
        x = int(input("Write position X: "))
        y = int(input("Write position Y: "))
        new_position = (x, y)
        if figure == "1":
            test = self.determine_direction(x, y, self.figure1PositionX, self.figure1PositionY)
            print(test)
            match test:
                case "desno":
                    tmp1 = []
                    tmp1.append(new_position)
                    tmp1.append(self.figurePositions[1])
                    self.figurePositions = tmp1
                    print('baba')
                case "levo":
                    self.figurePositions = new_position

                case "dole":
                    self.figurePositions = new_position




