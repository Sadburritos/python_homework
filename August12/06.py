def format_time(hour, min = 0, sec = 0):
    time = "{:02d}:{:02d}:{:02d}".format(hour, min, sec)
    return time

result1 = format_time(10)
result2 = format_time(6, 30, 45)
print(result1)  
print(result2)  