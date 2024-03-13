# Text/Emoji Replacer
# Author: Eric Zhang
# Feb 26, 2024

# Create a function that solves semantic errors
def clean_input(prompt):
    return input(prompt).strip(" sS,.!?").lower()

# Create a function called "translate" takes a string.
# Replace any noodles with 🍜
# Replaces any 100 s with 💯
def translate(user_input):
#    user_input = user_input.replace("noodle", "🍜")
#    user_input = user_input.replace("100", "💯")
   return user_input.replace("noodle", "🍜").replace("100", "💯")

# Mr. Ubial: return user_input.raplace ("100, "💯")
user_input = translate(clean_input("What do you like in terms of 100 and noodles?"))
print(user_input)

