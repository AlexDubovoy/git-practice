def sum_lists(list1, list2):
    """
    Складывает соответствующие элементы 2х списков.
    Если списки разной длины, недостающие элементы считаются как 0.
    """
    max_len = max(len(list1), len(list2))

    extended_list1 = list1 + [0] * (max_len - len(list1))
    extended_list2 = list2 + [0] * (max_len - len(list2))

    result = [extended_list1[i] + extended_list2[i] for i in range(max_len)]

    return result

# Пример:
list_num1 = [120, 220, 330, 766, 333]
list_num2 = [111, 211, 411, 11]

result = sum_lists(list_num1, list_num2)
print(result)  #[231, 431, 741, 777, 333]