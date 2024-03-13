# Chatbox
# Author: Eric Zhang
# Date: Mar 11, 2024

import random

# 1. Greet the user.
print("Hello there")

# 2. Ask the user how they are.
print("How are you doing today?")
user_feeling = input().strip(" .,?!").lower()

# 3. Resonds randomly, choicen from the list
good_response = ["I'm glad to hear that!", "Sounds dope!", "Nice bro!"]
bad_response = ["Stop mourning bro!", "Okay I don't need to know that", "Okay, so what?"]
neutral_response = ["Meh.", "Okay whatever.", "Sure bro."]

if user_feeling == "good" or user_feeling == "great":
    print(random.choice(good_response))
elif user_feeling == "bad" or user_feeling == "not good" or user_feeling == "not too good":
    print(random.choice(bad_response))
else:
    print(random.choice(neutral_response))


    
# Say goodbye
print("Alright good luck men. Later!")



# if user_feeling in ["good", "great"]:
#     print(random.choice(good_response))
# elif user_feeling in ["bad", "not good", "not too good"]:
#     print(random.choice(bad_response))
# else:
#     print(random.choice(neutral_response))