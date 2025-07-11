def is_game_possible(game):
    game_list = game.replace(',', '').replace(';', '').split(' ')[:1:-1]
    maximum_number_for_colour = {'red': 12, 'green': 13, 'blue': 14}

    current_colour = ''
    for item in game_list:
        try:
            if int(item) > maximum_number_for_colour[current_colour]:
                return False
        except:
            current_colour = item

    return True


if __name__ == '__main__':
    with open('data/02_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    possible_games = filter(is_game_possible, data)

    get_game_id = lambda game: int(game.split(' ')[1][:-1])
    possible_game_ids_sum = sum(map(get_game_id, possible_games))

    print(f'part 1: {possible_game_ids_sum}')