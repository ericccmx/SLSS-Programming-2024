# Using random.uniform function
# Author: Eric Zhang
# Date: Mar 11, 2024

# Explain the situation
print("Eric is prepping 10 academic tests, and he has practiced this set of tests by 1,000,000 times. He may have scored randomly from 90% to 100% for each set. If he scored half of the tests below 95%, he will get punished. If he scored half of the tests above 95%, he will get a \"keep trying\". If he got them above 95, he will get a \"good job\" compliment. What are the odds?")

import random

def test_odds():

    ninety_five_number = random.randrange(0,11)

    if ninety_five_number < 5:
        return "punish"
    elif ninety_five_number == 10:
        return "good_job"
    else:
        return "keep_trying"

# Repeat the experiment for 1,000,000 times, and keep track of the numbers.

def main():
    punish = 0
    keep_trying = 0
    good_job = 0
    
    for _ in range (1_000_000):
        result = test_odds()
        if result == "punish":
            punish += 1
        elif result == "keep_trying":
            keep_trying += 1
        else:
            good_job += 1
    
    print(f"You got punished by {punish} times!😈 ")
    print(f"You got a \"Keep trying\" for {keep_trying} times.")
    print(f"You got a \"Good job\" for {good_job} times. BUT keep trying!")    

main()
