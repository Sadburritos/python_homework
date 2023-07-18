positive_count = 0
negative_count = 0
zero_count = 0
even_count = 0
odd_count = 0

counter = 0
while counter < 10:
    num = int(input("Введите число: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    counter += 1

print("Статистика:")
print("Положительных чисел:", positive_count)
print("Отрицательных чисел:", negative_count)
print("Нулей:", zero_count)
print("Четных чисел:", even_count)
print("Нечетных чисел:", odd_count)
