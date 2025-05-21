from pprint import pprint

def get_coords_dict(data):
    unique_chars = sorted(tuple(set(char for char in ''.join(data) if char != '.')))
    coords_dict = {char: [] for char in unique_chars}

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != '.':
                coords_dict[data[y][x]].append((x, y))

    return coords_dict

def get_antinode_count(coords_dict, x_range, y_range):
    count = 0
    for k in coords_dict:
        for i in range(len(coords_dict[k])):
            x_coord = coords_dict[k][i][0]
            y_coord = coords_dict[k][i][1]
            for j in range(len(coords_dict[k])):
                if coords_dict[k][i] != coords_dict[k][j]:
                    next_x_coord = coords_dict[k][j][0]
                    next_y_coord = coords_dict[k][j][1]
                    x_antinode = x_coord + (x_coord - next_x_coord)
                    y_antinode = y_coord + (y_coord - next_y_coord)

                    if x_antinode in x_range and y_antinode in y_range:
                        count += 1

    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]
    y_range = range(len(data))
    x_range = range(len(data[0]))

    coords_dict = get_coords_dict(data)
    pprint(coords_dict)

    count = get_antinode_count(coords_dict, x_range, y_range)
    print(count)