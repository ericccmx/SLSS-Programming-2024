# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and functions

# Create a class that represents a Pokemon
class Pokemon:  # always name classes with capital
    def __init__(self):
        """Constructor (2 underlines on each side):
            contains all properties of a Pokemon.
            It also contains the default state of the properties.
            """
        self.name = ""  # nothing by default
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "Normal"

def main():
    # Create two Pokemon

    # Create something 'Pikachu' - like
    pokemon_one = Pokemon()     # How you create a new Pokemon

    # Change the values of the properties
    pokemon_one.name = "Pikachu"
    pokemon_one.id = 25
    pokemon_one.type = "Electric"

    # Access the properties inside pokemon_one
    # Print the properties of pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.id)
    print(pokemon_one.type)


    # Create something 'Squirtle' - like
        # - Create a new Pokemon object
        # - Store this in variable pokemon_two
        # - Squirtle's Pokedex id is 4
        # - Squirtle's type is water

    pokemon_two = Pokemon()
    pokemon_two.name = "Squirtle"
    pokemon_two.id = 4
    pokemon_two.type = "Water"

    # To test, print out all of the Squirtle's properties
    print(pokemon_two.name)
    print(pokemon_two.id)
    print(pokemon_two.type)

    # Pass ?

if __name__ == "__main__":
     main()