from itertools import permutations, product


def get_antinode_count(data):
    unique_chars = {char for char in ''.join(data) if char != '.'}
    coord_range = range(len(data))
    coords_dict = {char: [(x, y) for y, x in product(coord_range, repeat=2) if data[y][x] == char] for char in unique_chars}
    print(coords_dict)
 
    antinode_set = set()

    for k in coords_dict:
        for node, compairson_node in permutations(coords_dict[k], 2):
            x, y = node
            comparison_x, comparison_y = compairson_node
            x_antinode = x - (comparison_x - x)
            y_antinode = y - (comparison_y - y)

            if x_antinode in coord_range and y_antinode in coord_range:
                antinode_set.add((x_antinode, y_antinode))
                
    count = len(antinode_set)
    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)