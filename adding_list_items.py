list_num1 = [122, 227, 339, 722, 114]
list_num2 = [121, 212, 483, 777]

max_len = max(len(list_num1), len(list_num2))

list1 = list_num1 + [0] * (max_len - len(list_num1))
list2 = list_num2 + [0] * (max_len - len(list_num2))

result = [list1[i] + list2[i] for i in range(max_len)]

print(result) #[243, 439, 822, 1499, 114]