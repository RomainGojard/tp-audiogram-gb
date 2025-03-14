import pandas as pd

def compute_variation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule la variation de l'audition avant et après l'examen pour chaque fréquence.
    """
    df = df.copy()
    freqs = ["125_Hz", "250_Hz", "500_Hz", "1000_Hz", "2000_Hz", "4000_Hz", "8000_Hz"]
    
    for freq in freqs:
        df[f"variation_{freq}"] = df[f"after_exam_{freq}"] - df[f"before_exam_{freq}"]
    
    print(f"✅ Variations calculées pour {len(freqs)} fréquences")
    return df

def add_global_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajoute des statistiques globales sur la variation auditive.
    """
    df = df.copy()
    variation_cols = [col for col in df.columns if "variation" in col]
    
    df["mean_variation"] = df[variation_cols].mean(axis=1)
    df["std_variation"] = df[variation_cols].std(axis=1)
    
    print(f"✅ Statistiques globales ajoutées")
    return df

def node_master_feature_engineering(tonal_exams_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Fonction principale du pipeline `feature_engineering`.
    """

    df = compute_variation(tonal_exams_clean)
    df = add_global_stats(df)
    return df
