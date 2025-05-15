
from pprint import pprint


def get_all_operator_combinaton_list(maxLength, s=""):
    if len(s) == maxLength:
        return s
    else:
        temp = get_all_operator_combinaton_list(maxLength, s + "+") + "\n"
        temp += get_all_operator_combinaton_list(maxLength, s + "*")
        return temp
    
def check_if_equation_possible(item):

    result = item[0]
    equation = item[1]
    number_of_permuations = len(equation)**2



    # print(equation, allBinaryPossiblities(len(equation)-1))

    operator_list = get_all_operator_combinaton_list(len(equation)-1).split('\n')
    print(equation, operator_list)

    # operations_list.append(equation)
    total = 0
    for i in range(len(operator_list)):
        total = equation[0]
        for j in range(len(equation[1::])):
            if operator_list[i][j] == "+":
                total += equation[j]
            elif operator_list[i][j] == "*":
                total *= equation[j]
        if total == result:
            print(total, result, number_of_permuations)
            return True
        
    return False

    # for i in range(number_of_permuations):
    #     new_list = []
    #     total = equation[0]
    #     for j in range(len(equation)):
            # if j:
            #     if i%j:
            #         new_list.append('0')
            #         total += equation[j]
            #     else: 
            #         new_list.append('1')
            #         total *= equation[j]

        # new_list.append('   '+str(i))


        # operations_list.append(' '.join(new_list))




    # pprint(operations_list)
    # print(equation, len(set(operations_list)), len(operations_list))


if __name__ == '__main__':
    with open('data/07_input.txt', 'r', encoding='utf-8') as file:
        data = [line.strip().split(': ') for line in file]
        data = [[int(item[0]), list(map(int, item[1].split(' ')))] for item in data]

    part_1 = sum(list(item[0] for item in (filter(check_if_equation_possible, data))))

    print(part_1)


