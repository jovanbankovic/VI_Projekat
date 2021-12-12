from TableFields import TableFields
from Wall import Wall
from Player import define_first_player

if __name__ == '__main__':
    first_player_choice = define_first_player()

    obj = TableFields()
    wallObj = Wall()
    obj.init_game_table()
    obj.print_game_table()

    while obj.is_game_over() != 1 or obj.is_game_over != 2:
        print()
        if first_player_choice == 1:
            wallObj.init_wall(obj, obj.player1)
            obj.print_game_table()
            obj.player1.move_figure(obj)
            obj.print_game_table()
        elif first_player_choice == 2:
            wallObj.init_wall(obj, obj.player2)
            obj.print_game_table()
            obj.player2.move_figure(obj)
            obj.print_game_table()
