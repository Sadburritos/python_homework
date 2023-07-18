number = input("Введите число: ")
shift = int(input("На сколько позиций сдвинуть число: "))

shift = shift % len(number)

shift_num = number
while shift > 0:
    shift_num = shift_num[1:] + shift_num [0]
    shift -= 1

print("Результат сдвига:", shift_num )
