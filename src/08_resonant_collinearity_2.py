def get_antinode_count(data):
    unique_chars = sorted(tuple(set(char for char in ''.join(data) if char != '.')))
    coords_dict = {char: [] for char in unique_chars}
    y_range = range(1, len(data)+1)
    x_range = range(1, len(data[0])+1)
 
    for y in y_range:
        for x in x_range:
            if data[y-1][x-1] != '.':
                coords_dict[data[y-1][x-1]].append((x, y))

    count = 0
    antinode_list = []

    for k in coords_dict:
        print(f'\n\n{k}: {coords_dict[k]}\n')
        for i in range(1, len(coords_dict[k])+1):
            x, y = coords_dict[k][i-1]
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x, comparison_y = coords_dict[k][j]
                    x_antinode = x - (comparison_x - x)
                    y_antinode = y - (comparison_y - y)

                    multiplier_counter = 0
                    new_x_antinode = x_antinode
                    new_y_antinode = y_antinode
                    new_neg_x_antinode = x_antinode
                    new_neg_y_antinode = y_antinode
                    
                    while new_x_antinode in x_range and new_y_antinode in y_range:
                        multiplier_counter += 1

                        new_x_antinode = multiplier_counter*x_antinode
                        new_y_antinode = multiplier_counter*y_antinode
                        antinode_coord = (new_x_antinode, new_y_antinode)

                        print(antinode_coord)
                        if antinode_coord not in antinode_list:
                            antinode_list.append(antinode_coord)
                            count += 1
                        
                    multiplier_counter = 0

                    while new_neg_x_antinode in x_range and new_neg_y_antinode in y_range:
                        multiplier_counter += 1

                        new_neg_x_antinode = int(x_antinode/multiplier_counter)
                        new_neg_y_antinode = int(y_antinode/multiplier_counter)
                        antinode_coord = (new_neg_x_antinode, new_neg_y_antinode)

                        print(antinode_coord)
                        if antinode_coord not in antinode_list:
                            antinode_list.append(antinode_coord)
                            count += 1

    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)