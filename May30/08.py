score = 0

print("Вопрос 1: Какая столица Франции?")
print("a) Париж")
print("b) Лондон")
print("c) Рим")
answer1 = input("Ваш ответ: ")

if answer1 == "a":
    score += 2
    print ("Верно")
else:
    print("Не верно") 
print("Количество набранных баллов:", score)


print("Вопрос 2: Какая столица Англии?")
print("a) Париж")
print("b) Лондон")
print("c) Рим")
answer2 = input("Ваш ответ: ")

if answer2 == "b":
    score += 2
    print ("Верно")
else:  
    print("Не верно") 
print("Количество набранных баллов:", score) 

print("Вопрос 3: Какая столица Италии")
print("a) Париж")
print("b) Лондон")
print("c) Рим")
answer3 = input("Ваш ответ: ")

if answer3 == "c":
    score += 2
    print ("Верно")
else:  
    print("Не верно") 
print("Количество набранных баллов:", score)

print ("Конец игры")

