from TableFields import TableFields
from Wall import Wall

if __name__ == '__main__':
    #ko igra prvi

    obj = TableFields()
    wallObj = Wall()
    obj.init_game_table()
    updated_matrix = wallObj.init_wall(obj.table_fields)
    obj.print_game_table()

    #while obj.is_game_over() != 1 or obj.is_game_over != 2:
        #obj.player1.move_player(POZICIJA)
        #obj.print_game_table()
        #obj.player2.move_player(POZICIJA)
        #obj.print_game_table()
