"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""
from sklearn.metrics import accuracy_score

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

def node_master(model, X_test, y_test) -> float:
    """
    Fonction principale du pipeline `model_evaluation`.
    """
    accuracy = evaluate_model(model, X_test, y_test)
    return accuracy