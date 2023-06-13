def compare_numbers(num1, num2):
    if num1 < num2:
        return -1
    elif num1 > num2:
        return 1
    else:
        return 0

result = compare_numbers(5, 10)
print(result) 