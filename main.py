from TableFields import TableFields
from Wall import Wall

if __name__ == '__main__':
    #ko igra prvi

    obj = TableFields()
    wallObj = Wall()
    obj.init_game_table()
    obj.print_game_table()

    while obj.is_game_over() != 1 or obj.is_game_over != 2:
        print()
        wallObj.init_wall(obj)
        obj.player1.move_figure()
        obj.print_game_table()
