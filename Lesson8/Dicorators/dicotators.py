import time


def time_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start_time:.6f} seconds")
        return result
    return wrapper

@time_dec
def find_even_numbers():
    even_numbers = [num for num in range(1, 10001) if num % 2 == 0]
    return even_numbers

result = find_even_numbers()
print("Even numbers:", result)
