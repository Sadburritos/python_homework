user_in = input("Что в квадрат?  ")

try:
    user_num = int(user_in)
except ValueError:
    message = "Ошибка, это не число"
else:
    message = user_num ** 2
    
print(message)