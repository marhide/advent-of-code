with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    order_list = [l.strip() for l in f if '|' in l]
    order_tuple_list = [(l.split('|')[0], l.split('|')[1]) for l in order_list]
    order_dict = {l.split('|')[0]: [] for l in order_list}

    for item in order_tuple_list:
        if item[0] in order_dict:
            order_dict[item[0]].append(item[1])

with open('data/05_input.txt', 'r', encoding='utf-8') as f:
    updates_list = [l.strip() for l in f if ',' in l]

# print(order_dict)
# print(updates_list)


correct_updates = []
for update in updates_list:
    pages_checked = []
    is_update_correct = True
    for page in update.split(','):
        if page in order_dict:
            for incorrect_page in order_dict[page]:
                if incorrect_page in pages_checked:
                    is_update_correct = False
                    print(f'{update} is incorrect, {incorrect_page} cannot come before {page}')
            pages_checked.append(page)
        if not is_update_correct:
            break
                
    if is_update_correct:
        correct_updates.append(update)
        print(f'{update} is correct')
    
middle_pages = []
for update in correct_updates:
    update_list = update.split(',')
    middle_index = int(len(update_list)/2)
    middle_pages.append(int(update_list[middle_index]))
    

print(sum(middle_pages))