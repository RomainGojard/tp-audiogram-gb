"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import pickle
import pandas as pd
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.autolog()

def evaluate_model(trained_model, X_test, y_test, y_min, y_max):
    """
    Évalue le modèle en dénormalisant les prédictions et en calculant les métriques.
    """
    # Si y_min et y_max sont des DataFrame, convertir en Series
    if isinstance(y_min, pd.DataFrame):
        y_min = y_min.squeeze()  # Convertir en Series
    if isinstance(y_max, pd.DataFrame):
        y_max = y_max.squeeze()  # Convertir en Series

    # Vérifier les dimensions après conversion
    print(f"Dimensions après conversion - y_min : {y_min.shape}, y_max : {y_max.shape}")

    # Effectuer les prédictions
    predictions_normalized = trained_model.predict(X_test)

    # Dénormaliser les prédictions (diffusion colonne par colonne)
    predictions = predictions_normalized * (y_max.values - y_min.values) + y_min.values

    # Dénormaliser y_test (diffusion colonne par colonne)
    y_test = y_test * (y_max.values - y_min.values) + y_min.values

    # Calculer l'erreur quadratique moyenne (MSE)
    mse = mean_squared_error(y_test, predictions)
    print(f"✅ Erreur quadratique moyenne (MSE) : {mse}")

    mae = mean_absolute_error(y_test, predictions)
    print(f"✅ Erreur absolue moyenne (MAE) : {mae}")

    # Calculer le coefficient de détermination (R²)
    r2 = r2_score(y_test, predictions)
    print(f"✅ Coefficient de détermination (R²) : {r2}")

    return {"mean_squared_error": mse, "r2_score": r2, "mean_absolute_error": mae}