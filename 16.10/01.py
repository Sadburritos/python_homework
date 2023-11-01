import time


def measuretime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        print(f"{func.__name__}() - {elapsed_time_ms:.2f} мс")
        return result

    return wrapper


@measuretime
def some_function():
    time.sleep(10)


some_function()
