import csv


def lire_csv(fichier):
    data = []
    with open(fichier, 'r') as f:
        lecteur = csv.reader(f)
        next(lecteur) 
        for ligne in lecteur:
            data.append(ligne)
    #print(data)
    return data

#lire_csv("dataset2_Python+P7.csv")

def clean_data(fichier):
    data = lire_csv(fichier)
    data_cleaned = []
    for ligne in data :
        if len(ligne) != 3:
            continue
        nom_action = ligne[0]
        try:
            prix = float(ligne[1])
            profit = float(ligne[2])
        except ValueError:
            continue
        if prix < 0 or profit <=0:
            continue
        action = {"name":nom_action, "price":prix, "profit": profit}
        data_cleaned.append(action)
    #print(data_cleaned)
    print(len(data_cleaned))
    return data_cleaned

#clean_data("dataset1_Python+P7.csv")
