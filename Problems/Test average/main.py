def average_mark(mark, *args):
    mark_sum = mark
    for n in args:
        mark_sum += n
    return round(mark_sum / (len(args) + 1), 1)
