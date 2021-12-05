

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
        wall = Wall()
        return wall

    def init_wall(self, matrix):
        x = input("Write position X: ")
        y = input("Write position Y: ")
        pos = (int(x), int(y))
        inp = input("Choose blue or green: ")
        if inp == "blue":
            # provera
            
            return self.make_wall(inp, pos)
            # whatevercodeyouwant_1()
        elif inp == "green":
            # provera da li ima dovoljno zelenih
            return self.make_wall(inp, pos)
            # whatevercodeyouwant_2()
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
