with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    order_list = [l.strip() for l in f if '|' in l]
    order_dict = {l.split('|')[0]: [] for l in order_list}
    order_pair_tuple_list = [(l.split('|')[0], l.split('|')[1]) for l in order_list]

    for pair in order_pair_tuple_list:
        if pair[0] in order_dict:
            order_dict[pair[0]].append(pair[1])

with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    updates_list = [l.strip().split(',') for l in f if ',' in l]

correct_middle_pages = []
for update in updates_list:
    pages_checked = []
    is_update_correct = True
    for page in update:
        if page in order_dict:
            pages_checked.append(page)
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    # print(f'{", ".join(update)} is incorrect: {incorrect_page} cannot come before {page}')
                    is_update_correct = False
                    break
            if not is_update_correct:
                break

    if is_update_correct:
        middle_index = int(len(update)/2)
        correct_middle_pages.append(int(update[middle_index]))
    
print(sum(correct_middle_pages))