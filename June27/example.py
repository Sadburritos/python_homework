from functools import reduce

def square(x):
    return x ** 2

num = [1, 2, 3, 4, 5]
square_num = list(map(square, num))
print(square_num)  

def is_even(x):
    return x % 2 == 0

num = [1, 2, 3, 4, 5]
even_num = list(filter(is_even, num))
print(even_num)  


def multiply(x, y):
    return x * y

num = [1, 2, 3, 4, 5]
product = reduce(multiply, num)
print(product)  
