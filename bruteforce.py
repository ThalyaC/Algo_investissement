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
    """Calculer le bénéfice réel pour chaque action"""
    for action in actions:
        prix_depart, benefice_pourcent = action["price"], action["profit"]
        benefice_reel = (prix_depart * benefice_pourcent)/100
        action["benefice_reel"] = benefice_reel
    return actions


def calcul_code_binaire_combi(actions):
    """Créer les structures binaires pour ensuite enregistrer les combinaisons d'actions"""
    n=len(actions)
    nombre_combinaisons = 2**n
    i = 0
    liste_combi_mode_binaire = []
    while i != nombre_combinaisons:
        combi = bin(i)[2:]
        liste_combi_mode_binaire.append(combi)
        i += 1
    for i in range(len(liste_combi_mode_binaire)):
        while len(liste_combi_mode_binaire[i]) != n:
            liste_combi_mode_binaire[i] = "0" + liste_combi_mode_binaire[i]
    
    return liste_combi_mode_binaire


def calcul_combinaisons_actions(actions):
    """Calculer toutes les possibilités de combinaisons d'actions"""
    actions_avec_benefices_reels = calculer_benefice(actions)
    liste_type = calcul_code_binaire_combi(actions)
    liste_combi_actions = []
    
    for nombre_binaire in liste_type:
        combi_actions = []
        for j in range(len(nombre_binaire)):
            if nombre_binaire[j] == "1":
                combi_actions.append(actions_avec_benefices_reels[j]) #
        liste_combi_actions.append(combi_actions)
    print(f"\n\033[0;33m{len(liste_combi_actions)} \033[0;34mcombinaisons avec \033[0;33m{len(actions)} \033[0;34mactions\033[0m \n")   
    return liste_combi_actions


def calcul_combi_actions_portefeuille_max(actions, portefeuille_max):
    """Calculer la liste des combinaisons possibles en fonction d'un portefeuille donné"""
    liste_combi_actions = calcul_combinaisons_actions(actions)
    liste_combi_actions_portefeuille =[]
    
    for combi in liste_combi_actions:
        somme_price = 0
        for action in combi:
            somme_price += action["price"]
        if somme_price <= portefeuille_max:
            liste_combi_actions_portefeuille.append(combi)
    print(f"{len(liste_combi_actions_portefeuille)} combinaisons dont la somme est inférieure à {portefeuille_max} euros")
    
    return liste_combi_actions_portefeuille


def calcul_meilleur_placement(actions, portefeuille_max):
    """Calculer le meilleur placement"""
    liste_portefeuille_max=calcul_combi_actions_portefeuille_max(actions, portefeuille_max)
    liste_profit_combi = []

    for combi in liste_portefeuille_max:
        somme_benefice_reel = 0
        for action in combi:
            somme_benefice_reel += action["benefice_reel"] #action[2]
        liste_profit_combi.append([combi,somme_benefice_reel])
    liste_profit_combi.sort(key=lambda x: x[1], reverse=True)
    selection = liste_profit_combi[0][0]
    print("\nLa meilleure combinaison est :")
    for action_choisie in selection:
        print(action_choisie["name"], "prix : ",action_choisie["price"], "euros --> Profit : ", action_choisie["benefice_reel"], "euros")
        
    meilleur_placement = liste_profit_combi[0]
    actions_achetees = meilleur_placement[0]
    somme_actions_achetees = 0
    for action_achetee in actions_achetees:
        somme_actions_achetees += action_achetee["price"] #[0]
    print(f"\n\033[0;34mVous investissez \033[0;33m{somme_actions_achetees} \033[0;34meuros dans \033[0;33m{len(actions_achetees)} \033[0;34mactions aujourd'hui et vous gagnez \033[0;33m{meilleur_placement[1]} \033[0;34meuros dans 2 ans.\033[0m \n")
        

portefeuille_max = 500
calcul_meilleur_placement(actions, portefeuille_max)