"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.11
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_data(data: pd.DataFrame):
    X = data.drop('target', axis=1)
    y = data['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def node_master(data: pd.DataFrame) -> None:
    """
    Fonction principale du pipeline `model_training`.
    """
    X_train, X_test, y_train, y_test = load_data(data)
    model = train_model(X_train, y_train)
    return model
