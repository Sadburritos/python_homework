number_list = [3, 9, 8, 4, 5, 1]
result_list = [number_list[i] for i in range(1, len(number_list)) if number_list[i] > number_list[i - 1]]
print("Элементы, большие предыдущих:", result_list)