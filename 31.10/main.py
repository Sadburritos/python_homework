import json


def user_to_json(name, age, position, salary):
    user_data = {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary
    }
    return json.dumps(user_data)


name = "Jonny Lang"
age = 36
position = "musician"
salary = 8500000.0

json_string = user_to_json(name, age, position, salary)
print(json_string)
