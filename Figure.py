class Figure(object):
    positionX: None
    positionY: None
    startingPositionX: None
    startingPositionY: None

    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y
        self.startingPositionX = x
        self.startingPositionY = y

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def determine_direction(self, x, y):
        diff_x = x - self.positionX
        diff_y = y - self.positionY
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

    def move(self, x, y):
        direction = self.determine_direction(x, y)
        match direction:
            case "desno":
                self.positionX = x
                self.positionY = y
