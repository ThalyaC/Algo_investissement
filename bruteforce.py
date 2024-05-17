actions = {1:[20,5],2:[30,10],3:[50,15],4:[70,20],5:[60,17],6:[80,25],7:[22,7],8:[26,11],9:[48,13],10:[34,27],11:[42,17],12:[110,9],13:[38,23],14:[14,1],15:[18,3],16:[8,8],17:[4,12],18:[10,14],19:[24,21],20:[114,18]}


def calculer_benefice(actions):
    # Calcul du bénéfice réel pour chaque action
    for action, details in actions.items():
        prix_depart, benefice_pourcent = details
        benefice_reel = (prix_depart * benefice_pourcent)/100
        actions[action].append(benefice_reel)
    return actions


def calcul_code_binaire_combi(actions):
    # créer des structures binaires pour ensuite enregistrer des combinaisons d'actions
    n=len(actions)
    nombre_combinaisons = 2**n
    i = 0
    liste_combi_mode_binaire = []
    while i != nombre_combinaisons:
        combi = bin(i)[2:]
        liste_combi_mode_binaire.append(combi)
        i += 1
    return liste_combi_mode_binaire

def calcul_combinaisons_actions(actions):
    # Calculer toutes les possibilités de combinaisons d'actions
    actions_avec_benefices_reels = calculer_benefice(actions)
    liste_type = calcul_code_binaire_combi(actions)
    liste_combi_actions = []
    
    for nombre_binaire in liste_type:
        combi_actions = []
        for j in range(len(nombre_binaire)):
            if nombre_binaire[j] == "1":
                combi_actions.append(actions_avec_benefices_reels[j+1])
        liste_combi_actions.append(combi_actions)
    print(f"\n\033[0;33m{len(liste_combi_actions)} \033[0;34mcombinaisons avec \033[0;33m{len(actions)} \033[0;34mactions\033[0m \n")
    print(f"\033[0;34mExemple : une combinaison \n \033[0;33m {liste_combi_actions[2000]}\033[0m \n") 
        
    return liste_combi_actions

def calcul_combi_actions_portefeuille_max(actions, portefeuille_max):
    # Calcule la liste des combinaisons possibles en fonction d'un portefeuille donné
    liste_combi_actions = calcul_combinaisons_actions(actions)
    liste_combi_actions_portefeuille =[]
    
    for combi in liste_combi_actions:
        somme = 0
        for action in combi:
            somme += action[0]
        if somme <= portefeuille_max:
            liste_combi_actions_portefeuille.append(combi)
    print(f"\033[0;33m{len(liste_combi_actions_portefeuille)} \033[0;34mcombinaisons dont la somme est inférieure à \033[0;33m{portefeuille_max} \033[0;34meuros \033[0m")
    
    #878512 au lieu de 1 048 576 combinaisons
    return liste_combi_actions_portefeuille

def calcul_meilleur_placement(actions):
    liste_portefeuille_max=calcul_combi_actions_portefeuille_max(actions, portefeuille_max)
    liste_profit_combi = []

    for combi in liste_portefeuille_max:
        somme = 0
        for action in combi:
            somme += action[2]
        liste_profit_combi.append([combi,somme])
    liste_profit_combi.sort(key=lambda x: x[1], reverse=True)
    print(f"\n \033[0;34mLa meilleure combinaison est : \n \033[0;33m{liste_profit_combi[0]}\033[0m")
    
    meilleur_placement = liste_profit_combi[0]
    actions_achetees = meilleur_placement[0]
    somme2 = 0
    for action_achetee in actions_achetees:
        somme2 += action_achetee[0]
    print(f"\033[0;34mVous investissez \033[0;33m{somme2} \033[0;34meuros dans \033[0;33m{len(actions_achetees)} \033[0;34mactions aujourd'hui et vous gagnez \033[0;33m{meilleur_placement[1]} \033[0;34meuros dans 2 ans\033[0m")
    
    



        

portefeuille_max = 500
calcul_meilleur_placement(actions)
#calcul_liste_portefeuille_max(actions, portefeuille_max)
#list_type_combinaisons_possibles(actions)
#list_combinaisons_actions(actions)
#Calcul de la liste des actions les plus rentables
