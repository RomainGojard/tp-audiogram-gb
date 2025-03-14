from kedro.pipeline import Pipeline, node
from .nodes import clean_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=clean_data,
            inputs="tonal_exams",
            outputs="tonal_exams_clean",
            name="clean_data"
        )
    ])
