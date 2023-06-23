import matplotlib.pyplot as plt
import numpy as np
import json

def make_chart(pokemon_names, types):
    values = []
    stat_types = ("Hp", "Attack", "Defence", "SpAttack", "SpDefence", "Speed", "Average")
    with open("data.json", "r") as json_file:
        loaded_pokemon = json.load(json_file)
        for i in loaded_pokemon:
            set = []
            for j in i:
                set.append(j["base_stat"])
            set.append(int(sum(set) / 6))
            values.append(set)

    print("making pokemon list")

    pokemon_stats = {}
    for i in range(len(pokemon_names)):
        pokemon_stats[pokemon_names[i]] = values[i]
    
    x = np.arange(len(stat_types))  # the label locations
    width = 0.3
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    type_colors = []
    for i in types:
        num = []
        if i == "fire":
            random_int = np.random.randint(140, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 110)
            num.append(random_int)
            random_int = np.random.randint(0, 110)
            num.append(random_int)
        elif i == "grass":
            random_int = np.random.randint(0, 110)
            num.append(random_int)
            random_int = np.random.randint(140, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 110)
            num.append(random_int)
        elif i == "water":
            random_int = np.random.randint(0, 110)
            num.append(random_int)
            random_int = np.random.randint(0, 110)
            num.append(random_int)
            random_int = np.random.randint(140, 255)
            num.append(random_int)
        elif i == "ghost":
            random_int = np.random.randint(140, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 100)
            num.append(random_int)
            random_int = np.random.randint(140, 255)
            num.append(random_int)
        elif i == "ground":
            random_int = np.random.randint(140, 255)
            num.append(random_int)
            random_int = np.random.randint(120, 210)
            num.append(random_int)
            random_int = np.random.randint(0, 90)
            num.append(random_int)
        elif i == "rock":
            random_int = np.random.randint(100, 220)
            num.append(random_int)
            random_int = np.random.randint(70, 140)
            num.append(random_int)
            random_int = np.random.randint(0, 150)
            num.append(random_int)
        elif i == "fighting":
            random_int = np.random.randint(150, 255)
            num.append(random_int)
            random_int = np.random.randint(150, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 50)
            num.append(random_int)
        elif i == "fairy":
            random_int = np.random.randint(180, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 150)
            num.append(random_int)
            random_int = np.random.randint(180, 255)
            num.append(random_int)
        elif i == "poison":
            random_int = np.random.randint(130, 200)
            num.append(random_int)
            random_int = np.random.randint(0, 120)
            num.append(random_int)
            random_int = np.random.randint(130, 200)
            num.append(random_int)
        elif i == "flying":
            random_int = np.random.randint(180, 200)
            num.append(random_int)
            random_int = np.random.randint(180, 200)
            num.append(random_int)
            random_int = np.random.randint(220, 255)
            num.append(random_int)
        elif i == "normal":
            random_int = np.random.randint(150, 200)
            num.append(random_int)
            random_int = np.random.randint(150, 200)
            num.append(random_int)
            random_int = np.random.randint(150, 200)
            num.append(random_int)
        elif i == "steel":
            random_int = np.random.randint(130, 180)
            num.append(random_int)
            num.append(random_int)
            num.append(random_int)
        elif i == "electric":
            random_int = np.random.randint(230, 255)
            num.append(random_int)
            num.append(random_int)
            random_int = np.random.randint(0, 120)
            num.append(random_int)
        elif i == "ice":
            random_int = np.random.randint(0, 130)
            num.append(random_int)
            random_int = np.random.randint(200, 255)
            num.append(random_int)
            num.append(random_int)
        elif i == "dragon":
            random_int = np.random.randint(40, 80)
            num.append(random_int)
            random_int = np.random.randint(0, 40)
            num.append(random_int)
            random_int = np.random.randint(150, 255)
            num.append(random_int)
        elif i == "psychic":
            random_int = np.random.randint(230, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 60)
            num.append(random_int)
            random_int = np.random.randint(150, 200)
            num.append(random_int)
        elif i == "bug":
            random_int = np.random.randint(100, 190)
            num.append(random_int)
            num.append(random_int * 1.3)
            random_int = np.random.randint(0, 70)
            num.append(random_int)
        elif i == "dark":
            random_int = np.random.randint(20, 100)
            num.append(random_int)
            num.append(random_int * 0.7)
            random_int = np.random.randint(0, 10)
            num.append(random_int)
        else:
            random_int = np.random.randint(0, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 255)
            num.append(random_int)
            random_int = np.random.randint(0, 255)
            num.append(random_int)
        type_colors.append(num)

    counter = 0

    for name, values in pokemon_stats.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, values, width, label=name,
                       color=(type_colors[counter][0]/255,
                              type_colors[counter][1]/255,
                              type_colors[counter][2]/255))
        ax.bar_label(rects, padding=3)
        multiplier += 1
        counter += 1

    ax.set_ylabel('Stat Power')
    ax.set_title('Pokemon stats by stat type')
    ax.set_xticks(x + width, stat_types)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 250)

    plt.show()


