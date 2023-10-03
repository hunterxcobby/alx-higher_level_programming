#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# We first convert the number to a string
number_string = str(number)

# Then extract the last digit
last_digit = number_string[-1]

# DOn't forget to first handle the case where the number is negative
if number < 0:
    last_digit = "-" + last_digit

# Print the original number and the alst digit
print(f"Last digit of {number} is {last_digit} and", end=" ")

# Process conditions based on the last digit
if int(last_digit) > 5:
    print(f"is greater than 5")
elif int(last_digit) == 0:
    print(f"is 0")
else:
    print(f"is less than 6 and not 0")
