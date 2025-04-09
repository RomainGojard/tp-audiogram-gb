"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.11
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.autolog()

def split_data(df: pd.DataFrame, test_size: float = 0.2):
    """
    Prépare les données, les normalise et les sépare en ensembles d'entraînement et de test.
    """
    # Sélectionner les colonnes avant et après traitement
    before_cols = [col for col in df.columns if col.startswith("before_exam")]
    after_cols = [col for col in df.columns if col.startswith("after_exam")]

    # Vérifier que les colonnes correspondent
    assert len(before_cols) == len(after_cols), "Les colonnes avant et après traitement ne correspondent pas."

    # Caractéristiques (X) : valeurs avant traitement
    X = df[before_cols]

    # Cible (y) : valeurs après traitement
    y = df[after_cols]

    # Normaliser X
    X_min = X.min()
    X_max = X.max()
    X_normalized = (X - X_min) / (X_max - X_min)

    # Normaliser y
    y_min = y.min()
    y_max = y.max()
    y_normalized = (y - y_min) / (y_max - y_min)

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X_normalized, y_normalized, test_size=test_size, random_state=42)
    print(f"Données divisées en train ({len(X_train)}) et test ({len(X_test)})")

    # Retourner les données normalisées et les paramètres de normalisation
    return X_train, X_test, y_train, y_test, X_min, X_max, y_min, y_max

def train_model(X_train, y_train):
    """
    Entraîne un modèle RandomForestRegressor pour prédire l'augmentation de l'ouïe.
    """
    # Définir le modèle
    model = RandomForestRegressor(random_state=42)

    # Définir les hyperparamètres à optimiser
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    # Optimisation des hyperparamètres avec GridSearchCV
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=3,  # Validation croisée à 3 plis
        scoring="neg_mean_squared_error",
        verbose=1,
        n_jobs=-1
    )

    # Entraîner le modèle
    grid_search.fit(X_train, y_train)

    # Meilleur modèle
    best_model = grid_search.best_estimator_
    print(f"✅ Modèle entraîné avec succès avec les meilleurs paramètres : {grid_search.best_params_}")

    return best_model

def save_model(model, filepath: str):
    """
    Sauvegarde le modèle entraîné sous forme de fichier pickle.
    """
    with open(filepath, "wb") as f:
        pickle.dump(model, f)
    
    print(f"✅ Modèle sauvegardé dans {filepath}")


def node_master_model_training(tonal_exams_clean: pd.DataFrame) -> tuple:
    """
    Fonction principale du pipeline `model_training` qui orchestre les étapes.
    """
    X_train, X_test, y_train, y_test, X_min, X_max, y_min, y_max = split_data(tonal_exams_clean)
    model = train_model(X_train, y_train)

    # Convertir les Series en DataFrame pour permettre la sauvegarde
    X_min = X_min.to_frame(name="X_min")
    X_max = X_max.to_frame(name="X_max")
    y_min = y_min.to_frame(name="y_min")
    y_max = y_max.to_frame(name="y_max")

    # Retourner le modèle, les données de test et les paramètres de normalisation
    return model, X_test, y_test, X_min, X_max, y_min, y_max
