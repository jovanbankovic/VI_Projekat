from Colors import Colors


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
        """
        Funkcija koja odredjuje pravac kretanja figure
        """
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
        """
        Funkcija koja proverava da li je polje zauzeto
        """
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

    def isValidMove(self, x, y, obj, direction):
        """

        """
        match direction:
            case "desno":
                if obj.table_fields[self.positionX][self.positionY + 1].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY + 1].wallRight["type"] == "green":
                    return False
                else:
                    return True,(self.positionX,self.positionY + 1)
            case "desno_1":
                if self.is_occupied(x, y + 1, obj) == -1:
                    if obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green":
                        return False
                    else:
                        return True
                else:
                    return False
            case "levo":
                if obj.table_fields[self.positionX][self.positionY - 1].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY - 1].wallRight["type"] == "green":
                    return False
                else:
                    return True, (self.positionX, self.positionY - 1)
            case "levo_1":
                if self.is_occupied(x, y - 1, obj) == -1:
                    if obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green":
                        return False
                    else:
                        return True
                else:
                    return False
            case "gore":
                if obj.table_fields[self.positionX - 1][self.positionY].wallUp["type"] == "blue" or \
                        obj.table_fields[self.positionX - 1][self.positionY].wallDown["type"] == "blue":
                    return False
                else:
                    return True, (self.positionX-1, self.positionY)
            case "gore_1":
                if self.is_occupied(x - 1, y, obj) == -1:
                    if obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                        return False
                    else:
                        return True
                else:
                    return False
            case "dole":
                if obj.table_fields[self.positionX + 1][self.positionY].wallUp["type"] == "blue" or \
                        obj.table_fields[self.positionX + 1][self.positionY].wallDown["type"] == "blue":
                    return False
                else:
                    return True, (self.positionX+1, self.positionY)
            case "dole_1":
                if self.is_occupied(x + 1, y, obj) == -1:
                    if obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                        return False
                    else:
                        return True
                else:
                    return False
            case "dijagonalaGore_levo":
                if obj.table_fields[self.positionX - 1][self.positionY - 1].wallDown["type"] == "blue" or \
                        obj.table_fields[self.positionX - 1][self.positionY - 1].wallRight["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                    return False
                else:
                    return True, (self.positionX-1, self.positionY-1)
            case "dijagonalaGore_desno":
                if obj.table_fields[self.positionX - 1][self.positionY + 1].wallDown["type"] == "blue" or \
                        obj.table_fields[self.positionX - 1][self.positionY + 1].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                    return False
                else:
                    return True,(self.positionX-1, self.positionY+1)
            case "dijagonalaDole_desno":
                if obj.table_fields[self.positionX + 1][self.positionY + 1].wallUp["type"] == "blue" or \
                        obj.table_fields[self.positionX + 1][self.positionY + 1].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                    return False
                else:
                    return True, (self.positionX+1, self.positionY+1)
            case "dijagonalaDole_levo":
                if obj.table_fields[self.positionX + 1][self.positionY - 1].wallUp["type"] == "blue" or \
                        obj.table_fields[self.positionX + 1][self.positionY - 1].wallRight["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                        obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                    return False
                else:
                    return True, (self.positionX+1, self.positionY-1)

    def move(self, x, y, obj):
        """
            Funkcija koja uz validaciju pomera figuru
        """
        direction = self.determine_direction(x, y)
        is_filed_occupied = self.is_occupied(x, y, obj)
        if is_filed_occupied == 1:
            match direction:
                case "desno":
                    if obj.table_fields[self.positionX][self.positionY+1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY+1].wallRight["type"] == "green":
                        print(Colors.WARNING + "You can't go there. Green wall is blocking you." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "desno_1":
                    if self.is_occupied(x, y+1, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green":
                            print(Colors.WARNING + "You can't go there. Green wall is blocking you." + Colors.ENDC)
                            return -1
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print("You cant jump 1 filed!")
                        return -1
                case "levo":
                    if obj.table_fields[self.positionX][self.positionY - 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY - 1].wallRight["type"] == "green":
                        print(Colors.WARNING + "You can't go there. Green wall is blocking you." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "levo_1":
                    if self.is_occupied(x, y - 1, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green":
                            print(Colors.WARNING + "You can't go there. Green wall is blocking you." + Colors.ENDC)
                            return -1
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print(Colors.WARNING + "You can't jump one field." + Colors.ENDC)
                        return -1
                case "gore":
                    if obj.table_fields[self.positionX-1][self.positionY].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX-1][self.positionY].wallDown["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Blue wall is blocking you." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "gore_1":
                    if self.is_occupied(x-1, y, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                            print(Colors.WARNING + "You can't go there. Blue wall is blocking you." + Colors.ENDC)
                            return -1
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print(Colors.WARNING + "You can't jump one field." + Colors.ENDC)
                        return -1
                case "dole":
                    if obj.table_fields[self.positionX + 1][self.positionY].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY].wallDown["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Blue wall is blocking you." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dole_1":
                    if self.is_occupied(x + 1, y, obj) == -1:
                        if obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                            print(Colors.WARNING + "You can't go there. Blue wall is blocking you." + Colors.ENDC)
                            return -1
                        else:
                            self.positionX = x
                            self.positionY = y
                    else:
                        print(Colors.WARNING + "You can't jump one field." + Colors.ENDC)
                case "dijagonalaGore_levo":
                    if obj.table_fields[self.positionX - 1][self.positionY - 1].wallDown["type"] == "blue" or \
                            obj.table_fields[self.positionX - 1][self.positionY - 1].wallRight["type"] == "green" or \
                                obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                                    obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Wall is blocking your path." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaGore_desno":
                    if obj.table_fields[self.positionX - 1][self.positionY + 1].wallDown["type"] == "blue" or \
                            obj.table_fields[self.positionX - 1][self.positionY + 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallUp["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Wall is blocking your path." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaDole_desno":
                    if obj.table_fields[self.positionX + 1][self.positionY + 1].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY + 1].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Wall is blocking your path." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
                case "dijagonalaDole_levo":
                    if obj.table_fields[self.positionX + 1][self.positionY - 1].wallUp["type"] == "blue" or \
                            obj.table_fields[self.positionX + 1][self.positionY - 1].wallRight["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallLeft["type"] == "green" or \
                            obj.table_fields[self.positionX][self.positionY].wallDown["type"] == "blue":
                        print(Colors.WARNING + "You can't go there. Wall is blocking your path." + Colors.ENDC)
                        return -1
                    else:
                        self.positionX = x
                        self.positionY = y
        else:
            print(Colors.WARNING + "That filed is occupied." + Colors.ENDC)
            return -1


