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
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from src.tp_audiogram_gb.pipelines.model_evaluation.nodes import evaluate_model

@pytest.fixture
def mock_data():
    """
    Génère des données factices pour les tests.
    """
    X_test = pd.DataFrame(np.random.rand(10, 5), columns=[f"feature_{i}" for i in range(5)])
    y_test = pd.DataFrame(np.random.rand(10, 1), columns=["target"])
    y_min = pd.Series([0])  # Longueur 1
    y_max = pd.Series([1])  # Longueur 1
    return X_test, y_test, y_min, y_max

@pytest.fixture
def mock_model():
    """
    Crée un modèle factice entraîné.
    """
    model = RandomForestRegressor(random_state=42)
    X_train = np.random.rand(50, 5)
    y_train = np.random.rand(50)
    model.fit(X_train, y_train)
    return model

def test_evaluate_model(mock_model, mock_data):
    """
    Teste la fonction evaluate_model.
    """
    X_test, y_test, y_min, y_max = mock_data
    trained_model = mock_model

    # Appeler la fonction evaluate_model
    metrics = evaluate_model(trained_model, X_test, y_test, y_min, y_max)

    # Vérifier que les métriques sont calculées correctement
    assert "mean_squared_error" in metrics, "MSE is missing in the evaluation metrics"
    assert "mean_absolute_error" in metrics, "MAE is missing in the evaluation metrics"
    assert "r2_score" in metrics, "R² is missing in the evaluation metrics"

    # Vérifier les types des métriques
    assert isinstance(metrics["mean_squared_error"], float), "MSE is not a float"
    assert isinstance(metrics["mean_absolute_error"], float), "MAE is not a float"
    assert isinstance(metrics["r2_score"], float), "R² is not a float"

    print(f"✅ R2: {metrics['r2_score']}")

    # Vérifier les plages de valeurs
    assert metrics["mean_squared_error"] >= 0, "MSE should be non-negative"
    assert metrics["mean_absolute_error"] >= 0, "MAE should be non-negative"