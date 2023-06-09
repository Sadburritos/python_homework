

user_in1 = input("Число 1   ")
user_in2 = input("Число 2   ")
try:
    user_num1 = int(user_in1)
    user_num2 = int(user_in2)
except ValueError:
    message = "Ошибка, это не число"
    print(message)

else:  
    print("a * b = ", user_num1 * user_num2)
    print("a - b = ", user_num1 - user_num2)
    print("a + b = ", user_num1 + user_num2)
# VN: а поделить? :) С перехватом ZeroDivisionError, конечно же