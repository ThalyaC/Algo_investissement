def calculer_benefice(actions):
    """Calcul du bénéfice réel pour chaque action"""
    actions_benefices_reels = []
    for action in actions:
        produit = action["name"]
        prix = action["price"]
        pourcent = action["profit"]
        benefice_reel = (prix * pourcent)/100
        actions_benefices_reels.append({"name":produit,"price":prix,"benefice_reel":benefice_reel})
    return actions_benefices_reels


def remplir_matrice(portefeuille, actions_benefices_reels, matrice):
    """Remplissage de la matrice (du tableau)"""
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
    """Retrouver les actions en fonction du portefeuille"""
    n = len(actions_benefices_reels)
    elements_selection = []

    while portefeuille >= 0 and n >= 0:
        if matrice[n][portefeuille] != matrice[n-1][portefeuille]:
            elements_selection.append(actions_benefices_reels[n-1])
            portefeuille -= int(actions_benefices_reels[n-1]["price"]*100)
        n -= 1
    return elements_selection


def sacADos_dynamique(portefeuille, actions_benefices_reels):
    """Création de la matrice à deux dimensions, retourne le bénéfice maximal et la liste des actions sélectionnées"""
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
    somme_prix_actions = sum(prix_actions)
    somme_prix_actions_decimal = float(somme_prix_actions)
    investissement_arrondi = arrondir_investissement(somme_prix_actions_decimal)
    print(f"Pour un investissement de {investissement_arrondi} euros.")
 
def arrondir_investissement(investissement_brut):
    investissement_brut_str = str(investissement_brut)
    virgule_investissement = investissement_brut_str.index(".")
    investissement_arrondi = investissement_brut_str[:virgule_investissement + 3]
    return investissement_arrondi

