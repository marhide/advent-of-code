from pprint import pprint


def get_unique_chars(data):
    unique_chars = set(char for char in ''.join(data) if char != '.')
    unique_chars_sorted = sorted(tuple(unique_chars))
    return unique_chars_sorted


# def get_map_for_char(char_for_map):
#     accepted_chars = [char_for_map, '\n', '.']
#     new_map = [char if char in accepted_chars else '.' for char in data]
#     new_map_list = ''.join(new_map).split('\n')
#     return new_map_list



if __name__ == '__main__':
    with open('data/08_input.txt', 'r', encoding='utf-8') as f:
        data = [l.strip() for l in f]
        # data = f.read()

    unique_chars = get_unique_chars(data)
    # char_maps = map(get_map_for_char, unique_chars)


    coords_dict = {char: [] for char in unique_chars}
    # for char_map in char_maps:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != '.':
                coords_dict[data[y][x]].append((y, x))

    pprint(coords_dict)
    # pprint(list(char_maps))