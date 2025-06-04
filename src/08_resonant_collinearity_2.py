from pprint import pprint

def get_antinode_count(data):
    unique_chars = sorted(tuple(set(char for char in ''.join(data) if char != '.')))
    coords_dict = {char: [] for char in unique_chars}
    y_range = range(1, len(data)+1)
    x_range = range(1, len(data[0])+1)
 
    for y in y_range:
        for x in x_range:
            if data[y-1][x-1] != '.':
                coords_dict[data[y-1][x-1]].append((x, y))

    antinode_list = []

    print_maps = []
    for k in coords_dict:
        print_map = [['.' for _ in x_range] for _ in y_range]
        for i in range(len(coords_dict[k])):
            x, y = coords_dict[k][i]
            print_map[y-1][x-1] = k
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x, comparison_y = coords_dict[k][j]
                    counter = 1
                    x_antinode = x - (comparison_x - x)
                    y_antinode = y - (comparison_y - y)
                    while x_antinode in x_range and y_antinode in y_range:
                        antinode_list.append((x_antinode, y_antinode))
                        print_map[y_antinode-1][x_antinode-1] = '#'
                        counter += 1
                        x_antinode = x - ((comparison_x - x)*counter)
                        y_antinode = y - ((comparison_y - y)*counter)
        print_maps.append('\n'.join([''.join(item) for item in print_map]))
    with open('data/08_output.txt', 'w') as f: f.write('\n\n'.join(print_maps))
    count = len(set(antinode_list))
    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)