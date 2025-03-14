"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.11
"""
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import mlflow

mlflow.autolog()

def split_data(df: pd.DataFrame, test_size: float = 0.2):
    """
    Sépare les données en train/test.
    """
    X = df.drop(columns=["mean_variation"])
    y = df["mean_variation"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    print(f"Données divisées en train ({len(X_train)}) et test ({len(X_test)})")
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Entraîne un modèle RandomForestRegressor.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("Modèle entraîné avec succès")
    return model

def save_model(model, filepath: str):
    """
    Sauvegarde le modèle entraîné sous forme de fichier pickle.
    """
    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    
    print(f"✅ Modèle sauvegardé dans {filepath}")


def node_master_model_training(audiogram_features: pd.DataFrame) -> tuple:
    """
    Fonction principale du pipeline `model_training` qui orchestre les étapes.
    """
    X_train, X_test, y_train, y_test = split_data(audiogram_features)
    model = train_model(X_train, y_train)
    save_model(model, "data/06_models/trained_model.pkl")
    
    return "data/06_models/trained_model.pkl", X_test, y_test
