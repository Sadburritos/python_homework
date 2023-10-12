def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr(((ord(char) - ord('а') + 1) % 26) + ord('а'))
            else:
                new_char = chr(((ord(char) - ord('А') + 1) % 26) + ord('А'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


with open('input2.txt', 'r', encoding='utf-8') as input_file:
    text = input_file.read()

encrypted_text = encrypt(text)

with open('output2.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(encrypted_text)
