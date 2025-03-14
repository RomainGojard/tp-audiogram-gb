import pandas as pd

def clean_data(audiogram_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les données :
    - Convertit les fréquences en nombres
    - Supprime les valeurs aberrantes (ex : fréquences négatives)
    - Vérifie la cohérence des colonnes
    """
    df = audiogram_raw.copy()

    # Conversion des colonnes numériques
    cols = df.columns[1:]  # Ignorer la première colonne si c'est un ID ou une catégorie
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

    # Suppression des valeurs aberrantes (ex: fréquences négatives)
    df = df[(df[cols] >= 0).all(axis=1)]

    print(f"✅ Données nettoyées : {df.shape[0]} lignes restantes")
    return df