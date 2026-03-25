list_num1 = [1, 7, 9, 22, 104]
list_num2 = [121, 212, 483, 777]

result = []

for i in range(min(len(list_num1), len(list_num2))):
    result.append(list_num1[i] + list_num2[i])

print(result)  # [122, 219, 492, 799]