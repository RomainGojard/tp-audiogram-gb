from kedro.pipeline import Pipeline, node, pipeline
from .nodes import node_master_data_generation

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=node_master_data_generation,
            inputs=None,
            outputs="tonal_exams_raw",
            name="node_master_data_generation"
        )
    ])