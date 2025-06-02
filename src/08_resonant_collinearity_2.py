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
        for i in range(len(coords_dict[k])):
            x, y = coords_dict[k][i]
            for j in range(len(coords_dict[k])):
                if i != j:
                    comparison_x, comparison_y = coords_dict[k][j]
                    x_antinode = x - (comparison_x - x)
                    y_antinode = y - (comparison_y - y)

                    # print(f'\ni: {i}, j: {j} -- {x_antinode in x_range and y_antinode in y_range}\nx: {x}, comp x: {comparison_x}, x antinode: {x_antinode}, x antinode in range: {x_antinode in x_range}\ny: {y}, comp y: {comparison_y}, y antinode: {y_antinode}, y antinode in range: {y_antinode in y_range}\n')

                    multiplier_counter = 1
                    while x_antinode in x_range and y_antinode in y_range:

                        antinode_coord = (x_antinode, y_antinode)

                        print(antinode_coord)
                        if antinode_coord not in antinode_list:
                            antinode_list.append(antinode_coord)
                            count += 1

                        multiplier_counter += 1
                        x_antinode = x - ((comparison_x - x)*multiplier_counter)
                        y_antinode = y - ((comparison_y - y)*multiplier_counter)
                        

    return count

if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]

    count = get_antinode_count(data)
    print(count)