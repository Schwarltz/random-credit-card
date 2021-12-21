import math

def sumDigits(num):
    if num == 0:
        return 0
    x = num % 10
    return x + sumDigits(math.floor(num / 10))