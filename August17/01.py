def bubble_sort(the_list, key=None):
    n = len(the_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n - 1):
            if key is None:
                comparison = the_list[i] > the_list[i + 1]
            else:
                comparison = key(the_list[i]) > key(the_list[i + 1])
            #VN: ^^^^^^^^^^^^^^^^^^^^^^^ можно вообще оставить только эту строку
            # А в самом начале функции, если key is None, то присвоить key "функцию-пустышку"
            # Подумайте, как это можно сделать ;)
                
            if comparison:
                the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
                is_sorted = False
        n -= 1
    return the_list

user_in = input("Введите числа через запятую: ")
user_in = user_in.split(',')
my_list = list(map(lambda x: int(x), user_in))

def absolute_value(x):
    return abs(x)

sorted_list = bubble_sort(my_list)
print(sorted_list)

#VN: просто добавил для проверки вызова с key-функцией
sorted_list = bubble_sort(my_list, absolute_value)
print(sorted_list)

#VN: Всё отлично работает! Вы сделали очень хороший вариант. Как можно сделать ещё лучше, я отметил выше