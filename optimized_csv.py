from optimized import placement_optimized
from csv_cleaner import clean_data

def optimiz_csv(fichier, portefeuille):
    data_cleaned = clean_data(fichier)
    placement_optimized(portefeuille, data_cleaned)

portefeuille = 500
fichier = "dataset2_Python+P7.csv"
optimiz_csv(fichier, portefeuille)