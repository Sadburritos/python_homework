import random

def get_random_int(min, max):
    result = random.randint(min, max)
    return result

def game(my_random, min, max, attempts):
    if attempts == 0:
        print("Вы проиграли! А число было: %d" % my_random)
        play_again()
        return

    user_in = input("Угадай число от %s до %s. Осталось %s попыток: " % (min, max, attempts))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Только целое число вводи!")
        game(my_random, min, max, attempts)
    else:
        if my_random > user_num:
            print("Больше ;)")
            game(my_random, min, max, attempts - 1)
        elif my_random < user_num:
            print("Меньше :)")
            game(my_random, min, max, attempts - 1)
        else:
            print("Правильно! Вы угадали за %d попыток." % (7 - attempts + 1))
            play_again()

def play_again():
    user_choice = input("Хотите ещё раз сыграть (да/нет)? ").lower()
    if user_choice in ["да", "д", "yes", "y"]:
        num = get_random_int(0, 20)
        game(num, 0, 20, 7)
    elif user_choice in ["нет", "н", "no", "n"]:
        print("Спасибо за игру! До свидания.")
    else:
        print("Некорректный ответ. Пожалуйста, введите 'да' или 'нет'.")
        play_again()

num = get_random_int(0, 20)
game(num, 0, 20, 7)
