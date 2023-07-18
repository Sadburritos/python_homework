num = int(input("Число: "))
count = 0

while num >= 50:
    num /= 2
    count += 1

print("Полученное число:", num)
print("Количество делений:", count)
