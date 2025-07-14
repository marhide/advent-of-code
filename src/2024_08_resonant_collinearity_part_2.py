from itertools import permutations, product


def get_antinode_count(data):
    unique_chars = {char for char in str(data) if char.isalnum()}
    coord_range = range(len(data))
    coords_dict = {char: [(x, y) for x, y in product(coord_range, repeat=2) if data[y][x] == char] for char in unique_chars}

    antinode_set = set()

    for k in coords_dict:
        for node, comparison_node in permutations(coords_dict[k], 2):
            distance_multiplier = 0
            x, y = node
            comparison_x, comparison_y = comparison_node
            while True:
                x_antinode = x-(distance_multiplier*(comparison_x-x))
                y_antinode = y-(distance_multiplier*(comparison_y-y))
                
                if x_antinode in coord_range and y_antinode in coord_range:
                    antinode_set.add((x_antinode, y_antinode))
                    distance_multiplier += 1
                else:
                    break

    count = len(antinode_set)
    return count


if __name__ == '__main__':
    with open('data/2024_08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)