def seconds_to_time(sec):
    hours = sec // 3600
    min = (sec % 3600) // 60
    sec = (sec % 3600) % 60
    time_string = "{:02d}:{:02d}:{:02d}".format(hours, min, sec)
    return time_string

result = seconds_to_time(10000)
print(result)