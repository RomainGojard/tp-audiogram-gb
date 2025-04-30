"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.19.11
"""

import pandas as pd
import numpy as np
import json
import pickle

def predict_user_inputs(user_inputs: json, trained_model, X_min: pd.DataFrame, X_max: pd.DataFrame, y_min: pd.DataFrame, y_max: pd.DataFrame) -> dict:
    """
    Effectue une prédiction à partir des données utilisateur en normalisant les entrées
    et en dénormalisant les prédictions.
    """

    # Extraire les données utilisateur et les convertir en DataFrame (1, 7)
    user_inputs_data = pd.DataFrame([user_inputs['data']])  # Crée un DataFrame avec une seule ligne

    # Normaliser les entrées utilisateur
    X_min = X_min.squeeze()  # Convertir en Series si nécessaire
    X_max = X_max.squeeze()
    user_inputs_normalized = (user_inputs_data - X_min) / (X_max - X_min)

    # Effectuer les prédictions
    predictions_normalized = trained_model.predict(user_inputs_normalized)

    # Dénormaliser les prédictions
    y_min = y_min.squeeze()  # Convertir en Series si nécessaire
    y_max = y_max.squeeze()
    predictions = predictions_normalized * (y_max.values - y_min.values) + y_min.values

    # S'assurer que predictions est un tableau 2D
    if len(predictions.shape) == 1:  # Si predictions est 1D
        predictions = predictions.reshape(1, -1)  # Convertir en 2D

    # Retourner les prédictions sous forme de DataFrame
    predictions_df = pd.DataFrame(predictions, columns=[f"after_exam_{col}" for col in user_inputs_data.columns])

    # Convertir le DataFrame en un dictionnaire compatible avec JSON
    predictions_dict = predictions_df.to_dict(orient="records")  # Convertir en une liste de dictionnaires
    return predictions_dict
