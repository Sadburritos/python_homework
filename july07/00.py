input_data = input("Введите 10 чисел через пробел: ")
input_list = input_data.split()[:10]
number_list = [int(num) for num in input_list]
even_numbers = [num for num in number_list if num % 2 == 0]
print("Исходный список:", number_list)
print("Список четных чисел:", even_numbers)
