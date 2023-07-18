import random

def get_random_int(min, max):
    result = random.randint(min, max)
    return result

def game(my_random, min, max, attempts):
    if attempts == 0:
        print("Вы проиграли! А число было: %d" % my_random)
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

num = get_random_int(0, 20)
game(num, 0, 20, 7)