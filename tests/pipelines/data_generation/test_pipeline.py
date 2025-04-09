"""
This is a boilerplate test file for pipeline 'data_generation'
generated using Kedro 0.19.11.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
import pandas as pd
import numpy as np
from src.tp_audiogram_gb.pipelines.data_generation.nodes import (
    generate_audiograms,
    generate_thresholds_by_profile,
    calculate_improvements,
)

def test_generate_thresholds_by_profile():
    frequencies = [125, 250, 500, 1000, 2000, 4000, 8000]
    profiles = ['normal', 'mild', 'moderate', 'severe', 'profound', 'slope', 'reverse']

    for profile in profiles:
        thresholds = generate_thresholds_by_profile(profile, frequencies)
        assert len(thresholds) == len(frequencies), f"Thresholds length mismatch for profile {profile}"
        assert all(isinstance(t, int) for t in thresholds), f"Thresholds are not integers for profile {profile}"

def test_calculate_improvements():
    thresholds = [50, 60, 70, 80, 90, 100, 110]
    profiles = ['normal', 'mild', 'moderate', 'severe', 'profound', 'slope', 'reverse']

    for profile in profiles:
        improvements = calculate_improvements(profile, thresholds)
        assert len(improvements) == len(thresholds), f"Improvements length mismatch for profile {profile}"
        assert all(0 <= i <= 120 for i in improvements), f"Improvements out of range for profile {profile}"

def test_generate_audiograms():
    csv_filename = "test_audiograms.csv"
    exam_count = 100
    init_freq = 125

    df = generate_audiograms(csv_filename, exam_count, init_freq)
    assert isinstance(df, pd.DataFrame), "Generated data is not a DataFrame"
    assert len(df) == exam_count, "Generated DataFrame row count mismatch"
    assert all(col.startswith("before_exam") or col.startswith("after_exam") for col in df.columns), "Column names mismatch"

    # Check for valid data ranges
    before_cols = [col for col in df.columns if col.startswith("before_exam")]
    after_cols = [col for col in df.columns if col.startswith("after_exam")]

    assert not df[before_cols].isnull().values.any(), "Null values found in 'before_exam' columns"
    assert not df[after_cols].isnull().values.any(), "Null values found in 'after_exam' columns"

def test_outliers_in_generate_audiograms():
    csv_filename = "test_audiograms.csv"
    exam_count = 1000
    init_freq = 125

    df = generate_audiograms(csv_filename, exam_count, init_freq)
    before_cols = [col for col in df.columns if col.startswith("before_exam")]

    # Check for outliers
    outliers = df[before_cols].applymap(lambda x: x < 0 or x > 120).sum().sum()
    assert outliers > 0, "No outliers detected, but they should exist"
