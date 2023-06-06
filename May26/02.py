user_in1 = input("Число 1   ")
user_in2 = input("Число 2   ")
try:
    user_num1 = int(user_in1)
    user_num2 = int(user_in2)
except ValueError:
    message = "Ошибка, это не число"
else:
    message = (user_num1  + user_num2) / 2  

print(message)
