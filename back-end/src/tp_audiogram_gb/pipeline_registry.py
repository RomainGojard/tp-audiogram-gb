"""Project pipelines."""

from kedro.pipeline import Pipeline, pipeline
from tp_audiogram_gb.pipelines import (
    data_generation,
    data_processing,
    model_training,
    model_evaluation,
    predict  # Importer la pipeline predict
)

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": pipeline([
            data_generation.create_pipeline(),
            data_processing.create_pipeline(),
            model_training.create_pipeline(),
            model_evaluation.create_pipeline(),
        ]),
        "predict": predict.create_pipeline(),  # Ajouter la pipeline predict séparément
        "train_model": pipeline([
            model_training.create_pipeline(),
            model_evaluation.create_pipeline()
        ]),
    }
