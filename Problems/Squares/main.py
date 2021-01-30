def sq_sum(*numbers):
    num_sum = 0
    for number in numbers:
        num_sum += number ** 2
    return float(num_sum)
