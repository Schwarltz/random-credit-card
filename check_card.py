import sys
from helpers import sumDigits

if len(sys.argv) != 2:
    print("Usage: python check-card.py <card-num>")
    exit(1)

card = sys.argv[1]

if not card.isdigit():
    print(f"Input was not a convertable into a number")
    exit(1)
elif len(card) != 16:
    print(f"Invalid card! Input: {card}")
    exit(1)

card = [int(x) for x in card]

checkSum = 0
for i, digit in enumerate(card[:-1]):
    mult = 1
    if i % 2 == 0:
        mult = 2
    
    checkSum += sumDigits(mult*digit)

checkDigit = 10 - (checkSum % 10)
print(checkDigit)
if checkDigit == card[-1]:
    print("Valid card")
else:
    print("Invalid card")

    
    



