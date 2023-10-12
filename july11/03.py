def decrypt(text):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr(((ord(char) - ord('а') - 1) % 26) + ord('а'))
            else:
                new_char = chr(((ord(char) - ord('А') - 1) % 26) + ord('А'))
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

with open('input3.txt', 'r', encoding='utf-8') as input_file:
    encrypted_text = input_file.read()

decrypted_text = decrypt(encrypted_text)

with open('output3.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(decrypted_text)
