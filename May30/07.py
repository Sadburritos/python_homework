circle_len = float(input("Введите длину окружности: "))
square_per = float(input("Введите периметр квадрата: "))

radius = circle_len / (2 * 3.14)

square_side = square_per / 4

if square_side >= 2 * radius:
    print("Окружность поместиться в указанный квадрат")
else:
    print("Окружность не поместиться в указанный квадрат")