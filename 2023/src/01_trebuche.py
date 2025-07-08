def replace_written_number_with_int(calibration_line):
    number_lookup = {'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}

    numbers = ''

    for i in range(len(calibration_line)):
        if calibration_line[i].isnumeric():
            numbers += calibration_line[i]
        else:    
            for j in range(i, len(calibration_line)+1):
                if calibration_line[i:j] in number_lookup:
                    numbers += number_lookup[calibration_line[i:j]]
    
    print(numbers)
    
        
    return numbers

def return_calibration_value(calibration_line):
    calibration_value_list = list(filter(str.isdigit, calibration_line))
    calibration_value_int = int(calibration_value_list[0]+calibration_value_list[-1])

    return calibration_value_int


if __name__ == '__main__':
    with open('data/01_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    part_1 = sum(map(return_calibration_value, data))
    corrected_data = map(replace_written_number_with_int, data)
    part_2 = sum(map(return_calibration_value, corrected_data))

    print(f'part 1: {part_1}\npart 2: {part_2}')
