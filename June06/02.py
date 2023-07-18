def print_next_day(current_day=0):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    
    print("День недели -", days_of_week[current_day])
    answer = input("Хотите увидеть следующий день? (да/нет): ")
    
    if answer.lower() == "нет":
        return
    
    next_day = (current_day + 1) % 7
    print_next_day(next_day)

print_next_day()