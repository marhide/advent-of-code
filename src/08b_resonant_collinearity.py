from itertools import permutations

def get_antinode_count(data):
    unique_chars = sorted(tuple(set(char for char in ''.join(data) if char != '.')))
    coords_dict = {char: [] for char in unique_chars}
    coord_range = range(len(data))
 
    for y in coord_range:
        for x in coord_range:
            if data[y][x] != '.':
                coords_dict[data[y][x]].append((x, y))

    antinode_coord_set = set()

    for k in coords_dict:
        for node, comparison_node in permutations(coords_dict[k], 2):
            distance_multiplier = 0
            x, y = node
            comparison_x, comparison_y = comparison_node
            while True:
                x_antinode = x-(distance_multiplier*(comparison_x-x))
                y_antinode = y-(distance_multiplier*(comparison_y-y))
                if x_antinode in coord_range and y_antinode in coord_range:
                    antinode_coord_set.add((x_antinode, y_antinode))
                    distance_multiplier += 1
                else:
                    break
    count = len(antinode_coord_set)
    return count


if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)