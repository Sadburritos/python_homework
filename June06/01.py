def print_smileys(n):
    if n == 0:
        return
    print(":)") 

    print_smileys(n - 1)

n = 5
print_smileys(n)