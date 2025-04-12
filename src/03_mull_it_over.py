with open('data/03_input.txt', 'r', encoding='utf-8') as f:
    data = f.read()


def get_multiple(item):

    split_item = item.split(',')

    if len(split_item) > 1:

        item_1 = split_item[0]
        item_2 = split_item[1]
        num_1, num_2 = '', ''

        if len(item_1) in range(1,4) and item_1.isnumeric():
            for i in range(len(item_1)):
                if i in range(0,3) and item_1[i].isnumeric():
                    num_1 += item_1[i]

            for i in range(len(item_2)):
                if i in range(0,3) and item_2[i].isnumeric():
                    num_2 += item_2[i]
                elif i in range(1,4) and item_2[i] == ')':
                    output_multiple = int(num_1) * int(num_2)
                    return output_multiple

    return 0


def do_mul(data):
    do_mul_data = [item.split("don't()")[0] for item in data.split('do()')]
    do_mul_data_str = ''.join(do_mul_data)
    return do_mul_data_str

part_1 = sum(map(get_multiple, data.split('mul(')))
part_2 = sum(map(get_multiple, do_mul(data).split('mul(')))
print(f'part 1: {part_1}\npart 2: {part_2}')