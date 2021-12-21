import sys
import random
from helpers import sumDigits

CREDIT_CARD_LENGTH = 16




def luhnAlgo(length):
    
    digits = []
    checkSum = 0
    for i in range(length - 2):
        digit = random.randint(0,9)
        digits.append(digit)
        multiplied = digit
        if i % 2 == 0:
            multiplied *= 2
        checkSum += sumDigits(multiplied)
    
    digits.append(10 - (checkSum % 10))
    return "".join([str(x) for x in digits])

if __name__ == '__main__':
    if len(sys.argv) == 1:
        x = luhnAlgo(CREDIT_CARD_LENGTH)
    elif len(sys.argv) == 2:
        x = luhnAlgo(int(sys.argv[1]))
    print(x)

    
