"""
This is a boilerplate test file for pipeline 'model_training'
generated using Kedro 0.19.11.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from src.tp_audiogram_gb.pipelines.model_training.nodes import (
    split_data,
    train_model,
    save_model,
)

@pytest.fixture
def mock_data():
    # Génère des données factices pour les tests
    data = {
        "before_exam_125_Hz": np.random.rand(100),
        "before_exam_250_Hz": np.random.rand(100),
        "before_exam_500_Hz": np.random.rand(100),
        "after_exam_125_Hz": np.random.rand(100),
        "after_exam_250_Hz": np.random.rand(100),
        "after_exam_500_Hz": np.random.rand(100),
    }
    return pd.DataFrame(data)

def test_split_data(mock_data):
    # Teste la fonction split_data
    df = mock_data
    X_train, X_test, y_train, y_test, X_min, X_max, y_min, y_max = split_data(df)

    # Vérifie les dimensions des ensembles
    assert len(X_train) > 0, "X_train est vide"
    assert len(X_test) > 0, "X_test est vide"
    assert len(y_train) > 0, "y_train est vide"
    assert len(y_test) > 0, "y_test est vide"

    # Vérifie que les normalisations sont correctes
    assert (X_train.max().max() <= 1) and (X_train.min().min() >= 0), "X_train n'est pas normalisé"
    assert (y_train.max().max() <= 1) and (y_train.min().min() >= 0), "y_train n'est pas normalisé"

def test_train_model(mock_data):
    # Teste la fonction train_model
    df = mock_data
    X_train, X_test, y_train, y_test, _, _, _, _ = split_data(df)

    model = train_model(X_train, y_train)

    # Vérifie que le modèle est entraîné
    assert isinstance(model, RandomForestRegressor), "Le modèle entraîné n'est pas un RandomForestRegressor"
    assert hasattr(model, "predict"), "Le modèle entraîné ne possède pas de méthode predict"

def test_save_model(tmp_path):
    # Teste la fonction save_model
    model = RandomForestRegressor()
    model.fit(np.random.rand(10, 5), np.random.rand(10))  # Entraîne un modèle factice

    filepath = tmp_path / "test_model.pkl"
    save_model(model, filepath)

    # Vérifie que le fichier est créé
    assert filepath.exists(), "Le fichier modèle n'a pas été sauvegardé"
