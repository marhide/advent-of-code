def get_xmas_count(table):
    count = 0
    col_range = range(len(table))

    for col in col_range:
        row_range = range(len(table[col]))

        for row in row_range:

            for i in range(8):
                up = i in (0, 1, 7)
                down = i in (3, 4, 5)
                left = i in (5, 6, 7)
                right = i in (1, 2, 3)

                xmas_str = ''

                for j in range(4):
                    new_col = col-j if up else col+j if down else col
                    new_row = row-j if left else row+j if right else row
                    
                    if new_col in col_range and new_row in row_range:
                        xmas_str += table[new_col][new_row]

                if xmas_str == 'XMAS':
                    count += 1

    return count


def get_cross_mas_count(table):
    count = 0

    for col in range(1, len(table)-1):
        row_range = range(1, len(table[col])-1)

        for row in row_range:
            if table[col][row] == 'A':

                top_l = table[col-1][row-1]
                top_r = table[col-1][row+1]
                btm_l = table[col+1][row-1]
                btm_r = table[col+1][row+1]

                cross_str = top_l + top_r + btm_l + btm_r

                if cross_str in ('SSMM', 'MMSS', 'SMSM', 'MSMS'):
                    count += 1

    return count


if __name__ == '__main__':
    with open('data/04_input.txt', 'r', encoding='utf-8') as file:
        table = [line.strip() for line in file]

    print(f'part 1: {get_xmas_count(table)}\npart 2: {get_cross_mas_count(table)}')