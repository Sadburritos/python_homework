user_in = input("Длина квадрата = ")

try:
    user_num = int(user_in)
except ValueError:
    message = "Ошибка, это не число"
else:
    message = user_num * user_num
    
print(message)
