# Lists and Modules
# Author: Eric Zhang
# Mar 11, 2024

import random

def coin_flip():
    # Return heads, tails, or other
    # Head is any number 0 to 0.4999
    # Tail is anuy number from 0.5 to 0.9999
    # Other is any number greater than 0.9999

    roll = random.random()
    if roll < 0.5:
        return "heads"
    elif roll < 0.9999:
        return "tails"
    else:
        return "other"

def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0
    other = 0

    # Ran this code for 1 million times
    for _ in range (1_000_000):
    
        # Flip the coin
        result = coin_flip()
        if result == "heads":
            heads = heads +1 # increament
        elif result == "tails":
            tails += 1 # shortcut for increament
        else:
            other += 1
    
    # Print results
    print(f"Number of Heads:{heads}")
    print(f"Number of Tails:{tails}")
    print(f"Number of Other:{other}")

main()