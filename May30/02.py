num = input("Введите трехзначное число: ")

if len(num) != 3:
    print("Введено некорректное число ")
else:
    digit1 = num[0]
    digit2 = num[1]
    digit3 = num[2]

    if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
        print("В числе есть одинаковые цифры")
    else:
        print("В числе нет одинаковых цифр")