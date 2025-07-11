def is_game_possible(game):
    game_list = game.replace(',', '').replace(';', '').split(' ')[:1:-1]
    maximum_number_for_colour = {'red': 12, 'green': 13, 'blue': 14}

    current_colour = ''
    for item in game_list:
        if item.isnumeric():
            if int(item) > maximum_number_for_colour[current_colour]:
                return False
        else:
            current_colour = item

    return True


def get_game_id(game):
    game_id = int(game.split(' ')[1][:-1])
    return game_id


if __name__ == '__main__':
    with open('data/02_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    possible_games = filter(is_game_possible, data)
    possible_game_ids_sum = sum(map(get_game_id, possible_games))

    print(f'part 1: {possible_game_ids_sum}')