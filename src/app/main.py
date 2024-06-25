import utils
import dynamo
from fastapi import FastAPI, HTTPException, status
from botocore.exceptions import ClientError
from pokemon import Pokemon


app = FastAPI()


@app.get("/pokemons")
def get_all_pokemons():
    try:
        pokemons = dynamo.get_all_pokemons()
        return  { 
                    "count": len(pokemons),
                    "results": pokemons
                }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))

@app.post("/pokemons", status_code=status.HTTP_201_CREATED)
def create_pokemon(pokemon: Pokemon):
    try:
        dynamo.insert_pokemon(pokemon.model_dump())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))

@app.get("/pokemons/{search}", status_code=status.HTTP_200_OK)
def get_pokemon(search: str):
    try:
        result = dynamo.get_pokemon_by_id(int(search))
    except ValueError:
        result = dynamo.get_pokemon_by_name(search)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result

@app.delete("/pokemons/{search}", status_code=status.HTTP_202_ACCEPTED)
def delete_pokemon(search: str):
    try:
        try:
            dynamo.delete_pokemon_by_id(int(search))
        except ValueError:
            dynamo.delete_pokemon_by_name(search)
    except ClientError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)