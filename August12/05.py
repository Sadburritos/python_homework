def calculate_volume(diameter, height):
    radius = diameter / 2
    volume = 3.14 * radius * radius * height * 1000
    return volume

result = calculate_volume(2, 5)
print(result)