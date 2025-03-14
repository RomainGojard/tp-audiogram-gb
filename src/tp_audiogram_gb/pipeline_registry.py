"""Project pipelines."""

from kedro.pipeline import Pipeline, pipeline
from tp_audiogram_gb.pipelines import data_processing, feature_engineering, model_training, model_evaluation, model_deployment

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": pipeline([
            data_processing.create_pipeline(),
            feature_engineering.create_pipeline(),
            model_training.create_pipeline(),
            model_evaluation.create_pipeline(),
            model_deployment.create_pipeline()
        ])
    }
