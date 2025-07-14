with open('data/2024_02_input.txt', 'r', encoding='utf-8') as f:
    data = [list(map(int, l.strip().split(' '))) for l in f]


def is_report_safe(nums_list):
    r = range(len(nums_list)-1)

    only_increases = all([nums_list[i]<nums_list[i+1] for i in r])
    only_decreases = all([nums_list[i]>nums_list[i+1] for i in r])
    only_linear_changes = only_increases ^ only_decreases

    changes_in_bounds = all([nums_list[i]-nums_list[i+1] in range(-3, 4) for i in r])

    report_safe = only_linear_changes and changes_in_bounds
    return report_safe


def problem_dampener(num_list):

    if is_report_safe(num_list):
        return True

    for i in range(len(num_list)):
        current_list = num_list.copy()
        current_list.pop(i)
        if is_report_safe(current_list):
            return True
    
    return False


part_1 = len(tuple(filter(is_report_safe, data)))
part_2 = len(tuple(filter(problem_dampener, data)))
print(f'part 1: {part_1}\npart 2: {part_2}')