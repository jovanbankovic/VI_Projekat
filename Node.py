from TableFields import deep_copy_table
import random
MAX, MIN = 1000, -1000


class Node(object):
    def __init__(self):
        return

    def new_state_of_game(self, obj_param, x, y, inp, player, move, figure):
        """
        Funkcija koja pravi novo stanje na osnovu prosledjenih parametara
        :param obj_param: Trenutno stanje igre
        :param x:
        :param y:
        :param inp: vrsta zida
        :param player:
        :param move:
        :param figure:
        :return:
        """
        from TableFields import deep_copy_table
        from Wall import Wall

        obj = deep_copy_table(obj_param, obj_param.x, obj_param.y)
        if (0 < x < obj.x) or (0 < y < obj.y):
            pos = (x, y)
            if inp == "blue":
                if player.remainingBlueWalls > 0:
                    if 0 <= x < len(obj.table_fields) and 0 <= y + 1 < len(obj.table_fields[0]):
                        wall_object = Wall()
                        wall = wall_object.make_wall(inp, pos)
                        if obj.table_fields[x][y].wallDown["type"] == "blue":
                            return -1
                        elif obj.table_fields[x][y + 1].wallDown["type"] == "blue":
                            return -1
                        elif obj.table_fields[x][y].wallRight["type"] == "green":
                            return -1
                        else:
                            # we make copy of whole tableField object and add new wall than we check if it has path to start position
                            copied_matrix = deep_copy_table(obj, obj.x, obj.y)
                            return_param = copied_matrix.update_field_for_blue(x, y, y + 1, wall)
                            if return_param:
                                has_path = wall_object.check_if_there_are_paths(copied_matrix)
                                #has_path = True
                                if has_path:
                                    if figure == 'player1':
                                        obj.player1.remainingBlueWalls = obj.player1.remainingBlueWalls - 1
                                        obj.player1.figure1.positionX = move[0]
                                        obj.player1.figure1.positionY = move[1]
                                        obj.update_field_for_blue(x, y, y + 1, wall)
                                    else:
                                        obj.player2.remainingBlueWalls = obj.player2.remainingBlueWalls - 1
                                        obj.player2.figure1.positionX = move[0]
                                        obj.player2.figure1.positionY = move[1]
                                        obj.update_field_for_blue(x, y, y + 1, wall)
                                    return obj
                                else:
                                    return -1
                            else:
                                return -1
                    else:
                        return -1
                else:
                    if figure == 'player1':
                        obj.player1.figure1.positionX = move[0]
                        obj.player1.figure1.positionY = move[1]
                    else:
                        obj.player2.figure1.positionX = move[0]
                        obj.player2.figure1.positionY = move[1]
                    return obj
            elif inp == "green":
                if player.remainingGreenWalls > 0:
                    if 0 <= x + 1 < len(obj.table_fields) and 0 <= y < len(obj.table_fields[0]):
                        wall_object = Wall()
                        wall = wall_object.make_wall(inp, pos)
                        if obj.table_fields[x][y].wallRight["type"] == "green":
                            return -1
                        elif obj.table_fields[x + 1][y].wallRight["type"] == "green":
                            return -1
                        elif obj.table_fields[x][y].wallDown["type"] == "blue":
                            return -1
                        else:
                            copied_matrix = deep_copy_table(obj, obj.x, obj.y)
                            return_param = copied_matrix.update_field_for_green(x, y, x + 1, wall)
                            if return_param:
                                has_path = wall_object.check_if_there_are_paths(copied_matrix)
                                #has_path = True
                                if has_path:
                                    if figure == 'player1':
                                        obj.player1.remainingGreenWalls = obj.player1.remainingGreenWalls - 1
                                        obj.player1.figure1.positionX = move[0]
                                        obj.player1.figure1.positionY = move[1]
                                        obj.update_field_for_green(x, y, x + 1, wall)
                                    else:
                                        obj.player2.remainingGreenWalls = obj.player2.remainingGreenWalls - 1
                                        obj.player2.figure1.positionX = move[0]
                                        obj.player2.figure1.positionY = move[1]
                                        obj.update_field_for_green(x, y, x + 1, wall)
                                    return obj
                                else:
                                    return -1
                            else:
                                return -1
                    else:
                        return -1
                else:
                    if figure == 'player1':
                        obj.player1.figure1.positionX = move[0]
                        obj.player1.figure1.positionY = move[1]
                    else:
                        obj.player2.figure1.positionX = move[0]
                        obj.player2.figure1.positionY = move[1]
                    return obj
            else:
                return -1
        else:
            return -1


    def all_states_based_on_move(self, obj, move, figure):
        """
            Funkcija koja pronalazi stanja na osnovu poteza.
        """
        list_of_states = []
        if figure == 'player1':
            player = obj.player1
        else:
            player = obj.player2
        for i in range(obj.x):
            for j in range(obj.y):
                returned_value = self.new_state_of_game(obj, i, j, 'blue', player, move, figure)
                if returned_value != -1:
                    list_of_states.append(returned_value)

        for i in range(obj.x):
            for j in range(obj.y):
                returned_value = self.new_state_of_game(obj, i, j, 'green', player, move, figure)
                if returned_value != -1:
                    list_of_states.append(returned_value)

        bra = list_of_states.pop(0)
        return list_of_states


    def determinate_possible_state(self, obj, figure):
        """
            Funkcija koja vraca sva moguca stanja igre.
        """

        list_of_possible_states = []

        list_of_possible_moves = []
        moves = ['levo', 'desno', 'gore', 'dole', 'dijagonalaGore_levo', 'dijagonalaGore_desno', 'dijagonalaDole_levo', 'dijagonalaDole_desno']

        if figure == 'player1':
            for move in moves:
                value = obj.player1.figure1.is_valid_move_for_node(obj.player1.figure1.positionX,
                                                                     obj.player1.figure1.positionY,
                                                                     obj,
                                                                     move)
                list_of_possible_moves.append(value)
        else:
            for move in moves:
                value = obj.player2.figure1.is_valid_move_for_node(obj.player1.figure1.positionX,
                                                                   obj.player1.figure1.positionY,
                                                                   obj,
                                                                   move)
                list_of_possible_moves.append(value)


        for move in list_of_possible_moves:
            if move[0] is not False:
                new_matrix_state = deep_copy_table(obj, obj.x, obj.y)
                list_of_possible_states.append(self.all_states_based_on_move(new_matrix_state, move[1], figure))

        return list_of_possible_states

    def state_quality(self, current_state, maximazing_player):

        if maximazing_player is True:
            value_of_state = random.randint(0, 1000)
        else:
            value_of_state = random.randint(-1000, -1)

        return value_of_state, current_state

    def MAX(self, best, val):
        if best[0] < val[0]:
            return val
        else:
            return best

    def MIN(self, best, val):
        if best[0] > val[0]:
            return val
        else:
            return best

    def min_max(self, matrix_state, depth, maximizing_player, alpha, beta, figure):
        if depth == 0:
            return self.state_quality(matrix_state, maximizing_player)

        list_of_moves = self.determinate_possible_state(matrix_state, figure)

        if maximizing_player:
            best = [MIN]

            for moves in list_of_moves:
                for move in moves:
                    val = self.min_max(move, depth - 1, False, alpha, beta, figure)
                    best = self.MAX(best, val)
                    alpha = max(alpha, best[0])

                    if beta <= alpha:
                        break
            return best
        else:
            best = [MAX]

            for moves in list_of_moves:
                for move in moves:
                    val = self.min_max(move, depth - 1, True, alpha, beta, figure)
                    best = self.MIN(best, val)
                    beta = min(beta, best[0])
                    if beta <= alpha:
                        break
            return best

