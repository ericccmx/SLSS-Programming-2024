# Title: Asian Parents' Expectation for the Career of Their Kids
# Author: Eric Zhang
# Date: Apr 8, 2024

# Create a function that gives the kid 1 star per 100% they get
def number_of_100(num: int):
    # Ask the kid how many 100% they got this week.
    value = ""
    
    if num >= 5:
        value = f"Not toooo bad. Bare minimum tho. You can have these: {'*' * num}"
    elif num > 0 and num < 5:
        value = f"Only {num} times of 100%? You gotta be kidding me! No dinner for you tonight!"
    else:
        value = "You know what to do. Go find new parents, son."
    return value



user_one_hundreds = int(input("How many 100% did you get this week? "))
print(number_of_100(user_one_hundreds))

# Keep asking until the kid got at leat 5 100%
while user_one_hundreds < 5:
    user_one_hundreds = int(input("How many 100% did you get this week? "))
    print(number_of_100(user_one_hundreds))
    
