def get_antinode_count(data):
    unique_chars = sorted(tuple(set(char for char in ''.join(data) if char != '.')))
    coords_dict = {char: [] for char in unique_chars}
    coord_range = range(len(data))
 
    for y in coord_range:
        for x in coord_range:
            if data[y][x] != '.':
                coords_dict[data[y][x]].append((x, y))

    antinode_list = []

    for k in coords_dict:
        print(f'\n\n{k}: {coords_dict[k]}\n')
        new_map = [['.' for _ in coord_range] for _ in coord_range]
        for i in range(len(coords_dict[k])):
            x, y = coords_dict[k][i]
            new_map[y][x] = k
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x, comparison_y = coords_dict[k][j]
                    x_antinode = x - (comparison_x - x)
                    y_antinode = y - (comparison_y - y)

                    print(f'i: {i}, j: {j} -- {x_antinode in coord_range and y_antinode in coord_range}\nx: {x}, comp x: {comparison_x}, x antinode: {x_antinode}, x antinode in range: {x_antinode in coord_range}\ny: {y}, comp y: {comparison_y}, y antinode: {y_antinode}, y antinode in range: {y_antinode in coord_range}\n')
                    
                    if x_antinode in coord_range and y_antinode in coord_range:
                        antinode_list.append((x_antinode, y_antinode))
                        
                        new_map[y_antinode][x_antinode] = '#'
    
        print('\n'.join(''.join(item) for item in new_map))
    count = len(set(antinode_list))
    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)