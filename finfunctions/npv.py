from functools import reduce

def value(sum, F, i, n):
    sum += (F/((1 + i)**n))
    return sum

def npv(initial, rate, *values):
    n = len(values)
    sum = reduce(lambda x, y: value(x, y, rate, n), values)
    return initial * -1 + sum
