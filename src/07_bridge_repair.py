def check_if_equation_possible(item):

    result = item[0]
    equation = item[1]
    number_of_permuations = len(equation)**2

    total = equation[0]
    for i in range(1, number_of_permuations):
        for number in equation[1::]:
            total += number

        if total == result:
            print(total, result, number_of_permuations)
            return True

    # a+b+c
    # a*b+c
    # a+b*c
    # a*b*c
    
    return False


if __name__ == '__main__':
    with open('data/07_input.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(': ') for line in file]
        data = [[int(item[0]), list(map(int, item[1].split(' ')))] for item in data]

    part_1 = sum(list(item[0] for item in (filter(check_if_equation_possible, data))))

    print(part_1)


