"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""
from sklearn.metrics import accuracy_score
import mlflow

mlflow.autolog()

def evaluate_model(trained_model, X_test, y_test):
    predictions = trained_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy