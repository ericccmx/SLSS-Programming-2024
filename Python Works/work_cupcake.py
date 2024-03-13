# CCC '22 J1 - Cupcake Party
# Author: Eric Zhang
# Date: Feb 23, 2024

# Ask how many regular (R) and small (S) boxes there are.
R = int(input("How many regular boxes are there?"))
S = int(input("How many small boxes are there?"))

# Calculate the number of cupcakes that are left over.
left_over = R * 8 + S * 3 - 28
more = 28 - R * 8 + S * 3
if left_over >= 0:
    print(f"There are {left_over} cupcakes that are left over.")
else:
    print(f"You need {more} more cupcakes.")
