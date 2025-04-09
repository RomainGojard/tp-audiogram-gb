# app.py
from flask import Flask, request, jsonify
from kedro.framework.startup import bootstrap_project
import pandas as pd
import json
from pathlib import Path
from kedro.framework.session import KedroSession
from save_from_post_request import save_from_post_request
from kedro.framework.startup import bootstrap_project

app = Flask(__name__)
#project_path = "/Users/romaingojard/Desktop/M2_ESGI/Industrialisation_ML/TP_industrialisation_ML_GB/tp-audiogram-gb/"
bootstrap_project(Path.cwd())

# Define Flask route for POST requests
@app.route("/predict", methods=["POST"])
def predict():
    """
    Route REST pour prédire les résultats à partir des données utilisateur.
    Les données sont sauvegardées avec un identifiant unique.
    """

    # Définir le chemin pour sauvegarder les données utilisateur
    filepath = "data/05_model_input/user_inputs.json"

    # Sauvegarder les données utilisateur
    user_id = save_from_post_request(request, filepath)

    # Exécuter le pipeline Kedro
    with KedroSession.create(project_path=".") as session:
        session.run(pipeline_name="predict")

    # Charger le json générés par le pipeline
    # Le chemin doit être relatif au répertoire racine du projet
    output_path = "data/08_predictions/user_predictions.json"
    with open(output_path, "r") as file:
        output = json.load(file)

    # Retourner les résultats avec l'ID utilisateur
    response = {
        "user_id": user_id,
        "results": output
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True) #passer à false le mode debug à la fin des devs