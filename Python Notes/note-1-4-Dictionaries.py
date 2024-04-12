# Dictionaries
# Author: Eric Zhang
# Date: Apr 12, 2024

# Big Ideas:
#   - dictionaries are a data structure
#   - dictionaries map keys to values

# Flashback to lists
person = {
    "name": "John",
    "age": "23 years old",
    "credit card number": "4500 1023 2222 1111",
    "SIN number": "111 222 333",
}

# # Get and print the person's name
# print(person[0])
# print(person[1])    # age?
# print(person[2])    # some numbers?

# # Print the last thing in the list
# print(person[-1])
# print(person[-2])   # second to last

# print(person[10])   # break (out of range)

# Iterate over the person list
#   print each value
for item in person:
    print(item)


# Use a dictionary instead of a list
person_dictionary = {
    "name": "John",
    "age" : "23 years old",
    "credit card number": "4500 1023 2222 1111"
}

# Get and print the person's info by using its corresponding key
print(person_dictionary["name"])
print(person_dictionary["age"])
print(person_dictionary["credit card number"])

for key in person_dictionary:
    print(key, person_dictionary[key], sep=": ")

for key, value in person_dictionary.items():
    print(key)
    print(value)