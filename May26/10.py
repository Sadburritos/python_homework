salary = 250
user_int = input("Процент от продаж = ")

try:
    per_of_sales = int(user_int)
except ValueError:
    message = "Ошибка, это не число"
else:
    total_salary = per_of_sales // 10

    message = total_salary + salary
    
print(message)
