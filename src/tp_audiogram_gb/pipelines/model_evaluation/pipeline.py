"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.11
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import node_master

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=node_master,
            inputs="tonal_exams_mtrain",
            outputs="tonal_exams_meval",
            name="node_master"
        )
    ])
