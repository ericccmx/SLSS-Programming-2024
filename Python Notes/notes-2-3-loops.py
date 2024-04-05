# Loops and Iteration
# Author: Eric Zhang
# Date: Apr 5, 2024

# Print "something" 10 times
for _ in range (10):
    print("something")

# Print out every item in my grocery list
grocery_list = [
    "dishwasher tabs",
    "aluminium foil",
    "blueberry muffins",
    "RTX 4070 Super"
]

# Stop if we reach blueberry muffins
for grocery_item in grocery_list:
    print("---")
    print(f"* {grocery_item}")

    if grocery_item == "blueberry muffins":
        break

# Count from 0 to 9 --> Keep track of the loop
for i in range (10):    # i represents how many times it has iterated
    print(i)
    # Modulo (%): the remainder
    if i % 2 ==0:
        print(f"{i} is an even number")

# Rewrite the above for loop as a while loop
counter = 0

while counter < 10:
    print (counter)

    if counter % 2 == 0:
        print (f"{counter} is an even number.")
    # increment counter by 1: counter = counter + 1
    counter += 1