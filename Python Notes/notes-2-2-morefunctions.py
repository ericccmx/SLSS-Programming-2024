# More functions
# Author: Eric Zhang
# April 3, 2024

# # Multiply strings
# greeting = "hello"
# print(greeting * 5)
# print("The quick brown fox jumps over the lazy dog." *2)

# Implement stars function
def stars(num: int):
    """Returns specified number of *s"""
    value = "" # placeholder for return value

    # If number is 0, return 1 star.
    # If number is 1, return 1 star.
    # elif number is greater than 1, return that number * star.
    # else return error saying negative numbers aren't allowed

    if num == 0 or num ==1:
        value = "*"
    elif num > 1:
        value = "*" * num
    else:
        value = "Sorry, we can't take negative numbers."
    return value

print(stars(0))
print(stars(1))
print(stars(1000))
print(stars(-1))

