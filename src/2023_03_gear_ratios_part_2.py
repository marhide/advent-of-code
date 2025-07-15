from itertools import product
from math import prod

def get_sum_of_correct_numbers(data):
    sum_of_correct_numbers = 0
    coord_range = list(product(range(len(data)), repeat=2))

    for i, j in coord_range:
        if data[i][j] == '*':
            adjacent_number_coords = []

            for new_coord in product((i-1, i, i+1), (j-1, j, j+1)):
                if new_coord in coord_range:
                    char = data[new_coord[0]][new_coord[1]]
                    if char.isnumeric():
                        adjacent_number_coords.append({char: new_coord})

            print(adjacent_number_coords)


            numbers = []
            
            for item in adjacent_number_coords:
                y, x = list(item.values())[0]
                number = ''
                for new_coord in product((x-1, x, x+1), [y]):
                    if new_coord in coord_range:
                        char = data[new_coord[0]][new_coord[1]]
                        if char.isnumeric():
                            number += char
                if number:
                    numbers.append(int(number))


            print(numbers)



            if len(numbers) == 2:
                sum_of_correct_numbers += prod(numbers)

    return sum_of_correct_numbers


        
if __name__ == '__main__':
    with open('data/2023_03_input.txt', 'r') as f:
        data = [l.strip() for l in f]


    part_2 = get_sum_of_correct_numbers(data)
    print(part_2)