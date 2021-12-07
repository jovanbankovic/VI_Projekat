

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

    def init_wall(self, obj):
        x = int(input("Write position X: ")) - 1
        y = int(input("Write position Y: ")) - 1
        pos = (x, y)
        inp = input("Choose blue or green: ")
        if inp == "blue":
            wall = self.make_wall(inp, pos)
            current_field = any(x for x in obj.table_fields[x][y].wallList if x.wall_type == "blue")
            next_field = any(x for x in obj.table_fields[x][y+1].wallList if x.wall_type == "blue")
            has_green_wall = any(x for x in obj.table_fields[x-1][y].wallList if x.wall_type == "green")
            if current_field:
                print("Ima zid ovde!")
                return -1
            elif next_field:
                print("Ima zid pored!")
                return -1
            elif has_green_wall:
                print("Ima zid izmedju!");
                return -1
            else:
                obj.update_field(x, y, wall)
        elif inp == "green":
            wall = self.make_wall(inp, pos)
            current_field = any(x for x in obj.table_fields[x][y].wallList if x.wall_type == "green")
            next_field = any(x for x in obj.table_fields[x+1][y].wallList if x.wall_type == "green")
            has_blue_wall = any(x for x in obj.table_fields[x+1][y].wallList if x.wall_type == "blue")
            if current_field:
                print("Ima zid ovde!")
                return -1
            elif next_field:
                print("Ima zid pored!")
                return -1
            elif has_blue_wall:
                print("Ima zid izmedju!");
                return -1
            else:
                obj.update_field(x, y, wall)
        else:
            print("You must choose between blue or green")
            return self.init_wall()


class WallList(object):
    wall_list = []
    number_of_walls = 0

    def __init__(self, number_of_walls):
        self.number_of_walls = number_of_walls

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def add_to_list(self, wall):
        if len(self.wall_list) <= self.number_of_walls:
            copy_wall_list = self.wall_list
            copy_wall_list.append(wall)
