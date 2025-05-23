"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import node_master_model_training

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=node_master_model_training,
            inputs="tonal_exams_clean",
            outputs=["trained_model", "X_test", "y_test", "X_min", "X_max","y_min", "y_max"],
            name="node_master_model_training"
        )
    ])
