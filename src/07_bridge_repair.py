def get_operator_sequence_permutations(number_of_sequences, current_sequence=''):
    if len(current_sequence) == number_of_sequences:
        return current_sequence
    else:
        output = get_operator_sequence_permutations(number_of_sequences, current_sequence+'+')+' '
        output += get_operator_sequence_permutations(number_of_sequences, current_sequence+'*')
        return output
    

def check_if_equation_possible(item):
    equation_possible = False
    result = item[0]
    equation = item[1]
    number_of_operators = len(equation)-1

    operator_sequence_permutations = get_operator_sequence_permutations(number_of_operators).split(' ')

    for i in range(len(operator_sequence_permutations)):
        total = equation[0]
        operator_sequence = operator_sequence_permutations[i]

        for j in range(number_of_operators):
            operator = operator_sequence[j]
            number = equation[j+1]
            if operator == '+':
                total += number
            elif operator == '*':
                total *= number

        if total == result:
            equation_possible = True

    return equation_possible


if __name__ == '__main__':
    with open('data/07_input.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(': ') for line in file]
        data = [[int(item[0]), tuple(map(int, item[1].split(' ')))] for item in data]

    part_1 = sum(map(lambda item: item[0], filter(check_if_equation_possible, data)))
    print(f'part 1: {part_1}\npart 2: {""}')