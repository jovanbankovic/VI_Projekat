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
            elif diff_y == 1:
                return "desno_1"
            elif diff_y == -1:
                return "levo_1"
            else:
                return "error"
        elif diff_y == 0:
            if diff_x == 2:
                return "dole"
            elif diff_x == -2:
                return "gore"
            elif diff_x == 1:
                return "dole_1"
            elif diff_x == -1:
                return "gore_1"
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

    def is_occupied(self, x, y, obj):
        if self.positionX == x and self.positionY == y:
            return -1
        elif obj.player1.figure2.positionX == x and obj.player1.figure2.positionY == y:
            return -1
        elif obj.player2.figure1.positionX == x and obj.player2.figure1.positionY == y:
            return -1
        elif obj.player2.figure2.positionX == x and obj.player2.figure2.positionY == y:
            return -1
        else:
            return 1

    def move(self, x, y, obj):
        # treba uslov za opseg da ne izlazi van
        direction = self.determine_direction(x, y)
        is_filed_occupied = self.is_occupied(x, y, obj)
        if is_filed_occupied == 1:
            match direction:
                case "desno":
                    if obj.table_fields[self.positionX][self.positionY+1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY+1].wallRight["type"] == "green":
                        print("You cant go there green wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "desno_1":
                    if self.is_occupied(x, y+1, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green":
                            print("You cant go there green wall is blocking you.")
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print("You cant jump 1 filed!")
                case "levo":
                    if obj.table_fields[self.positionX][self.positionY - 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY - 1].wallRight["type"] == "green":
                        print("You cant go there green wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "levo_1":
                    if self.is_occupied(x, y - 1, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green":
                            print("You cant go there green wall is blocking you.")
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print("You cant jump 1 filed!")
                case "gore":
                    if obj.table_fields[self.positionX-1][self.positionY].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX-1][self.positionY].wallDown["type"] == "blue":
                        print("You cant go there blue wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "gore_1":
                    if self.is_occupied(x-1, y, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                            print("You cant go there green wall is blocking you.")
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print("You cant jump 1 filed!")
                case "dole":
                    if obj.table_fields[self.positionX + 1][self.positionY].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY].wallDown["type"] == "blue":
                        print("You cant go there blue wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dole_1":
                    if self.is_occupied(x + 1, y, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                            print("You cant go there green wall is blocking you.")
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print("You cant jump 1 filed!")
                case "dijagonalaGore_levo":
                    if obj.table_fields[self.positionX - 1][self.positionY - 1].wallDown["type"] == "blue" or \
                            obj.table_fields[self.positionX - 1][self.positionY - 1].wallRight["type"] == "green" or \
                                obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                                    obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                        print("You cant go there is  wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaGore_desno":
                    if obj.table_fields[self.positionX - 1][self.positionY + 1].wallDown["type"] == "blue" or \
                            obj.table_fields[self.positionX - 1][self.positionY + 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                        print("You cant go there is  wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaDole_desno":
                    if obj.table_fields[self.positionX + 1][self.positionY + 1].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY + 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                        print("You cant go there is  wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaDole_levo":
                    if obj.table_fields[self.positionX + 1][self.positionY - 1].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY - 1].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                        print("You cant go there is  wall is blocking you.")
                    else:
                        self.positionX = x
                        self.positionY = y
        else:
            print("That filed is occupied!")


