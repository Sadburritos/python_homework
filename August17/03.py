user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def quick_sort(the_list, key=None):
    if len(the_list) <= 1:
        return the_list
    if key is None:
        pivot = the_list[0]
    else:
        pivot = key(the_list[0])

    less = list(filter(lambda x: (key(x) if key else x) < pivot, the_list))
    equals = list(filter(lambda x: (key(x) if key else x) == pivot, the_list))
    more = list(filter(lambda x: (key(x) if key else x) > pivot, the_list))
    
    result = quick_sort(less, key) + equals + quick_sort(more, key)
    return result

def absolute_value(x):
    return abs(x)

print(quick_sort(my_list, key=absolute_value))
print(quick_sort(my_list))