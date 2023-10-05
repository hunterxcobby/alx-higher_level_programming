#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
# Calculate the result using the imported function
result = add(a, b)

# Print the result using string formatting
print("{:d} + {:d} = {:d}".format(a, b, result))
