"""
This is a boilerplate pipeline 'model_deployment'
generated using Kedro 0.19.11
"""
import pandas as pd
import joblib

def load_model(model_path: str):
  """Load a pre-trained model from a file."""
  model = joblib.load(model_path)
  return model

def predict(model, data: pd.DataFrame) -> pd.DataFrame:
  """Make predictions using the loaded model and input data."""
  predictions = model.predict(data)
  return pd.DataFrame(predictions, columns=["predictions"])

def deploy_model(model_path: str, data: pd.DataFrame) -> pd.DataFrame:
  """Load the model and make predictions on the input data."""
  model = load_model(model_path)
  predictions = predict(model, data)
  return predictions

def node_master_model_deployment(trained_model: object, evaluation_metrics: object) -> pd.DataFrame:
    """
    Fonction principale du pipeline `feature_engineering`.
    """
    df = load_model(trained_model)
    df = deploy_model(df)
    return df