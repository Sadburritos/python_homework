def calculate_area(length, width = 0):
    if width == 0:
        area = length ** 2
    else:
        area = length * width
    return area

result1 = calculate_area(5)
result2 = calculate_area(4, 6)
print(result1)  
print(result2)  