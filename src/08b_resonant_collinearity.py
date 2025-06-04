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

    print_maps = []
    for k in coords_dict:
        print_map = [['.' for _ in coord_range] for _ in coord_range]
        for node, comparison_node in permutations(coords_dict[k], 2):
            distance_multiplier = 1
            x, y = node
            print_map[y][x] = k
            comparison_x, comparison_y = comparison_node
            while True:
                x_antinode = x-(distance_multiplier*(comparison_x-x))
                y_antinode = y-(distance_multiplier*(comparison_y-y))
                if x_antinode in coord_range and y_antinode in coord_range:
                    antinode_coord_set.add((x_antinode, y_antinode))
                    print_map[y_antinode][x_antinode] = '#'
                    distance_multiplier += 1
                else:
                    break
        print_maps.append('\n'.join([''.join(item) for item in print_map]))

    with open('data/08b_output.txt', 'w') as f: f.write('\n\n'.join(print_maps))
    count = len(antinode_coord_set)
    return count




    # print_maps = []
    # for k in coords_dict:
    #     print_map = [['.' for _ in coord_range] for _ in coord_range]
    #     for i in range(len(coords_dict[k])):
    #         x, y = coords_dict[k][i]
    #         print_map[y][x] = k
    #         for j in range(len(coords_dict[k])):
    #             if i != j:
    #                 comparison_x, comparison_y = coords_dict[k][j]
    #                 distance_multiplier = 1
    #                 x_antinode = x - (comparison_x - x)
    #                 y_antinode = y - (comparison_y - y)
    #                 while x_antinode in coord_range and y_antinode in coord_range:
    #                     antinode_coord_set.add((x_antinode, y_antinode))
    #                     print_map[y_antinode-1][x_antinode-1] = '#'
    #                     distance_multiplier += 1
    #                     x_antinode = x - ((comparison_x - x)*distance_multiplier)
    #                     y_antinode = y - ((comparison_y - y)*distance_multiplier)
    #     print_maps.append('\n'.join([''.join(item) for item in print_map]))
    # with open('data/08b_output.txt', 'w') as f: f.write('\n\n'.join(print_maps))
    # count = len(antinode_coord_set)
    # return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)