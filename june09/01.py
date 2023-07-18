start = int(input("Начало: "))
end = int(input("Конец: "))

sum_of_numbers = 0
num = start

while num <= end:
    sum_of_numbers += num
    num += 1

print("Сумма чисел в диапазоне", start, "до", end, "=", sum_of_numbers)
