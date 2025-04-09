import pandas as pd
import pytest
from src.tp_audiogram_gb.pipelines.data_processing.nodes import clean_data

@pytest.fixture
def mock_audiogram_raw():
    # Génère un DataFrame factice avec des données brutes
    data = {
        "before_exam_125_Hz": [10, 20, None, 40, "abc"],
        "before_exam_250_Hz": [15, 25, 35, None, 50],
        "after_exam_125_Hz": [5, 10, 15, 20, 25],
        "after_exam_250_Hz": [None, 30, 40, 50, 60],
        "irrelevant_column": ["irrelevant", "data", "to", "be", "removed"],
    }
    return pd.DataFrame(data)

def test_clean_data(mock_audiogram_raw):
    # Teste la fonction clean_data
    audiogram_raw = mock_audiogram_raw
    cleaned_data = clean_data(audiogram_raw)

    # Vérifie que les colonnes inutiles ont été supprimées
    expected_columns = ["before_exam_125_Hz", "before_exam_250_Hz", "after_exam_125_Hz", "after_exam_250_Hz"]
    assert list(cleaned_data.columns) == expected_columns, "Les colonnes inutiles n'ont pas été supprimées"

    # Vérifie que les lignes contenant des valeurs manquantes ont été supprimées
    assert not cleaned_data.isnull().values.any(), "Les lignes contenant des valeurs manquantes n'ont pas été supprimées"

    # Vérifie que les lignes contenant des lettres ont été supprimées
    assert not cleaned_data.apply(lambda x: x.astype(str).str.contains('[a-zA-Z]').any(), axis=1).any(), "Les lignes contenant des lettres n'ont pas été supprimées"

    # Vérifie que le DataFrame nettoyé a la bonne forme
    assert cleaned_data.shape[0] == 2, f"Le nombre de lignes après nettoyage est incorrect : {cleaned_data.shape[0]}"
    assert cleaned_data.shape[1] == 4, f"Le nombre de colonnes après nettoyage est incorrect : {cleaned_data.shape[1]}"
