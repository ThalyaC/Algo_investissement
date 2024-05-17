actions = {1:[20,5],2:[30,10],3:[50,15],4:[70,20],5:[60,17],6:[80,25],7:[22,7],8:[26,11],9:[48,13],10:[34,27],11:[42,17],12:[110,9],13:[38,23],14:[14,1],15:[18,3],16:[8,8],17:[4,12],18:[10,14],19:[24,21],20:[114,18]}

# Calcul du bénéfice réel pour chaque action

def calculer_benefice(actions):
    for action, details in actions.items():
        prix_depart, benefice_pourcent = details
        benefice_reel = (prix_depart * benefice_pourcent)/100
        actions[action].append(benefice_reel)

    #print("actions =", actions)
    return actions

def calcul_type_combinaisons_possibles(actions):
    n=len(actions)
    nombre_combinaisons = 2**n
    i = 0
    liste_combi_mode_binaire = []
    while i != nombre_combinaisons:
        combi = bin(i)[2:]
        liste_combi_mode_binaire.append(combi)
        i += 1
    #print(liste_combi_mode_binaire[1])
    return liste_combi_mode_binaire

def calcul_combinaisons_actions(actions):
    actions_avec_benefices_reels = calculer_benefice(actions)
    liste_type = calcul_type_combinaisons_possibles(actions)
    liste_combi_actions = []
    
    for nombre_binaire in liste_type:
        combi_actions = []
        for j in range(len(nombre_binaire)):
            if nombre_binaire[j] == "1":
                combi_actions.append(actions_avec_benefices_reels[j+1])
        liste_combi_actions.append(combi_actions)
    #print(liste_combi_actions[2000]) 
    #résultat :[[20, 5, 1.0], [30, 10, 3.0], [50, 15, 7.5], [70, 20, 14.0], [60, 17, 10.2], [22, 7, 1.54]]
    
    return liste_combi_actions

def calcul_liste_portefeuille_max(actions, portefeuille_max):
    liste_combi_actions = calcul_combinaisons_actions(actions)
    liste_combi_actions_portefeuille =[]
    somme = 0
    for combi in liste_combi_actions:
        
        for action in combi:
            somme += action[0]
            if somme <= portefeuille_max:
                liste_combi_actions_portefeuille.append(combi)
    print(len(liste_combi_actions_portefeuille))
    
    #352030 au lieu de 1 048 576
    return liste_combi_actions_portefeuille

def calcul_meilleur_placement(actions):
    liste_portefeuille_max=calcul_liste_portefeuille_max(actions, portefeuille_max)
    liste_profit_combi = []

    for combi in liste_portefeuille_max:
        somme = 0
        for action in combi:
            somme += action[2]
        liste_profit_combi.append([combi,somme])
    liste_profit_combi.sort(key=lambda x: x[1], reverse=True)
    print(liste_profit_combi[0])
    
    meilleur_placement = liste_profit_combi[0]
    actions_achetees = meilleur_placement[0]
    somme2 = 0
    for action_achetee in actions_achetees:
        somme2 += action_achetee[0]
    print(f"Vous investissez {somme2} euros dans {len(actions_achetees)} actions aujourd'hui et vous gagnez {meilleur_placement[1]} euros dans 2 ans")
    
    



        

portefeuille_max = 500
calcul_meilleur_placement(actions)
#calcul_liste_portefeuille_max(actions, portefeuille_max)
#list_type_combinaisons_possibles(actions)
#list_combinaisons_actions(actions)
#Calcul de la liste des actions les plus rentables
