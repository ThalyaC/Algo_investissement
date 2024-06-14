from optimized import placement_optimized
from csv_cleaner import clean_data

def optimiz_csv(fichier, portefeuille, profit_pourcent_min):
    data_cleaned = clean_data(fichier, profit_pourcent_min)
    placement_optimized(portefeuille, data_cleaned)

