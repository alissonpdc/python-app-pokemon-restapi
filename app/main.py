import utils

from fastapi import FastAPI, HTTPException, status
from pokemon import Pokemon


app = FastAPI()


pokemon_list = [
    { "id": 1, "name": "Bulbasaur", "type": "grass", "evolution_level": 0, "next_evolution_id": 2, "previous_evolution_id": None },
    { "id": 2, "name": "Ivysaur", "type": "grass", "evolution_level": 1, "next_evolution_id": 3, "previous_evolution_id": 1 },
    { "id": 3, "name": "Venusaur", "type": "grass", "evolution_level": 2, "next_evolution_id": None, "previous_evolution_id": 2 },
    { "id": 4, "name": "Charmander", "type": "fire", "evolution_level": 0, "next_evolution_id": 5, "previous_evolution_id": None }
]


@app.get("/pokemons")
def get_all_pokemons():
    return  { 
                "count": len(pokemon_list),
                "results": pokemon_list
            }


@app.post("/pokemons", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon: Pokemon):
    pokemon_list.append(pokemon.model_dump())
    return {}

@app.get("/pokemons/{search}", status_code=status.HTTP_200_OK)
def get_pokemon(search: str):
    _,result = utils.find_pokemon(pokemon_list, search)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result

@app.delete("/pokemons/{search}", status_code=status.HTTP_202_ACCEPTED)
def delete_pokemon(search: str):
    result = utils.delete_pokemon(pokemon_list, search)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {}