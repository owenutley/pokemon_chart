import requests
import json
import sys

count_num = sys.argv[1]
file_name = sys.argv[2]

pokemon_all = {}

count = 905
while True:
    count +=1
    try:
        response = requests.get(F'https://pokeapi.co/api/v2/pokemon/{count}')
    except:
        print("It failed! Haha")
        print(F"Went through {count} pokemon!")
        break
    else:
        if response.status_code == 200:
            json_obj = response.json()
            pokemon_all[json_obj["name"]] = {"type": json_obj["types"][0]["type"]["name"],
                                             "stats": {json_obj["stats"][0]["stat"]["name"]: json_obj["stats"][0]["base_stat"],
                                                       json_obj["stats"][1]["stat"]["name"]: json_obj["stats"][1]["base_stat"],
                                                       json_obj["stats"][2]["stat"]["name"]: json_obj["stats"][2]["base_stat"],
                                                       json_obj["stats"][3]["stat"]["name"]: json_obj["stats"][3]["base_stat"],
                                                       json_obj["stats"][4]["stat"]["name"]: json_obj["stats"][4]["base_stat"],
                                                       json_obj["stats"][5]["stat"]["name"]: json_obj["stats"][5]["base_stat"],
                                                    }}
        else:
            print("couldn't get your pokemon!")
    if count >= int(count_num) + 905:
        break

with open(F"{file_name}", "x") as json_file:
    json.dump(pokemon_all, json_file, indent=4)

