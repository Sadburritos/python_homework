num = int(input("Число = "))
last_num = num %10

num = num // 10
 
new_num = last_num * 10000 + num
 
print(new_num)