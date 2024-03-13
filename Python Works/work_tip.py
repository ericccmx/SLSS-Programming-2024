# Tip Calculator
# Author: Eric Zhang
# Date: Feb 28, 2024

# Create a function that converts the meal price to float.
def price_to_float(price):
    return float(price)

# Create a function that converts the tip percentage to float
def tip_percentage_to_float(tip_percentage):
    return float(tip_percentage)/100

# Ask for the price of the meal and the percentage of tip.
# Convert the string to float
def main():
    price = price_to_float(input("How much was the meal?"))
    tip_percentage = tip_percentage_to_float(input("What percentage should I tip?"))
    tip = price * tip_percentage
    # Round the result to 2 decimal places
    print(f"The tip should be {round(tip, 2)} dollars.")

main()