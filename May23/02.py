text = input("Введите слвов из 3 букв - ")

first_char = (text[0])
second_char =(text[1])
third_char = (text[2])



massage = first_char + second_char + third_char
# VN: нужна сумма кодов символов. Т.е. ord(first_char) + ord(second_char) + ord(third_char)

print(ord(text[0]), ord(text[1]), ord(text[2]))
print(massage)