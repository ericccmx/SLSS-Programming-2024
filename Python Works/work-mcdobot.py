# Ask the user's name
user_name = input("Hi, what's your name?")

#Capitalize the first letter of the user's name
user_name = user_name.title()

# Ask if the user wants fries with their meal
meal_choice = input (f"Hi, {user_name}! Would you like fries to come with your meal?")

# Cut off any unnecessary components from the user's input
meal_choice = meal_choice.strip(" ?.!").lower() 

# Reply the user correspondingly.
if meal_choice == "yes" or meal_choice == "sure":
    print(f"Alright, {user_name}. Here is your meal with fries.")
elif meal_choice == "no":
    print(f"No problem, {user_name}. I won't put fries in your meal.")
else:
    print(f"Sorry, {user_name}. I didn't understant what you said.")

# Say goodbye to the user.
print(f"Here's your meal, {user_name}. Have a good day!")
