from kedro.pipeline import Pipeline, node
from .nodes import node_master_feature_engineering

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=node_master_feature_engineering,
            inputs="tonal_exams_clean",
            outputs="tonal_exams_features",
            name="node_master_feature_engineering"
        )
    ])
