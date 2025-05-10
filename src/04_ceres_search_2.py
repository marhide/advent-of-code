

def get_xmas_count(table):
    count = 0
    col_range = range(len(table))

    for col_index in col_range:
        row_range = range(len(table[col_index]))

        for row_index in row_range:

            for i in range(8):
                up = i in (0, 1, 7)
                down = i in (3, 4, 5)
                left = i in (5, 6, 7)
                right = i in (1, 2, 3)

                xmas_str = ''

                for j in range(4):
                    new_col_index = col_index-j if up else col_index+j if down else col_index
                    new_row_index = row_index-j if left else row_index+j if right else row_index

                    if new_col_index in col_range and new_row_index in row_range:
                        xmas_str += table[new_col_index][new_row_index]

                if xmas_str == 'XMAS':
                    count += 1

    return count


if __name__ == '__main__':
    with open('data/04_input.txt', 'r', encoding='utf-8') as file:
        table = [line.strip() for line in file]

    print(get_xmas_count(table))