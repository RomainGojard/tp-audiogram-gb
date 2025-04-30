import pandas as pd
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.autolog()

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

    # Suppression des lignes contenant des valeurs manquantes
    df = df.dropna()

    # Supression des valeurs avec des lettres
    df = df[~df.apply(lambda x: x.astype(str).str.contains('[a-zA-Z]').any(), axis=1)]

    # # Stockage des extrémums (min et max) de chaque colonne
    # extremums = {col: {"min": df[col].min(), "max": df[col].max()} for col in df.columns}
    # # print(f"📊 Extrémums des colonnes : {extremums}")

    # for col in df.columns:
    #     min_val = extremums[col]["min"]
    #     max_val = extremums[col]["max"]
    #     df[col] = (df[col] - min_val) / (max_val - min_val)


    print(f"✅ Données nettoyées : {df.shape[0]} lignes restantes, {df.shape[1]} colonnes")
    return df