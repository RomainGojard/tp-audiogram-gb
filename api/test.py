import requests
import json
from kedro.framework.context import KedroContext
from kedro.framework.startup import bootstrap_project

def test_api():
    # Initialiser Kedro avec le chemin du projet
    project_path = "/Users/romaingojard/Desktop/M2_ESGI/Industrialisation_ML/TP_industrialisation_ML_GB/tp-audiogram-gb"
    bootstrap_project(project_path)

    # URL de l'API
    url = "http://127.0.0.1:5002/predict"

    # Données d'entrée pour le test
    payload = {
        "before_exam_125_Hz": 21,
        "before_exam_250_Hz": 24,
        "before_exam_500_Hz": 25,
        "before_exam_1000_Hz": 35,
        "before_exam_2000_Hz": 63,
        "before_exam_4000_Hz": 74,
        "before_exam_8000_Hz": 66
    }

    # En-têtes HTTP
    headers = {
        "Content-Type": "application/json"
    }

    # Envoyer une requête POST
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Vérifier le statut de la réponse
    if response.status_code == 200:
        print("✅ Requête réussie !")
        print("Réponse de l'API :")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"❌ Erreur : {response.status_code}")
        print("Détails :", response.text)

if __name__ == "__main__":
    test_api()
