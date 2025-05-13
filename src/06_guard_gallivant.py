def add_border_to_table(table):
    table = ['E'+row+'E' for row in table]
    end_row = ''.join(['E' for _ in range(len(table[0]))])
    table = [end_row]+table+[end_row]
    return table


def get_starting_positions(table):
    for col_index in range(len(table)):
        for row_index in range(len(table[col_index])):
            if table[col_index][row_index] == '^':
                return col_index, row_index


def get_unique_position_count(table):

    table = add_border_to_table(table)
    col_index, row_index = get_starting_positions(table)
    coords_visited = []
    direction_index = 0

    while table[col_index][row_index] != 'E':
        match direction_index:
            case 0:
                col_index -= 1
            case 1:
                row_index += 1
            case 2:
                col_index += 1
            case 3:
                row_index -= 1

        if table[col_index][row_index] == '#':
            match direction_index:
                case 0: 
                    col_index += 1
                case 1:
                    row_index -= 1
                case 2:
                    col_index -= 1
                case 3:
                    row_index += 1

            direction_index += 1
            if direction_index > 3:
                direction_index = 0

        coords_visited.append((col_index, row_index))

    #     table[col_index] = table[col_index][:row_index]+"X"+table[col_index][row_index+1:]
    # for row in table: print(row)

    unique_position_count = len(set(coords_visited))
    return unique_position_count


if __name__ == '__main__':
    with open('data/06_input.txt', 'r', encoding='utf-8') as file:
        table = [line.strip() for line in file]

    print(get_unique_position_count(table))