import pandas as pd
import numpy as np
import random


def generate_audiograms(csv_filename: str, exam_count: int = 10000, init_freq: int = 125) -> None:
    """
    Génère des audiogrammes avec des profils d'amélioration et les sauvegarde dans un fichier CSV.
    """
    frequencies = [init_freq * (2 ** i) for i in range(7)]
    headers = [f"exam_{freq}_Hz" for freq in frequencies]
    headers_before = ["before_" + header for header in headers]
    headers_after = ["after_" + header for header in headers]
    columns = headers_before + headers_after

    data = []

    for _ in range(exam_count):
        profile = random.choice(['normal', 'mild', 'moderate', 'severe', 'profound', 'slope', 'reverse'])
        thresholds = generate_thresholds_by_profile(profile, frequencies)
        improvements = calculate_improvements(profile, thresholds)

        # Ajouter des valeurs aberrantes aléatoires
        if random.random() < 0.1:  # 10% de chance par audiogramme
            outlier_position = random.randint(0, len(thresholds) - 1)
            if random.random() < 0.5:
                thresholds[outlier_position] = random.randint(120, 150)  # Perte très élevée
            else:
                thresholds[outlier_position] = random.randint(-10, 0)  # Audition exceptionnellement bonne

        data.append(thresholds + improvements)

    df = pd.DataFrame(data, columns=columns)
    return df


def generate_thresholds_by_profile(profile, frequencies):
    if profile == 'normal':
        return [random.randint(-10, 20) for _ in frequencies]
    elif profile == 'mild':
        return [random.randint(20, 40) for _ in frequencies]
    elif profile == 'moderate':
        return [random.randint(40, 60) for _ in frequencies]
    elif profile == 'severe':
        return [random.randint(60, 80) for _ in frequencies]
    elif profile == 'profound':
        return [random.randint(80, 120) for _ in frequencies]
    elif profile == 'slope':
        return [random.randint(0, 25) + i * 10 for i, _ in enumerate(frequencies)]
    elif profile == 'reverse':
        return [random.randint(70, 90) - i * 5 for i, _ in enumerate(frequencies)]
    else:
        return [random.randint(0, 100) for _ in frequencies]


def calculate_improvements(profile, thresholds):
    if profile in ['normal', 'mild']:
        return np.clip(thresholds - np.random.randint(15, 30, size=len(thresholds)), 0, 120).tolist()
    elif profile in ['moderate', 'severe', 'profound']:
        return np.clip(thresholds - np.random.randint(5, 15, size=len(thresholds)), 0, 120).tolist()
    elif profile == 'slope':
        return np.clip(thresholds - np.random.randint(10, 20, size=len(thresholds)), 0, 120).tolist()
    elif profile == 'reverse':
        return np.clip(thresholds - np.random.randint(0, 10, size=len(thresholds)), 0, 120).tolist()
    else:
        return thresholds  # Pas d'amélioration par défaut
    
def node_master_data_generation(csv_filename: str = "data/01_raw/tonal_exams.csv") -> str:
    """
    Fonction principale du pipeline `data_generation`.
    """
    df = generate_audiograms(csv_filename)
    return df