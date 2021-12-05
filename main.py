from TableFields import TableFields
from wall import Wall

if __name__ == '__main__':
    obj = TableFields()
    wallObj = Wall()
    obj.init_game_table()
    updated_matrix = wallObj.init_wall(obj.table_fields)
    obj.print_game_table()
