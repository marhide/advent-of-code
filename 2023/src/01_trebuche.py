def return_calibration_value(calibration_line):
    calibration_value_list = list(filter(str.isdigit, calibration_line))
    calibration_value_int = int(calibration_value_list[0]+calibration_value_list[-1])

    return calibration_value_int


if __name__ == '__main__':
    with open('data/01_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    part_1 = sum(map(return_calibration_value, data))
    part_2 = ''

    print(f'part 1: {part_1}\npart 2: {part_2}')
