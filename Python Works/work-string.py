# String Practice
# Eric Zhang
# Date: 9 February, 2024

# 1. Greet the user
print("Whatup, user.")
print("I'm gonna put ya in a test")
      
# Put an empty space
print()

# 2. Ask them a question
print("You gud?")
input()

# 3. Respond specifically to that question
print("Alright, sounds dope.")
print()

# 4. Ask for the user's name
#   - store the user's response
#   - use the person's name in a repy
print("So, what's your name again? ")
user_name = input()

# 5. Ask for the user's educational attainment.
#   - praise the user if they go to SLSS 
#   - mock at the user if they go somewhere else
print(f"Okay {user_name}, so where do you go to school?")
school_name = input()
if school_name in ["SLSS", "slss", "Steveston-London Secondary School"]:
    print("W choice! Don't miss Mr. Ubial's programming class!")
else:
   print(f"What, are you kidding me? {school_name}? Why ain't you go to SLSS?")
   input()
   print("I don't think that rationale is acceptable anyways.")
print()

# 6. Ask who does the user vote for the new US president.
# If it's Trump, praise the user.
# Else, mock the user.

print(f"You're a Trump guy right, {user_name}?. Come on, it's a yes or no question")
president_choice = input()
if president_choice in ["yes", "YES"]:
    print(f"Wow {user_name}, you're GOAT no cap!")
else:
    print("Okay I don't need to know this.")
print()

# 7. Ask the user about the trolly problem
print("Here, let me ask you this: A trolley is on course to collide with 5 dudes down the track, but you can divert the vehicle to kill just one dude on a different track. Will you divert the vehicle? Just tell me what you think. Yes or no?")
trolly_choice = input()
if trolly_choice in ["Yes", "yes"]:
    print("Yo how about that one innocent dude?")
else:
    print("Woh Woh. So you're gonna let 5 dudes die? That might've been 5 families!")
print()

# 8. Say goodbye
# If the user has answered the first 2 questions correctly, treat them nicely.
# Else, put the user into coma.

if school_name in ["SLSS", "slss", "Steveston-London Secondary School"] and president_choice in ["yes", "YES"]:
    print(f"Alright {user_name}, you've done a fairly good job. Go save the world tomorrow!")
else:
    print(f"Fine, I guess I'm gonna put you into coma, {user_name}, as you're not cool enough!")