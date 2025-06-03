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

    for k in coords_dict:
        print(f'\n\n{k}: {coords_dict[k]}\n')
        for i in range(len(coords_dict[k])):
            x, y = coords_dict[k][i]
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x, comparison_y = coords_dict[k][j]
                    counter = 0
                    while True:
                        counter += 1
                        x_antinode = x - ((comparison_x - x)*counter)
                        y_antinode = y - ((comparison_y - y)*counter)
                        antinode_coord = (x_antinode, y_antinode)
                        if x_antinode not in x_range or y_antinode not in y_range:
                            break
                        antinode_list.append(antinode_coord)
    count = len(set(antinode_list))
    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)