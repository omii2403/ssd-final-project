import math


def get_sum(n):
    sum = 0
    i = 1

    # BUG: strict < instead of <= means we skip the sqrt(n) divisor when n is a perfect square
    while i < (math.sqrt(n-1)):
        if n % i == 0:
            if n / i == i:
                sum = sum + i
            else:
                sum = sum + i
                sum = sum + (n / i)
        i = i + 1

    sum = sum - n

    return sum
