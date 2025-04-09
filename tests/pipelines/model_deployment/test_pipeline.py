"""
This is a boilerplate test file for pipeline 'model_deployment'
generated using Kedro 0.19.11.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
import pandas as pd
import joblib
from unittest.mock import MagicMock
from src.tp_audiogram_gb.pipelines.model_deployment.nodes import (
    load_model,
    predict,
    deploy_model,
)

def test_load_model(mocker):
    # Mock joblib.load
    mock_model = MagicMock()
    mocker.patch("joblib.load", return_value=mock_model)

    model_path = "test_model.pkl"
    model = load_model(model_path)

    joblib.load.assert_called_once_with(model_path)
    assert model == mock_model, "Loaded model does not match the mocked model"

def test_predict():
    # Mock model
    mock_model = MagicMock()
    mock_model.predict.return_value = [0.5, 0.7, 0.9]

    # Create test data
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})

    predictions = predict(mock_model, data)

    mock_model.predict.assert_called_once_with(data)
    assert isinstance(predictions, pd.DataFrame), "Predictions are not returned as a DataFrame"
    assert list(predictions.columns) == ["predictions"], "Prediction DataFrame does not have the correct column name"
    assert predictions["predictions"].tolist() == [0.5, 0.7, 0.9], "Predictions do not match expected values"

def test_deploy_model(mocker):
    # Mock load_model and predict
    mock_model = MagicMock()
    mocker.patch("src.tp_audiogram_gb.pipelines.model_deployment.nodes.load_model", return_value=mock_model)
    mocker.patch("src.tp_audiogram_gb.pipelines.model_deployment.nodes.predict", return_value=pd.DataFrame({"predictions": [0.5, 0.7, 0.9]}))

    model_path = "test_model.pkl"
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})

    predictions = deploy_model(model_path, data)

    load_model.assert_called_once_with(model_path)
    predict.assert_called_once_with(mock_model, data)
    assert isinstance(predictions, pd.DataFrame), "Predictions are not returned as a DataFrame"
    assert list(predictions.columns) == ["predictions"], "Prediction DataFrame does not have the correct column name"
    assert predictions["predictions"].tolist() == [0.5, 0.7, 0.9], "Predictions do not match expected values"
