with open('data/04_input.txt', 'r', encoding='utf-8') as f:
    data = [l.strip() for l in f]

def get_xmas_count(data):

    xmas_count = 0

    for x in range(len(data)):

        bottom_to_top_range = range(3, len(data))
        top_to_bottom_range = range(len(data)-3)
        left_to_right_range = range(len(data[x])-3)
        right_to_left_range = range(3, len(data[x]))

        for y in range(len(data[x])):

            #bottom to top vertical
            if x in bottom_to_top_range:
                if data[x][y]+data[x-1][y]+data[x-2][y]+data[x-3][y] == 'XMAS':
                    xmas_count += 1

            #bottom to top, left to right diagonal
            if x in bottom_to_top_range and y in left_to_right_range:
                if data[x][y]+data[x-1][y+1]+data[x-2][y+2]+data[x-3][y+3] == 'XMAS':
                    xmas_count += 1

            #left to right horizontal
            if y in left_to_right_range:
                if data[x][y]+data[x][y+1]+data[x][y+2]+data[x][y+3] == 'XMAS':
                    xmas_count += 1
            
            #top to bottom, left to right diagonal
            if x in top_to_bottom_range and y in left_to_right_range:
                if data[x][y]+data[x+1][y+1]+data[x+2][y+2]+data[x+3][y+3] == 'XMAS':
                    xmas_count += 1

            #top to bottom vertical
            if x in top_to_bottom_range:
                if data[x][y]+data[x+1][y]+data[x+2][y]+data[x+3][y] == 'XMAS':
                    xmas_count += 1

            #top to bottom, right to left diagonal
            if x in top_to_bottom_range and y in right_to_left_range:
                if data[x][y]+data[x+1][y-1]+data[x+2][y-2]+data[x+3][y-3] == 'XMAS':
                    xmas_count += 1

            #right to left horizontal
            if y in right_to_left_range:
                if data[x][y]+data[x][y-1]+data[x][y-2]+data[x][y-3] == 'XMAS':
                    xmas_count += 1

            #bottom to top, right to left diagonal
            if x in bottom_to_top_range and y in right_to_left_range:
                if data[x][y]+data[x-1][y-1]+data[x-2][y-2]+data[x-3][y-3] == 'XMAS':
                    xmas_count += 1

    return xmas_count

print(f'part 1: {get_xmas_count(data)}\npart 2: ')

def cross_mas_count(data):
    count = 0
    x_range = range(1, len(data)-1)
    print(str(x_range))
    # for x in range(1, len(data)-1):
    #     count += 1
    #     print(f"{count}/{len(data)}")

cross_mas_count(data)