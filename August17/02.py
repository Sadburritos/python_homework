# user_in = input("Введите числа через запятую: ")
# user_in = user_in.split(',')
# my_list = list(map(lambda x: int(x), user_in))

# sorted_list = []
# for _ in range(len(my_list)):
#     # min_elem = min(my_list)
#     # sorted_list.append(min_elem)
#     # del my_list[my_list.index(min_elem)]
#     min_index = 0
#     for k in range(1, len(my_list)):
#         if my_list[k] < my_list[min_index]:
#             min_index = k
#     sorted_list.append(my_list[min_index])
#     del my_list[min_index]


# my_list = sorted_list
# print(my_list)

def selection_sort(the_list, key=None):
    sorted_list = []

    for _ in range(len(the_list)):
        min_index = 0
        for i in range(1, len(the_list)):
            if key is None:
                comparison = the_list[i] < the_list[min_index]
            else:
                comparison = key(the_list[i]) < key(the_list[min_index])
            
            if comparison:
                min_index = i

        sorted_list.append(the_list[min_index])
        del the_list[min_index]

    return sorted_list

def absolute_value(x):
    return abs(x)

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

sorted_list = selection_sort(my_list.copy(), key=absolute_value)
print(sorted_list)
sorted_list = selection_sort(my_list.copy())
print(sorted_list)