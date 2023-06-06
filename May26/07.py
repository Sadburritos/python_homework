user_in1 = input("Час - ")
user_in2 = input("Минута - ")
try:
    user_num1 = int(user_in1) 
    user_num2 = int(user_in2)
except ValueError:
    print("Ошибка, это не число")

else:
    print(23 - user_num1)
    print (60 - user_num2)


