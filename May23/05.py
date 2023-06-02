word = input("Что цензурить?")

first_letter = word[0]
lastest_letter = word [-1]
word_len = len(word) - 2

censor = "*" * word_len 

print(first_letter, censor, lastest_letter)

