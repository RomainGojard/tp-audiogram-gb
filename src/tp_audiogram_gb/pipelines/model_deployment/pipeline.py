"""
This is a boilerplate pipeline 'model_deployment'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import node_master_model_deployment

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=node_master_model_deployment,
            inputs="trained_model",
            outputs="",
            name="node_master_model_deployment"
        )
    ])