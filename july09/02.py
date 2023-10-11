fruits = ['apple', 'banana', 'cherry', 'apple', 'orange', 'banana', 'apple', 'banana', 'cherry', 'apple', 'orange', 'banana']
passed = {}
duplicates = []
for item in fruits:
    if item in passed:
        duplicates.append(item)
    else:
        passed[item] = True
print(f'Найденные дубликаты: {duplicates}')