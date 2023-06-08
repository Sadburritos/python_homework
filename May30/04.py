word = input("Слово из пяти букв: ")

if len(word) != 5:
    print("Слово не из пяти букв.")
else:
    reversed_word = word[::-1]  

    if word == reversed_word:
        print("Слово палиндромом.")
    else:
        print("Слово не палиндром.")