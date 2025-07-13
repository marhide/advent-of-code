from itertools import product

def get_sum_of_correct_numbers(data):
    symbols = {char for char in ''.join(data) if char not in '.0123456789'}
    sum_of_correct_numbers = 0

    for line_number in range(len(data)):
        line_position = 0
        while line_position in range(len(data[line_number])):
            char = data[line_number][line_position]
            index = 0
            coords_of_number = []
            while True:
                if line_position+index in range(len(data[line_position])):
                    char = data[line_number][line_position+index]
                    if char.isnumeric():
                        coords_of_number.append((line_number, line_position+index))
                        index += 1
                    else:
                        break
                else:
                    break
            line_position += 1 + index
            
            if coords_of_number:
                breaker = False
                for y, x in coords_of_number:
                    if breaker: break
                    for new_y, new_x in product([-1, 0, 1], repeat=2):
                        if y+new_y in range(len(data)) and x+new_x in range(len(data[line_number])):
                            if data[y+new_y][x+new_x] in symbols:
                                number = int(''.join([data[y][x] for y, x in coords_of_number]))
                                sum_of_correct_numbers += number
                                breaker = True
                                break
  
    return sum_of_correct_numbers

if __name__ == '__main__':
    with open('data/03_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    part_1 = get_sum_of_correct_numbers(data)
    print(part_1)