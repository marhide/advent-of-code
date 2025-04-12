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

    for page in update:
        if page in order_dict:
            pages_checked.append(page)
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    return False
                
    return True


def update_corrector(update, fn_has_ran_before=False):

    if update_checker(update) and fn_has_ran_before:
        return update

    pages_checked = []

    for page in update:
        pages_checked.append(page)
        if page in order_dict:
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    update.remove(incorrect_page)
                    update.append(incorrect_page)
                    return update_corrector(update, True)


correct_updates = filter(update_checker, updates_list)
incorrect_updates = filter(lambda update: not update_checker(update), updates_list)
corrected_updates = map(update_corrector, incorrect_updates)

def sum_middle_pages(updates_list_to_sum):
    get_middle_page = lambda update: int(update[int(len(update)/2)])
    middle_pages = [get_middle_page(update) for update in updates_list_to_sum]
    return sum(middle_pages)

print(f'part 1: {sum_middle_pages(correct_updates)}\npart 2: {sum_middle_pages(corrected_updates)}')