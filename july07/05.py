employee_names = ["Анна", "Иван", "Марина", "Анна", "Петр", "Иван"]
duplicates = []

for name in employee_names:
    if employee_names.count(name) > 1 and name not in duplicates:
        duplicates.append(name)

if duplicates:
    print("Сотрудники с дубликатами:", duplicates)
else:
    print("Дубликатов нет.")
