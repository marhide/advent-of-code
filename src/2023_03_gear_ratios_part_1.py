from itertools import product


def get_sum_of_correct_numbers(data):
    symbols = {char for char in ''.join(data) if char not in '.0123456789'}
    sum_of_correct_numbers = 0
    coord_range = range(len(data))

    for i in coord_range:
        j = 0

        while j in coord_range:
            coords_of_number = []

            while j in coord_range:
                char = data[i][j]
                coord = (i, j)
                j += 1
                if char.isnumeric():
                    coords_of_number.append(coord)
                else:
                    break
            
            if coords_of_number:
                break_flag = False
                for y, x in coords_of_number:
                    if break_flag:
                        break

                    for new_y, new_x in product([y-1, y, y+1], [x-1, x+1]):
                        if new_y in coord_range and new_x in coord_range:
                            if data[new_y][new_x] in symbols:
                                number = int(''.join([data[y][x] for y, x in coords_of_number]))
                                sum_of_correct_numbers += number
                                break_flag = True
                                break

    return sum_of_correct_numbers


if __name__ == '__main__':
    with open('data/2023_03_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    part_1 = get_sum_of_correct_numbers(data)
    print(part_1)