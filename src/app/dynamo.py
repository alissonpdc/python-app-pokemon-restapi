import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

from pokemon import Pokemon


dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('Pokemon')

def insert_pokemon(pokemon: Pokemon) -> None:
    try:
        table.put_item(Item=pokemon)
        print(f"Pokémon {pokemon['name']} inserted successfully.")
    except ClientError as e:
        raise Exception(f"Failed to insert Pokémon: {e.response['Error']['Message']}")

def get_all_pokemons():
    try:
        response = table.scan()
        return response.get('Items', [])
    except ClientError as e:
        raise Exception(f"Failed to retrieve all Pokémon: {e.response['Error']['Message']}")

def get_pokemon_by_id(pokemon_id: int):
    try:
        response = table.get_item(Key={'id': pokemon_id})
        return response.get('Item', None)
    except ClientError as e:
        raise Exception(f"Failed to get Pokémon by ID: {e.response['Error']['Message']}")

def get_pokemon_by_name(pokemon_name: str):
    try:
        response = table.query(
            IndexName='NameIndex',
            KeyConditionExpression=Key('name').eq(pokemon_name)
        )
        return response.get('Items', [])
    except ClientError as e:
        raise Exception(f"Failed to get Pokémon by name: {e.response['Error']['Message']}")

def delete_pokemon_by_id(pokemon_id: int) -> None:
    try:
        table.delete_item(Key={'id': pokemon_id})
        print(f"Pokémon with ID {pokemon_id} deleted successfully.")
    except ClientError as e:
        raise Exception(f"Failed to delete Pokémon by ID: {e.response['Error']['Message']}")

def delete_pokemon_by_name(pokemon_name: str) -> None:
    try:
        response = table.query(
            IndexName='NameIndex',
            KeyConditionExpression=Key('name').eq(pokemon_name)
        )
        items = response.get('Items', [])
        for item in items:
            table.delete_item(Key={'id': item['id']})
            print(f"Pokémon {pokemon_name} with ID {item['id']} deleted successfully.")
    except ClientError as e:
        raise Exception(f"Failed to delete Pokémon by name: {e.response['Error']['Message']}")

# Example usage
if __name__ == "__main__":
    # Insert a Pokémon
    new_pokemon = {
        "id": 151,
        "name": "mew",
        "type": "psychic",
        "evolution_level": 0,
        "next_evolution_id": None,
        "previous_evolution_id": None
    }
    insert_pokemon(new_pokemon)

    # Get all Pokémon
    print("All Pokémon:")
    all_pokemons = get_all_pokemons()
    for pokemon in all_pokemons:
        print(pokemon)

    # Get Pokémon by ID
    print("Pokémon with ID 151:")
    print(get_pokemon_by_id(151))

    # Get Pokémon by name
    print("Pokémon with name 'mew':")
    print(get_pokemon_by_name('mew'))

    # Delete Pokémon by ID
    delete_pokemon_by_id(151)

    # Delete Pokémon by name
    delete_pokemon_by_name('mew')
