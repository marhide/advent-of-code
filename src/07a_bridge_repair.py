def get_operator_sequence_permutations(number_of_sequences, current_sequence=''):
    if len(current_sequence) == number_of_sequences:
        return current_sequence
    else:
        output = get_operator_sequence_permutations(number_of_sequences, current_sequence+'+')+' '
        output += get_operator_sequence_permutations(number_of_sequences, current_sequence+'*')
        return output
    

def is_equation_possible(item):
    result = item[0]
    number_list = item[1]
    number_of_operators = len(number_list)-1

    operator_sequence_permutations = get_operator_sequence_permutations(number_of_operators).split(' ')

    for operator_sequence in operator_sequence_permutations:
        total = number_list[0]
        for i in range(number_of_operators):
            operator = operator_sequence[i]
            number = number_list[i+1]
            if operator == '+':
                total += number
            elif operator == '*':
                total *= number

        if total == result:
            return True

    return False


if __name__ == '__main__':
    with open('data/07_input.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(': ') for line in file]
        data = [(int(item[0]), tuple(map(int, item[1].split(' ')))) for item in data]

    part_1 = sum(map(lambda item: item[0], filter(is_equation_possible, data)))
    print(f'part 1: {part_1}')