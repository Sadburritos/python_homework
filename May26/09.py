user_in = input("Число = ")

try:
    user_num = int(user_in)
except ValueError:
    message = "Ошибка, это не число"
else:
    message = user_num ** 2
    last_num = user_num % 10

    new_num = user_num // 10
 
    message = last_num * 10000 + new_num
    
print(message)