#!/usr/bin/python3
i#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# We first convert the number to a string
number_str = str(number)

# Then extract the last digit
last_digit = number_str[-1]

# Print the original and last number
print("Last digit of", end=" ")
print(f"{number}", end=" ")
print(f"is {last_digit}", end=" ")

# Process conditions based on the last digit
if int(last_digit) > 5:
    print(f"and is greater than 5")
elif int(last_digit) == 0:
    print(f"and is 0")
elif int(last_digit) < 6 and int(last_digit) != 0:
    print(f"and is less than 6 and not 0")
