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

    correct_line = ''
    letters = ''

    for char in calibration_line:

        if char.isalpha():
            letters += char

        if letters in number_lookup:
            correct_line += number_lookup[letters]
            letters = ''

        elif char.isnumeric():
            correct_line += char
            letters = ''
        
    print(calibration_line, correct_line)


    return correct_line

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
