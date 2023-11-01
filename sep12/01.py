import threading
import os


def replace_words_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = content.replace('old_word', 'new_word')

    modified_filename = "modified_" + filename
    with open(modified_filename, 'w') as modified_file:
        modified_file.write(content)


files = ['file1.txt', 'file2.txt', 'file3.txt']


threads = []

for file in files:
    thread = threading.Thread(target=replace_words_in_file, args=(file,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("Файлы успешно обработаны и сохранены с префиксом 'modified'.")
