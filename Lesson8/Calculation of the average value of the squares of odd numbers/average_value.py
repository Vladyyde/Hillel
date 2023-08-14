from functools import reduce


def average_value(numbers):
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    squared_odd_numbers = map(lambda x: x ** 2, odd_numbers)

    sum = reduce(lambda x, y: x + y, squared_odd_numbers)
    count = len(list(squared_odd_numbers))

    average = sum / count if count > 0 else 0
    return average


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = average_value(numbers)
print(f"average_value {value}")
