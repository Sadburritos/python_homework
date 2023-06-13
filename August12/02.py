def sum_of_numbers(num):
    total_sum = 0
    for i in range(num + 1):
        total_sum += i
    return total_sum

result = sum_of_numbers(10)
print(result) 