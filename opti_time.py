from time import perf_counter

from optimized import placement_optimized
from csv_cleaner import clean_data

def optimiz_csv(fichier, portefeuille):
    data_cleaned = clean_data(fichier)
    placement_optimized(portefeuille, data_cleaned)

start_time = perf_counter()

portefeuille = 500
fichier = "dataset1_Python+P7.csv"
optimiz_csv(fichier, portefeuille)

end_time = perf_counter()
time_execution_prog = end_time - start_time

print(f"Ce programme a été exécuté en {time_execution_prog} secondes")