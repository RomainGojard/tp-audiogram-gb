import json
import uuid
from datetime import datetime

def save_from_post_request(request, filepath):
    """
    Sauvegarde les données d'une requête POST dans un fichier JSON en les identifiant comme données utilisateur.
    """
    # Générer un identifiant unique pour les données
    user_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()

    # Récupérer les données de la requête POST
    data = request.get_json()

    # Ajouter des métadonnées pour identifier les données utilisateur
    data_with_metadata = {
        "user_id": user_id,
        "timestamp": timestamp,
        "data": data
    }

    # Sauvegarder les données dans un fichier JSON

    with open(filepath, "w") as f:
        json.dump(data_with_metadata, f, indent=4)

    print(f"✅ Données utilisateur sauvegardées avec l'ID : {user_id}")
    return user_id