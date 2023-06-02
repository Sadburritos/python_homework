word = input("Что половинить?")
word_len = len(word)
word_half = word_len // 2 

word_start = word[:word_half]
word_end = word[word_half:]

print(word_start, " ", word_end)