from fastapi import FastAPI, HTTPException, status, Query, Response
from pokemon import Pokemon
from utils import find_pokemon_index

app = FastAPI()


pokemon_list = [
        { "name": "pikachu", "type": "eletric" },
        { "name": "charmander", "type": "fire" }
    ]


@app.get("/pokemons")
def get_all_pokemons():
    return { "status": "OK", "pokemons": pokemon_list }


@app.post("/pokemons", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon: Pokemon):
    pokemon_list.append(pokemon.dict())
    return { "status": "OK", "pokemons": pokemon_list }

@app.get("/pokemons/{name}")
def get_pokemon_by_name(name: str):
    idx = find_pokemon_index(pokemon_list, name)
    if idx is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pokemon {name} doesnt exist."
        )
    return pokemon_list[idx]