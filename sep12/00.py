import threading

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calculate_average(sublist):
    avg = sum(sublist) / len(sublist)
    return avg


num_threads = 4
chunk_size = len(numbers) // num_threads
sublists = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

threads = []
results = []

for sublist in sublists:
    thread = threading.Thread(target=lambda s=sublist: results.append(calculate_average(s)))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

final_average = sum(results) / len(results)

print("Среднее значение списка:", final_average)
