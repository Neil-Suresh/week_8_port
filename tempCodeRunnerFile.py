
        name = "Pikachu"
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        rep =httpx.get(url)
        data = rep.json()
        print(data)

    

        # TODO: Store the Pokemon's name (lowercase) - done

        # TODO: Fetch Pokemon data from PokeAPI - done
        # - Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # - Make GET request
        # - Check response status code (raise error if not 200)
        # - Store the JSON data

        # TODO: Calculate and store stats
        # - Use _calculate_stat() for attack, defense, speed
        # - Use _calculate_hp() for max HP
        # - Store stats in a dictionary
        # - Set current_hp = max_hp

        