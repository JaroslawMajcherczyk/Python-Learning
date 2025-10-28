
import requests

#https://pokeapi.co/api/v2/

base_url = "https://pokeapi.co/api/v2/"
pokemon_name = ""

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Data retrieve")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
        print()
        pokemon_name = input("Enter pokemon name: ").strip().lower()

is_runing = True

while is_runing:

    print("**** Your POKEMON search engine ****")
    pokemon_name = input("Enter pokemon name: ").strip().lower()
    if pokemon_name == "":
        print("⚠️ You mast write your pokemon name")
        print()
        continue
    if pokemon_name.isdigit():
        print("❌ Pokémon name cannot be numbers! Try again.")
        print()
        continue


    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        types = [t['type']['name'] for t in pokemon_info['types']]
        types_str = ', '.join(types)
        print()
        print(f"Pokemon info: {pokemon_info['id']} {pokemon_info['name'].title()}")
        print(f"Type(s): {types_str}")
        print(f"Height: {pokemon_info['height']} Weight: {pokemon_info['weight']}")
        print()
    if not input("Want to check out another Pokemon? (y/n): ").lower() == "y":
        is_runing = False

print("See You next time!")
print()