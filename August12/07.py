def time_to_seconds(hours, min, sec):
    total_seconds = hours * 3600 + min * 60 + sec
    return total_seconds

result = time_to_seconds(2, 30, 45)
print(result)  