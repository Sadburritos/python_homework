def print_multiplication_table(number, multiplier=1):
    if multiplier > 10:
        return
    
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
    
    print_multiplication_table(number, multiplier + 1)

def print_all_tables(number=2):
    if number > 9:
        return
    
    print(f"Таблица умножения для числа {number}:")
    print_multiplication_table(number)
    print()
    
    print_all_tables(number + 1)

print_all_tables()