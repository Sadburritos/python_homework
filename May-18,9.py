a = int(input("Число = "))
b = 0
 
while a > 0:
    c = a % 10
    a = a // 10
 
    b = b * 10
    b = b + c
 
 
print(b)