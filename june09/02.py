def find_gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))

gcd = find_gcd(num1, num2)
print("Наибольший общий делитель чисел", num1, ",", num2, "=", gcd)
