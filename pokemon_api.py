
import requests

#https://pokeapi.co/api/v2/

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Data retrieve")
        pokemon_data = response.json()
        return pokemon_data
    else:
        # print(f"Failed to retrieve data {response.status_code}")
        print("Something went wrong/can't get that pokemon ")
        print()

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
    else:
        pokemon_info = get_pokemon_info(pokemon_name)

        if pokemon_info:
            types = [t['type']['name'] for t in pokemon_info['types']]
            types_str = ', '.join(types)
            print()
            print("------ Pokemon info ------")
            print()
            print(f"no.{pokemon_info['id']} Name: {pokemon_info['name'].title()}")
            print(f"Type(s): {types_str}")
            print(f"Height: {pokemon_info['height']} Weight: {pokemon_info['weight']}")
            print()
            print("--------------------------")
            print()

    choice = input("Want to check out another Pokemon? \nPress Enter to 'Yes' or write 'N' to close : ").strip().lower() == "n"
    if choice == "n":
        is_running = False
        print("\n👋 Exiting the POKEMON search engine. Goodbye, Kierowniku!\n")
    else:
        print()

print("See You next time!")
print()