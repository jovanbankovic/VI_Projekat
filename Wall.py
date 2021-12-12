from Colors import Colors


class Wall(object):
    wall_type = ""
    position = (0, 0)

    def __init__(self):
        self.wall_type = self.wall_type
        self.position = self.position

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def make_wall(self, wall_type, position):
        """
        Funkcija koja kreira zid i postavlja parametre
        """
        self.wall_type = wall_type
        self.position = position
        return self

    def init_wall(self, obj, player):
        """
        Funkcija koja omogucava unos pozicija gde ce se nalaziti zid i postavlja ga uz validaciju
        """
        inp = input("Select whether you want to set the blue or green wall by typing "
                    + Colors.OKBLUE + "blue" + Colors.ENDC + " or " + Colors.OKGREEN + "green" + Colors.ENDC + ": ")\
            .lower()
        try:
            x = int(input("Enter the " +
                      Colors.OKBLUE + "X" + Colors.ENDC +
                      " coordinate of the field where the wall will be located: ")) - 1

            y = int(input("Enter the " + Colors.OKBLUE +
                      "Y" + Colors.ENDC + " coordinate of the field where the wall will be located: ")) - 1
        except ValueError:
            print(Colors.WARNING + 'Value must be number. Please try again.' + Colors.ENDC)
            return self.init_wall(obj, player)

        if (0 < x < obj.x) or (0 < y < obj.y):
            pos = (x, y)
            if inp == "blue":
                if player.remainingBlueWalls > 0:
                    wall = self.make_wall(inp, pos)
                    if obj.table_fields[x][y].wallDown["type"] == "blue":
                        print(Colors.WARNING + "There is already a wall in that field." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y + 1].wallDown["type"] == "blue":
                        print(Colors.WARNING +
                              "There is already a wall in the field next to where you are trying to set up the wall."
                              + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is a green wall between." + Colors.ENDC)
                        return -1
                    else:
                        player.remainingBlueWalls = player.remainingBlueWalls - 1
                        obj.update_field_for_blue(x, y, y+1, wall)
                else:
                    print(Colors.WARNING + "You don't have any more blue walls." + Colors.ENDC)
            elif inp == "green":
                if player.remainingGreenWalls > 0:
                    wall = self.make_wall(inp, pos)
                    if obj.table_fields[x][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is already a wall in that field." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x+1][y].wallRight["type"] == "green":
                        print(Colors.WARNING + "There is already wall underneath." + Colors.ENDC)
                        return -1
                    elif obj.table_fields[x][y].wallDown["type"] == "blue":
                        print(Colors.WARNING + "There is a blue wall between." + Colors.ENDC)
                        return -1
                    else:
                        obj.update_field_for_green(x, y, x+1, wall)
                else:
                    print(Colors.WARNING + "You don't have any more green walls." + Colors.ENDC)
            else:
                print(Colors.WARNING + "You must choose between blue or green wall." + Colors.ENDC)
                return self.init_wall(obj, player)
        else:
            print(Colors.WARNING + 'Entered values are invalid. Please try again.' + Colors.ENDC)
            self.init_wall(obj, player)


