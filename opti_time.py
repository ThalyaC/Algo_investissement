from time import perf_counter
from optimized_csv import optimiz_csv

portefeuille = 500
profit_pourcent_min = input("Pour chaque action, quel pourcentage minimum de profit souhaitez-vous?")
fichier = "dataset1_Python+P7.csv"
#"data_essai.csv"
#"dataset2_Python+P7.csv"
start_time = perf_counter()
optimiz_csv(fichier, portefeuille, profit_pourcent_min)

end_time = perf_counter()
time_execution_prog = end_time - start_time

print(f"Ce programme a été exécuté en {time_execution_prog} secondes")