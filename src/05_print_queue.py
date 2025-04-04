with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    order_list = [l.strip() for l in f if '|' in l]
    order_dict = {l.split('|')[0]: [] for l in order_list}
    order_pair_tuple_list = [(l.split('|')[0], l.split('|')[1]) for l in order_list]

    for pair in order_pair_tuple_list:
        if pair[0] in order_dict:
            order_dict[pair[0]].append(pair[1])
        

with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    updates_list = [l.strip().split(',') for l in f if ',' in l]


def update_checker(update):
    pages_checked = []
    is_update_correct = True
    for page in update:
        if page in order_dict:
            pages_checked.append(page)
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    is_update_correct = False
                    break
        if not is_update_correct:
            break
    return is_update_correct


counter = 0
def update_corrector(update):

    global counter

    if update_checker(update) and counter:
        # print (f"{update} is correct, {counter}")
        counter = 0
        return update

    counter += 1

    pages_checked = []
    for page in update:
        pages_checked.append(page)
        if page in order_dict:
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    # print(f'{", ".join(update)} is incorrect: {incorrect_page} cannot come before {page}')
                    update.remove(incorrect_page)
                    update.append(incorrect_page)
                    return update_corrector(update)


get_middle_page = lambda update: int(update[int(len(update)/2)])

def sum_middle_pages(updates_list_to_sum):
    middle_pages = []
    for update in updates_list_to_sum:
        middle_page = get_middle_page(update)
        middle_pages.append(middle_page)
    return sum(middle_pages)

correct_updates = filter(update_checker, updates_list)

incorrect_updates = filter(lambda update: not update_checker(update), updates_list)
corrected_updates = map(update_corrector, incorrect_updates)

print(f'part 1: {sum_middle_pages(correct_updates)}\npart 2: {sum_middle_pages(corrected_updates)}')