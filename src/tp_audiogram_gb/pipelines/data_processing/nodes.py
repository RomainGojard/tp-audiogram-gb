import pandas as pd

def clean_data(audiogram_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les données :
    - Convertit les colonnes en valeurs numériques
    - Supprime les valeurs aberrantes (ex : fréquences négatives ou non numériques)
    - Supprime les colonnes inutiles
    - Supprime les lignes contenant des valeurs manquantes
    """
    df = audiogram_raw.copy()

    # Conversion des colonnes en valeurs numériques
    df = df.apply(pd.to_numeric, errors="coerce")

    # Suppression des colonnes inutiles (si elles ne commencent pas par "before_exam" ou "after_exam")
    valid_columns = [col for col in df.columns if col.startswith("before_exam") or col.startswith("after_exam")]
    df = df[valid_columns]

    # Suppression des valeurs aberrantes (valeurs négatives)
    df = df[(df >= 0).all(axis=1)]

    # Suppression des lignes contenant des valeurs manquantes
    df = df.dropna()

    # Stockage des extrémums (min et max) de chaque colonne
    extremums = {col: {"min": df[col].min(), "max": df[col].max()} for col in df.columns}
    # print(f"📊 Extrémums des colonnes : {extremums}")

    for col in df.columns:
        min_val = extremums[col]["min"]
        max_val = extremums[col]["max"]
        df[col] = (df[col] - min_val) / (max_val - min_val)


    print(f"✅ Données nettoyées : {df.shape[0]} lignes restantes, {df.shape[1]} colonnes")
    return df