from TableFields import TableFields
from Wall import Wall
from Player import Player

if __name__ == '__main__':
    #ko igra prvi

    obj = TableFields()
    wallObj = Wall()
    obj.init_game_test()
    obj.print_game_table()

    while obj.is_game_over() != 1 or obj.is_game_over != 2:
        print()
        obj.player1.move_player()
        #wallObj.init_wall(obj)
        obj.print_game_table()
