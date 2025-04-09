"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.19.11
"""

import pandas as pd
import numpy as np
import pickle

def predict_user_inputs(user_inputs: pd.DataFrame, trained_model, X_min: pd.DataFrame, X_max: pd.DataFrame, y_min: pd.DataFrame, y_max: pd.DataFrame) -> pd.DataFrame:
    """
    Effectue une prédiction à partir des données utilisateur en normalisant les entrées
    et en dénormalisant les prédictions.
    """
    # Charger le modèle entraîné

    # Normaliser les entrées utilisateur
    X_min = X_min.squeeze()  # Convertir en Series si nécessaire
    X_max = X_max.squeeze()
    user_inputs_normalized = (user_inputs - X_min) / (X_max - X_min)

    # Effectuer les prédictions
    predictions_normalized = trained_model.predict(user_inputs_normalized)

    # # Dénormaliser les prédictions
    # y_min = y_min.squeeze()  # Convertir en Series si nécessaire
    # y_max = y_max.squeeze()
    predictions = predictions_normalized * (y_max - y_min) + y_min

    # Retourner les prédictions sous forme de DataFrame
    predictions_df = pd.DataFrame(predictions, columns=[f"after_exam_{col}" for col in user_inputs.columns])
    return predictions_df
