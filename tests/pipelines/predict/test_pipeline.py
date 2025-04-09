"""
This is a boilerplate test file for pipeline 'predict'
generated using Kedro 0.19.11.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
import pandas as pd
import numpy as np
from unittest.mock import MagicMock
from src.tp_audiogram_gb.pipelines.predict.nodes import predict_user_inputs

@pytest.fixture
def mock_user_inputs():
    # Génère des données utilisateur factices
    data = {
        "before_exam_125_Hz": [10, 20, 30],
        "before_exam_250_Hz": [15, 25, 35],
        "before_exam_500_Hz": [20, 30, 40],
    }
    return pd.DataFrame(data)

@pytest.fixture
def mock_trained_model():
    # Crée un modèle factice avec une méthode predict
    mock_model = MagicMock()
    mock_model.predict.return_value = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
    return mock_model

@pytest.fixture
def mock_normalization_params():
    # Génère des paramètres de normalisation factices
    X_min = pd.DataFrame({"before_exam_125_Hz": [0], "before_exam_250_Hz": [0], "before_exam_500_Hz": [0]})
    X_max = pd.DataFrame({"before_exam_125_Hz": [100], "before_exam_250_Hz": [100], "before_exam_500_Hz": [100]})
    return X_min, X_max
