# Methods - string method
# Author: Eric Zhang
# Date: Feb 21, 2024

# Ask the user what the weather is like
user_reply = input("What is the weather like?")

#If they answer rainy, say bring an umbrella
if user_reply.strip(" !?.").lower() == "rainy":
    print("Bring an umbrella!")
else:
    print("Sorry, I didn't understant what you said.")