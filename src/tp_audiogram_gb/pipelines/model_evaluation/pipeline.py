"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs=["trained_model", "X_test", "y_test"],
            outputs="evaluation_metrics",
            name="node_master"
        )
    ])
