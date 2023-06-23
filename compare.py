import requests
import json
import make_chart

def compare():
    possible = (2, 3)
    while(True):
        try:
            num = int(input("\nHow many pokemon will you compare?\n2 or 3?: "))
        except:
            print("\nThat isn't a valid response")
        else:
            if num in possible:
                print("\nLet's go!!")
                break
            else:
                print("\nI can't compare that many for you")
    
    poke_list = []
    poke_names = []
    types = []
    for _ in range(num):
        while(True):
            try:
                pokemon = str(input("Name a pokemon: ")).lower()
                response = requests.get(F'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            except:
                print("You may have spelled that name wrong :( Try again")
            else:
                if response.status_code == 200:
                    json_obj = response.json()
                    types.append(json_obj["types"][0]["type"]["name"])
                    poke_list.append(json_obj["stats"])
                    poke_names.append(pokemon)
                    print("That's a great pokemon")
                    break
                elif response.status_code == 404:
                    print("We couldn't find that pokemon. Check your spelling.")

    with open("data.json", "w") as json_file:
        json.dump(poke_list, json_file)

    make_chart.make_chart(poke_names, types)
