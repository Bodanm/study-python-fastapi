def calculate_average(numbers):
    count = len(numbers)
    sum = 0
    for i in numbers:
        sum += i
    return sum / count


def find_max(numbers):
    numbers.sort(reverse=True)
    max_number = numbers[0]
    return max_number
