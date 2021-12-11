

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
        self.wall_type = wall_type
        self.position = position
        return self

    def init_wall(self, obj, player):
        x = int(input("Write position X: ")) - 1
        y = int(input("Write position Y: ")) - 1
        pos = (x, y)
        inp = input("Choose blue or green: ")
        if inp == "blue":
            if player.remainingBlueWalls > 0:
                wall = self.make_wall(inp, pos)
                if obj.table_fields[x][y].wallDown["type"] == "blue":
                    print("Ima zid ovde!")
                    return -1
                elif obj.table_fields[x][y + 1].wallDown["type"] == "blue":
                    print("Ima zid pored!")
                    return -1
                elif obj.table_fields[x][y].wallRight["type"] == "green":
                    print("Ima zeleni zid izmedju!")
                    return -1
                else:
                    player.remainingBlueWalls = player.remainingBlueWalls - 1
                    obj.update_field_for_blue(x, y, y+1, wall)
            else:
                print("Nemate vise plavih zidova!")
        elif inp == "green":
            if player.remainingGreenWallsWalls > 0:
                wall = self.make_wall(inp, pos)
                if obj.table_fields[x][y].wallRight["type"] == "green":
                    print("Ima zid ovde!")
                    return -1
                elif obj.table_fields[x+1][y].wallRight["type"] == "green":
                    print("Ima zid ispod!")
                    return -1
                elif obj.table_fields[x][y].wallDown["type"] == "blue":
                    print("Ima plavi zid izmedju!!!!")
                    return -1
                else:
                    obj.update_field_for_green(x, y, x+1, wall)
            else:
                print("Nemate vise zelenih zidova!")
        else:
            print("You must choose between blue or green")
            self.init_wall(obj)


