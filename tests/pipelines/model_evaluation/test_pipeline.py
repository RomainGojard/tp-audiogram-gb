"""
This is a boilerplate test file for pipeline 'model_evaluation'
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
from sklearn.metrics import mean_squared_error, r2_score
from src.tp_audiogram_gb.pipelines.model_evaluation.nodes import evaluate_model

@pytest.fixture
def mock_data():
    # Génère des données factices pour les tests
    X_test = pd.DataFrame(np.random.rand(10, 5), columns=[f"feature_{i}" for i in range(5)])
    y_test = pd.DataFrame(np.random.rand(10, 1), columns=["target"])
    y_min = pd.Series([0] * 10)
    y_max = pd.Series([1] * 10)
    return X_test, y_test, y_min, y_max

@pytest.fixture
def mock_model():
    # Crée un modèle factice entraîné
    model = RandomForestRegressor(random_state=42)
    X_train = np.random.rand(50, 5)
    y_train = np.random.rand(50)
    model.fit(X_train, y_train)
    return model

def test_evaluate_model(mock_model, mock_data):
    # Teste la fonction evaluate_model
    X_test, y_test, y_min, y_max = mock_data
    trained_model = mock_model

    metrics = evaluate_model(trained_model, X_test, y_test, y_min, y_max)

    # Vérifie que les métriques sont calculées correctement
    assert "mean_squared_error" in metrics, "MSE is missing in the evaluation metrics"
    assert "r2_score" in metrics, "R² is missing in the evaluation metrics"
    assert isinstance(metrics["mean_squared_error"], float), "MSE is not a float"
    assert isinstance(metrics["r2_score"], float), "R² is not a float"
    assert 0 <= metrics["r2_score"] <= 1, "R² is out of range [0, 1]"
