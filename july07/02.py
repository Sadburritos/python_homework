number_list = [3, 9, 8, 4, 5, 1]
min_index = number_list.index(min(number_list))
max_index = number_list.index(max(number_list))
number_list[min_index], number_list[max_index] = number_list[max_index], number_list[min_index]
print("Список после обмена:", number_list)
