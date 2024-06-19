def find_pokemon_index(pokemon_list, name: str):
    for index,pokemon in enumerate(pokemon_list):
        if pokemon['name'] == name:
            return index