def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum == num:
        return True
    else:
        return False

result = is_perfect_number(6)
print(result) 