def get_xmas_count(table):
    count = 0

    for col_index in range(len(table)):
        for row_index in range(len(table[col_index])):
            for i in range(8):
                up = i in (0, 1, 7)
                down = i in (3, 4, 5)
                right = i in (1, 2, 3)
                left = i in (5, 6, 7)

                xmas_str = ''

                for j in range(4):
                    new_col_index = col_index+j if down else col_index-j if up else col_index
                    new_row_index = row_index+j if right else row_index-j if left else row_index

                    try:
                        xmas_str += table[new_col_index][new_row_index]
                    except IndexError:
                        break

                    if xmas_str == 'XMAS':
                        count += 1
                        print(f"{xmas_str}, row_index: {row_index+1} col_index: {col_index+1},{' up' if up else ''}{' down' if down else ''}{' right' if right else ''}{' left' if left else ''}")

    return count


if __name__ == '__main__':

    with open('data/04_input.txt', 'r', encoding='utf-8') as f:
        table = [l.strip() for l in f]

    print(get_xmas_count(table))