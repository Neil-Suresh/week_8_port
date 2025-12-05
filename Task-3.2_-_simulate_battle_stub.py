# """
# Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

# In this exercise, you will create a Pokemon class and use it to simulate battles.
# This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
# """

import httpx
import json 

class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        """
        Initialise a Pokemon by fetching its data from the API and calculating its stats.

        Args:
            name (str): The name of the Pokemon (e.g., "pikachu")
        """
        self.name = name.lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        rep =httpx.get(url)
        
        if rep.status_code != 200:
            raise ValueError("Pokemon not found")
        
        data = rep.json()
        

           

        # TODO: Store the Pokemon's name (lowercase) - done

        # TODO: Fetch Pokemon data from PokeAPI - done
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data
        stats_list = data["stats"]
        base_hp = stats_list[0]["base_stat"]
        base_attack = stats_list[1]["base_stat"]
        base_defense = stats_list[2]["base_stat"]
        base_speed = stats_list[5]["base_stat"]

        max_hp = self._calculate_hp(base_hp)
        attack = self._calculate_stat(base_attack)
        defense = self._calculate_stat(base_defense)
        speed = self._calculate_stat(base_speed)

        self.stats = {
            "max_hp" : max_hp,
            "attack" : attack, 
            "defense" : defense,
            "speed" : speed
        }
        self.current_hp = max_hp
        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp

        

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated stat
        """

        
        # TODO: Implement the stat calculation formula
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)
        

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 15)
            ev (int): Effort value (default 85)

        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)
        

    def attack(self, defender):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            defender (Pokemon): The Pokemon being attacked

        Returns:
            int: The amount of damage dealt
        """

        level = 50
        base_power = 60
        # TODO: Calculate damage using the damage formula
        damage=  int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        # Where 50 is level and 60 is base_power

        # TODO: Make the defender take damage
        defender.take_damage(damage)

        return damage 

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        # TODO: Reduce current_hp by amount
        # Make sure HP doesn't go below 0
        self.current_hp = max(0, self.current_hp - amount)

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        # TODO: Return True if current_hp <= 0, False otherwise
        return self.current_hp <= 0

    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)"
        return f"{self.name.title()} HP: {self.current_hp}/{self.stats["max_hp"]}"


def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects
    poke1 = Pokemon(pokemon1_name)
    poke2 = Pokemon(pokemon2_name)


    # TODO: Display battle start message
    # Show both Pokemon names and initial HP
    print(f"{pokemon1_name} and {pokemon2_name} have engaged in a battle!!")

    print(poke1)
    print(poke2)
    
    if poke1.stats["speed"] >= poke2.stats["speed"]:
        attacker, defender = poke1 , poke2
    else:
        attacker , defender = poke2 , poke1
    
    rounds = 1

    while True:
        print(f" Round {rounds} --")

        damage = attacker.attack(defender)
        print(f"{attacker.name.title()} strikes {defender.name.title()} for {damage}!")
        print(defender)

        if defender.is_fainted():
            print(f"{defender.name.title()} fainted!")
            print(f"{attacker.name.title()} won the battle!!")
            break
        

        damage = defender.attack(attacker)
        print(f"{defender.name.title()} strikes {attacker.name.title()} for {damage}!")

        print(attacker)

        if attacker.is_fainted():
            print(f"{attacker.name.title()} fainted!")
            print(f"{defender.name.title()} wins the battle!!")
            break

        rounds+= 1
    # TODO: Determine who attacks first based on speed
    # The Pokemon with higher speed goes first
    # Hint: Compare pokemon1.stats['speed'] with pokemon2.stats['speed']



    # TODO: Battle loop
    # - Keep track of round number
    # - While neither Pokemon is fainted:
    #   - Display round number
    #   - Attacker attacks defender
    #   - Display damage and remaining HP
    #   - Check if defender fainted
    #   - If not, swap attacker and defender
    #   - Increment round number

    # TODO: Display battle result
    # Show which Pokemon won and their remaining HP
    pass


if __name__ == "__main__":
    # Test your battle simulator
    simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    simulate_battle("charmander", "squirtle")
    simulate_battle("eevee", "jigglypuff")
