
import random



if __name__ == '__main__':
    start_dict = {
        "Sergey" : "je Sergey m'appelle Platonov",
        "Anthony" : "je m'appelle Anthony Claude",
        "Juan" : "je m'appelle Juan Pecan",
        "Taonga" : "je m'appelle Taonga Banda",
    }

    print(random.choice(list(start_dict.keys())))

    anthony_torture = [len(name) for name in start_dict.keys()] # MEME EFFET ! OPTIMALE QUALITE

    name_lengths = list(map(lambda x : len(x),start_dict.keys())) # MEME CHOSE !
    name_lengths = list(map(len, start_dict.keys())) # MEME CHOSE ! OPTIMALE PERF
    name_lengths = [length for length in map(lambda x:len(x),start_dict.keys())] # MEME CHOSE !
    print(anthony_torture)
    #verifier la premier lettre du dictionnaire start_dict si p go dans une liste
    juan_torture = [key for key, valeur in start_dict.items() if valeur.split(sep=" ")[-1][0] == "P"]
    names_with_lastnames_m = list(filter(lambda k : start_dict[k].split()[-1][0] == "P" , start_dict.keys()))
    print(juan_torture)

    # start_dict -> list[list["Sergey", "Sergey", "Platonov"]] -> dict["S" : "SP"]
    #pacourir le dic
    #pour chac element->clé , la valeur
    #clé premier lettre 
    #valeur dont appartient el contient premiere lettre

    lst=[
        [key]+[
            word
            for word
            in value.split()
            if word==key
        ] + [value.split()[-1]]
        for key, value 
        in start_dict.items()
    ]

    value_split = lambda key, value : [key] + [word for word in value.split() if word==key] + [value.split()[-1]]
    lst=[
        value_split(key, value)
        for key, value 
        in start_dict.items()
    ]
    lst=[[key]+[word for word in value.split() if word==key] + [value.split()[-1]] for key, value in start_dict.items()]
    # [['Sergey', 'Sergey', 'Platonov'], ['Anthony', 'Anthony', 'Claude'], ['Juan', 'Juan', 'Pecan'], ['Taonga', 'Taonga', 'Banda']]
    # start_dict -> list[list["Sergey", "Sergey", "Platonov"]] -> dict["S" : "SP"]
    dct = {item[0][0] : "".join([word[0] for word in item[1:]]) for item in lst}
    print(dct)

    # ****************
    first_way = [0 for _ in range(10)] # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] best way
    second_way = [0] * 10           # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_way[0] = 1 # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    second_way[0] = 1 # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(first_way)
    # print(second_way)
    # ****************

