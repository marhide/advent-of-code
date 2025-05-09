with open('data/04_test_input_2.txt', 'r', encoding='utf-8') as f:
    data = [l.strip() for l in f]

'''
0 -y         up
1 -y and +x  up right
2 +x         right
3 +y and +x  down right
4 +x         down
5 +y and -x  down left
6 -x         left
7 -y and -x  up left
'''

def get_xmas_count(data):
    count = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            for i in range(8):
                up = i in (0, 1, 7)
                down = i in (3, 4, 5)
                right = i in (1, 2, 3)
                left = i in (5, 6, 7)

                xmas_str = ''

                for j in range(4):
                    new_y = y+j if down else y-j if up else y
                    new_x = x+j if right else x-j if left else x

                    try:
                        xmas_str += data[new_y][new_x]
                    except IndexError:
                        break

                    if xmas_str == 'XMAS':
                        count += 1
                        print(f"{xmas_str}, x: {x+1} y: {y+1},{' up' if up else ''}{' down' if down else ''}{' right' if right else ''}{' left' if left else ''}")

    return count


print(get_xmas_count(data))