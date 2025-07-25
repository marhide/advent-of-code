from itertools import product


def is_equation_possible(item):
    result = item[0]
    number_list = item[1]
    operator_sequence_length = len(number_list)-1

    operator_sequence_permutations = product('+*|', repeat=operator_sequence_length)

    for operator_sequence in operator_sequence_permutations:
        total = number_list[0]
        for i in range(operator_sequence_length):
            operator = operator_sequence[i]
            number = number_list[i+1]
            
            match operator:
                case '+':
                    total += number
                case '*':
                    total *= number
                case '|':
                    total = int(f'{total}{number}')

        if total == result:
            return True

    return False


if __name__ == '__main__':
    with open('data/2024_07_input.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(': ') for line in file]
        data = [(int(item[0]), tuple(map(int, item[1].split(' ')))) for item in data]

    part_2 = sum(map(lambda item: item[0], filter(is_equation_possible, data)))
    print(f'part 2: {part_2}')