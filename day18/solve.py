import math


def sum_divisor(n):
    if n <= 1:
        return 0
    sum_div = 1
    limit = int(math.sqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            if i * i == n:
                sum_div += i
            else:
                sum_div += i + (n // i)

    return sum_div


def buddy(start, limit):
    for i in range(start, limit + 1):
        temp = sum_divisor(i) - 1
        if temp > i and temp > 0:
            if sum_divisor(temp) - 1 == i:
                return [i, temp]
    return "Nothing"
