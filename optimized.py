actions = [
    {"name":"action 1", "price":20, "profit":5},
    {"name":"action 2", "price":30, "profit":10},
    {"name":"action 3", "price":50, "profit":15},
    {"name":"action 4", "price":70, "profit":20},
    {"name":"action 5", "price":60, "profit":17},
    {"name":"action 6", "price":80, "profit":25},
    {"name":"action 7", "price":22, "profit":7},
    {"name":"action 8", "price":26, "profit":11},
    {"name":"action 9", "price":48, "profit":13},
    {"name":"action 10", "price":34, "profit":27},
    {"name":"action 11", "price":42, "profit":17},
    {"name":"action 12", "price":110, "profit":9},
    {"name":"action 13", "price":38, "profit":23},
    {"name":"action 14", "price":14, "profit":1},
    {"name":"action 15", "price":18, "profit":3},
    {"name":"action 16", "price":8, "profit":8},
    {"name":"action 17", "price":4, "profit":12},
    {"name":"action 18", "price":10, "profit":14},
    {"name":"action 19", "price":24, "profit":21},
    {"name":"action 20", "price":114, "profit":18}
    ]


def calculer_benefice(actions):
    # Calcul du bénéfice réel pour chaque action
    actions_benefices_reels = []
    for action in actions:
        produit = action["name"]
        prix = action["price"]
        pourcent = action["profit"]
        benefice_reel = (prix * pourcent)/100
        actions_benefices_reels.append({"name":produit,"price":prix,"benefice_reel":benefice_reel})
    return actions_benefices_reels


def remplir_matrice(portefeuille, actions_benefices_reels, matrice):
    #remplissage de la matrice (du tableau)
    #_ : variable jetable
    for i in range(1, len(actions_benefices_reels) + 1):
        prix = int(actions_benefices_reels[i-1]["price"]*100) 
        benefice_reel = int(actions_benefices_reels[i-1]["benefice_reel"]*100)
        for w in range(1, portefeuille + 1):
            if prix <= w:
                matrice[i][w] = max(benefice_reel + matrice[i-1][w-prix], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    return matrice


def retrouver_actions_selectionnees(portefeuille, actions_benefices_reels, matrice):
    # Retrouver les actions en fonction du portefeuille
    w = portefeuille
    n = len(actions_benefices_reels)
    elements_selection = []

    while w >= 0 and n >= 0:
        if matrice[n][w] != matrice[n-1][w]:
            elements_selection.append(actions_benefices_reels[n-1])
            w -= int(actions_benefices_reels[n-1]["price"]*100)
        n -= 1
    return elements_selection


def sacADos_dynamique(portefeuille, actions_benefices_reels):
    #Création de la matrice à deux dimensions, retourne le bénéfice maximal et la liste des actions sélectionnées
    #_ : variable jetable
    matrice = [[0 for _ in range(portefeuille + 1)] for _ in range(len(actions_benefices_reels) + 1)]
    matrice = remplir_matrice(portefeuille, actions_benefices_reels, matrice)
    elements_selection = retrouver_actions_selectionnees(portefeuille, actions_benefices_reels, matrice)
    return matrice[-1][-1]/100, elements_selection


def calcul_meilleur_placement_optimized(portefeuille, actions):
    portefeuille_centimes = int(portefeuille*100)
    actions_benefices_reels = calculer_benefice(actions)
    return sacADos_dynamique(portefeuille_centimes, actions_benefices_reels)
    

def placement_optimized(portefeuille, actions):
    meilleur_benefice, selection = calcul_meilleur_placement_optimized(portefeuille, actions)
    prix_actions =[]
    print("Meilleur bénéfice : ", meilleur_benefice)
    print(f"Grâce aux {len(selection)} actions suivantes :")
    for action_choisie in selection:
        print(action_choisie["name"], "prix : ",action_choisie["price"], "profit : ", action_choisie["benefice_reel"])
        prix_actions.append(action_choisie["price"])
    print(f"Pour un investissement de {sum(prix_actions)} euros.")
 

#portefeuille = 500
#placement_optimized(portefeuille, actions)