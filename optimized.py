actions = [
    {"produit":"action 1", "prix":20, "pourcent":5},
    {"produit":"action 2", "prix":30, "pourcent":10},
    {"produit":"action 3", "prix":50, "pourcent":15},
    {"produit":"action 4", "prix":70, "pourcent":20},
    {"produit":"action 5", "prix":60, "pourcent":17},
    {"produit":"action 6", "prix":80, "pourcent":25},
    {"produit":"action 7", "prix":22, "pourcent":7},
    {"produit":"action 8", "prix":26, "pourcent":11},
    {"produit":"action 9", "prix":48, "pourcent":13},
    {"produit":"action 10", "prix":34, "pourcent":27},
    {"produit":"action 11", "prix":42, "pourcent":17},
    {"produit":"action 12", "prix":110, "pourcent":9},
    {"produit":"action 13", "prix":38, "pourcent":23},
    {"produit":"action 14", "prix":14, "pourcent":1},
    {"produit":"action 15", "prix":18, "pourcent":3},
    {"produit":"action 16", "prix":8, "pourcent":8},
    {"produit":"action 17", "prix":4, "pourcent":12},
    {"produit":"action 18", "prix":10, "pourcent":14},
    {"produit":"action 19", "prix":24, "pourcent":21},
    {"produit":"action 20", "prix":114, "pourcent":18}
    ]


def calculer_benefice(actions):
    # Calcul du bénéfice réel pour chaque action
    actions_benefices_reels = []
    for action in actions:
        produit = action["produit"]
        prix = action["prix"]
        pourcent = action["pourcent"]
        benefice_reel = (prix * pourcent)/100
        actions_benefices_reels.append({"produit":produit,"prix":prix,"benefice_reel":benefice_reel})
    return actions_benefices_reels

def sacADos_dynamique(portefeuille, actions_benefices_reels):
    #_ : variable jetable
    # Création de la matrice à deux dimensions
    matrice = [[0 for _ in range(portefeuille + 1)] for _ in range(len(actions_benefices_reels) + 1)]

    #remplissage de la matrice (du tableau)
    for i in range(1, len(actions_benefices_reels) + 1):
        prix = actions_benefices_reels[i-1]["prix"] 
        benefice_reel = actions_benefices_reels[i-1]["benefice_reel"]
        for w in range(1, portefeuille + 1):
            if prix <= w:
                matrice[i][w] = max(benefice_reel + matrice[i-1][w-prix], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = portefeuille
    n = len(actions_benefices_reels)
    elements_selection = []

    while w >= 0 and n >= 0:
        if matrice[n][w] != matrice[n-1][w]:
            elements_selection.append(actions_benefices_reels[n-1])
            w -= actions_benefices_reels[n-1]["prix"]

        n -= 1

    return matrice[-1][-1], elements_selection

def calcul_meilleur_placement_optimized(portefeuille, actions):
    actions_benefices_reels = calculer_benefice(actions)
    return sacADos_dynamique(portefeuille, actions_benefices_reels)
    

def placement_optimized(portefeuille, actions):
    meilleur_benefice, selection = calcul_meilleur_placement_optimized(portefeuille, actions)
    prix_actions =[]
    print("Meilleur bénéfice : ", meilleur_benefice)
    print(f"Grâce aux {len(selection)} actions suivantes :")
    for action_choisie in selection:
        print(action_choisie["produit"], "prix : ",action_choisie["prix"])
        prix_actions.append(action_choisie["prix"])
    print(f"Pour un investissement de {sum(prix_actions)} euros.")
 
portefeuille = 500
placement_optimized(portefeuille, actions)