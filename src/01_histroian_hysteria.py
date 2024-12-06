left_list, right_list = [], []

with open('data/01_input.txt', 'r', encoding='utf-8') as f:
    for l in f:
        nums = l.split('   ')
        num_1 = int(nums[0].strip())
        num_2 = int(nums[1].strip())
        left_list.append(num_1)
        right_list.append(num_2)

#part 1 answer
num_pairs = zip(sorted(left_list), sorted(right_list))
diff_calc = lambda num_pair: abs(num_pair[0]-num_pair[1])
sum_of_differences = sum(map(diff_calc, num_pairs))

#part 2 answer
left_in_right_similarity_calc = lambda num: num*right_list.count(num)
similarity_score = sum(map(left_in_right_similarity_calc, set(left_list)))

print(f'part 1: {sum_of_differences}\npart 2: {similarity_score}')