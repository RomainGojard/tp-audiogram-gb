"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import pickle

mlflow.autolog()

def evaluate_model(trained_model, X_test, y_test, y_min, y_max):
    """
    Évalue le modèle en dénormalisant les prédictions et en calculant les métriques.
    """
    # Effectuer les prédictions
    predictions_normalized = trained_model.predict(X_test)

    # Dénormaliser les prédictions
    predictions = predictions_normalized * (y_max - y_min) + y_min

    # Dénormaliser y_test
    y_test = y_test * (y_max - y_min) + y_min

    # Calculer l'erreur quadratique moyenne (MSE)
    mse = mean_squared_error(y_test, predictions)
    print(f"✅ Erreur quadratique moyenne (MSE) : {mse}")

    # Calculer le coefficient de détermination (R²)
    r2 = r2_score(y_test, predictions)
    print(f"✅ Coefficient de détermination (R²) : {r2}")

    return {"mean_squared_error": mse, "r2_score": r2}