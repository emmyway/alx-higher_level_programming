#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_number = number
if abs_number < 0:
    abs_number *= -1

# to get last digit
last_digit = abs_number % 10

# to include negative sign
if number < 0 and last_digit != 0:
    last_digit *= -1

# print outcome
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less "
          f"than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
