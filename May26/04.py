
user_in = input("км = ")

try:
    user_num = int(user_in)
except ValueError:
    message = "Ошибка, это не число"
else:
    message = user_num * 0.6213711
    
print('am = ', message)
