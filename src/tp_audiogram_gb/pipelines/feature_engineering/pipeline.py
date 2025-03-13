from kedro.pipeline import Pipeline, node
from .nodes import node_master

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=node_master,
            inputs="tonal_exams_clean",
            outputs="tonal_exams_features",
            name="node_master"
        )
    ])
