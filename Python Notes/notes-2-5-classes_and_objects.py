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

        self.actual_cry = "Rooooooar"

    # Method is a function inside of a class
    def cry(self) -> str:
        """Represents the sound a Pokemon makes
        
        Returns:
            - As a string the sound a pokemon makes
            - e.g. "{name} says, "{actual_cry}"""
        return f"{self.name} cries, \"{self.actual_cry}!\""
    
    def consume(self, item: str) -> str:
        """Pokemon consumes the item
        
        Params:
            - the item the pokemon consumes
        
        Returns:
            - the response of the pokemon"""
        
        if item.lower() == "berry":
            return f"{self.name} eats the berry and says, \"YUM!\""
        elif item.lower() == "potion":
            return f"{self.name} feels much better after the potion!"
        else:
            return f"{self.name} batted away the {item}!"
        
class Pikachu(Pokemon):
    """a child class of Pokemon"""

    def __init__(self, name = "Pikachu"):    # "Pikachu" is the name by default
        # Call the super-class constructor
        super().__init__()

        # Setting the default values for a Pikachu
        self.name = name    # name here is the name in the ()
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikachu"

    def thunder(self, defender: Pokemon) -> str:
        """Represents the thunder attack.
         Params:
            - defender: defending pokemon"""

        response = f"{self.name} used Thunder."

        if defender.type.lower() == "water":
            response = response + " It was super effective!"

        return response


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

    # To test Pokemon cry
    print(pokemon_one.cry())
    print(pokemon_two.cry())

    # To test Pokemon consume
    print(pokemon_one.consume("berry"))
    print(pokemon_two.consume("potion"))
    print(pokemon_one.consume("poison"))

    # Create a new Pikachu object
    pikachu_one = Pikachu()
    # Print name, ID, and type of pikachu_one
    print(pikachu_one.name, pikachu_one.id, pikachu_one.type)

    # Use the Pokemon (parent class) methods on Pikachu object (child class)
    print(pikachu_one.cry())

    # Use the thunder method on pokemon_one and pokemon_two (water type)
    print(pikachu_one.thunder(pokemon_one))
    print(pikachu_one.thunder(pokemon_two))

    # pokemon_one.thunder()   # It will break as thunder() is exclusive to pikachu

    # Pass ?

if __name__ == "__main__":
     main()