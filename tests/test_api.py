import pytest
import requests
import json
from kedro.framework.startup import bootstrap_project

BASE_URL = "http://127.0.0.1:5002"

@pytest.fixture
def api_url():
    """Fixture pour définir l'URL de base de l'API."""
    return BASE_URL

def test_run_default(api_url):
    """Test pour la route /run-default."""
    url = f"{api_url}/run-default"
    response = requests.post(url)

    assert response.status_code == 200, f"Statut attendu : 200, obtenu : {response.status_code}"
    data = response.json()
    assert data["status"] == "success", f"Statut attendu : success, obtenu : {data['status']}"
    assert "Pipeline par défaut exécuté avec succès." in data["message"]

def test_train_model(api_url):
    """Test pour la route /train-model."""
    url = f"{api_url}/train-model"
    response = requests.post(url)

    assert response.status_code == 200, f"Statut attendu : 200, obtenu : {response.status_code}"
    data = response.json()
    assert data["status"] == "success", f"Statut attendu : success, obtenu : {data['status']}"
    assert "Pipeline d'entraînement exécuté avec succès." in data["message"]

def test_predict(api_url):
    """
    Test pour la route /predict.
    Envoie une requête POST avec des données utilisateur et vérifie la réponse.
    """
    # URL de l'API
    url = f"{api_url}/predict"

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
    assert response.status_code == 200, f"Statut attendu : 200, obtenu : {response.status_code}"

    # Vérifier le contenu de la réponse
    data = response.json()
    assert "user_id" in data, "La réponse doit contenir un 'user_id'."
    assert "results" in data, "La réponse doit contenir des 'results'."
    assert isinstance(data["results"], list), "Les résultats doivent être une liste."
    assert len(data["results"]) > 0, "Les résultats ne doivent pas être vides."

    # Vérifier les clés des résultats
    expected_keys = [
        "after_exam_before_exam_125_Hz",
        "after_exam_before_exam_250_Hz",
        "after_exam_before_exam_500_Hz",
        "after_exam_before_exam_1000_Hz",
        "after_exam_before_exam_2000_Hz",
        "after_exam_before_exam_4000_Hz",
        "after_exam_before_exam_8000_Hz"
    ]
    for key in expected_keys:
        assert key in data["results"][0], f"Clé manquante dans les résultats : {key}"

    # Afficher la réponse pour le débogage
    print("✅ Requête réussie !")
    print("Réponse de l'API :")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    pytest.main()
