import requests

def run_default():
    url = "http://localhost:5002/run-default"  # Remplacez par l'URL de votre API
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print("Réponse de l'API :", response.json())
        else:
            print(f"Erreur {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)

if __name__ == "__main__":
    run_default()