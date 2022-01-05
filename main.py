from TableFields import TableFields
from Wall import Wall
from Player import define_first_player, define_first_turn_between_players, switch_turns, play_turn
from Node import Node
import sys

MAX, MIN = 1000, -1000

if __name__ == '__main__':
    first_player_choice = define_first_turn_between_players()

    obj = TableFields()
    wallObj = Wall()
    obj.init_game_table()
    obj.print_game_table()

    #node = Node()
    #node.min_max(obj, 3, True, MIN, MAX)
    #node.determinate_possible_state(obj)

    play_turn(obj, wallObj, first_player_choice)

