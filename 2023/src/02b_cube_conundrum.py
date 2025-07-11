def get_power_of_game(game):
    game_list = game.replace(',', '').replace(';', '').split(' ')[:1:-1]
    highest_number_for_colour = {'red': 0, 'green': 0, 'blue': 0}

    current_colour = ''
    for item in game_list:
        if item.isnumeric():
            if int(item) > highest_number_for_colour[current_colour]:
                highest_number_for_colour[current_colour] = int(item)
        else:
            current_colour = item

    power_of_game = 1
    for key in highest_number_for_colour:
        power_of_game *= highest_number_for_colour[key]

    return power_of_game


if __name__ == '__main__':
    with open('data/02_input.txt', 'r') as f:
        data = [l.strip() for l in f]

    total_power_of_games = sum(map(get_power_of_game, data))

    print(f'part 2: {total_power_of_games}')