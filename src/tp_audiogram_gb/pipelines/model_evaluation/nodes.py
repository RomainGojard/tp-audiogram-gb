"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import pickle

mlflow.autolog()

def evaluate_model(trained_model, X_test, y_test):
    """
    Évalue le modèle en calculant la précision sur les données de test.
    """
    # Charger le modèle depuis le fichier
    #print(trained_model)
    #with open(trained_model, "rb") as f:
    #   trained_model = pickle.load(f)
    
    # Effectuer les prédictions
    predictions = trained_model.predict(X_test)
    
    # Calculer l'erreur quadratique moyenne (MSE)
    mse = mean_squared_error(y_test, predictions)
    print(f"✅ Erreur quadratique moyenne (MSE) : {mse}")
    
    # Calculer le coefficient de détermination (R²)
    r2 = r2_score(y_test, predictions)
    print(f"✅ Coefficient de détermination (R²) : {r2}")
    
    return {"mean_squared_error": mse, "r2_score": r2}