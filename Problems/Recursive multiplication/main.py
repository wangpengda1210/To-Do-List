def multiply(a, b):

    if b <= 0:
        return 0

    if b == 1:  # base case
        return a
    # recursive case
    return a + multiply(a, b - 1)
