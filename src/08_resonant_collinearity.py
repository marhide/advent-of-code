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
    y_range = range(1, 51)
    x_range = range(1, 51)
    for k in coords_dict:
        print(f'\n\n{k}: {coords_dict[k]}\n')
        for i in range(len(coords_dict[k])):
            x = coords_dict[k][i][0]
            y = coords_dict[k][i][1]
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x = coords_dict[k][j][0]
                    comparison_y = coords_dict[k][j][1]
                    x_antinode = x - (comparison_x - x)
                    y_antinode = y - (comparison_y - y)

                    print(f'i: {i}, j: {j} - {x_antinode in x_range and y_antinode in y_range}\nx: {x}, comp x: {comparison_x}, x antinode: {x_antinode}, x antinode in range: {x_antinode in x_range}\ny: {y}, comp y: {comparison_y}, y antinode: {y_antinode}, y antinode in range: {y_antinode in y_range}\n')
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