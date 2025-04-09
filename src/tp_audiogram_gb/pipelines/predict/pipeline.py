"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import predict_user_inputs

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=predict_user_inputs,
            inputs=["user_inputs", "trained_model", "X_min", "X_max", "y_min", "y_max"],
            outputs="user_predictions",
            name="predict_node"
        )
    ])
