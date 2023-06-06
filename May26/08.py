
user_in = input("Трехзначное число = ")

try:
    user_num = int(user_in)
except ValueError:
    message = "Ошибка, это не число"
else:
    idk = user_num // 10            #Я не знаю как назвать переменнуюпоэтому IDK
    message = idk % 10
    
print(message)