from pokemon import Pokemon

def find_pokemon_by_id(pokemon_list: list[Pokemon], id: int ) -> tuple[int, Pokemon]:
    for index,pokemon in enumerate(pokemon_list):
        if pokemon['id'] == id:
            return index,pokemon
    return None,None


def find_pokemon_by_name(pokemon_list: list[Pokemon], name: str) -> tuple[int, Pokemon]:
    for index,pokemon in enumerate(pokemon_list):
        if pokemon['name'].lower() == name.lower():
            return index,pokemon
    return None,None
        

def find_pokemon(pokemon_list: list[Pokemon], search: str) -> tuple[int, Pokemon]:
    try:
        return find_pokemon_by_id(pokemon_list, id=int(search))
    except ValueError:
        return find_pokemon_by_name(pokemon_list, name=search)


def delete_pokemon(pokemon_list: list[Pokemon], search: str) -> int:
    index,_ = find_pokemon(pokemon_list, search)
    if index is not None:
        pokemon_list.pop(index)
        return index