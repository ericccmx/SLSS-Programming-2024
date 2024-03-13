# Problem J1: Conveyor Belt Sushi
# Author: Eric Zhang
# Date: Feb 23, 2024

# Record how many red plates (R), green plates (G), and blue plates (B) of sushi are consumed
R = int(input("How many red plates of sushi are consumed?"))
G = int(input("How many green plates of sushi are consumed?"))
B = int(input("How many blue plates of sushi are consumed?"))

# Calculate the total cost
total_cost = int(R)*3 + int(G)*4 + int(B)*5
print(f"The total cost is {total_cost}.")