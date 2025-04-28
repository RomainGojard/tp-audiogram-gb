# app.py
from flask import Flask, request, jsonify
from kedro.framework.startup import bootstrap_project
import pandas as pd
import json
from pathlib import Path
from kedro.framework.session import KedroSession
from save_from_post_request import save_from_post_request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
bootstrap_project(Path.cwd())

# Route pour vérifier l'état de l'API
@app.route("/", methods=["GET"])
def index():
    """
    Route REST pour vérifier l'état de l'API.
    """
    return jsonify({"status": "API is running"}), 200

# Route pour exécuter le pipeline Kedro par défaut
@app.route("/run-default", methods=["POST"])
def run_default():
    """
    Route REST pour exécuter le pipeline Kedro par défaut.
    """
    try:
        with KedroSession.create(project_path=".") as session:
            session.run()  # Exécute le pipeline par défaut
        return jsonify({"status": "success", "message": "Pipeline par défaut exécuté avec succès."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route pour exécuter le pipeline d'entraînement du modèle
@app.route("/train-model", methods=["POST"])
def train_model():
    """
    Route REST pour exécuter le pipeline d'entraînement du modèle.
    """
    try:
        with KedroSession.create(project_path=".") as session:
            session.run(pipeline_name="train_model")  # Exécute le pipeline d'entraînement
        return jsonify({"status": "success", "message": "Pipeline d'entraînement exécuté avec succès."}), 200
    except Exception as e:
        print(f"Erreur lors de l'exécution du pipeline d'entraînement : {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Route pour prédire les résultats à partir des données utilisateur
@app.route("/predict", methods=["POST"])
def predict():
    """
    Route REST pour prédire les résultats à partir des données utilisateur.
    Les données sont sauvegardées avec un identifiant unique.
    """
    filepath = "data/05_model_input/user_inputs.json"
    user_id = save_from_post_request(request, filepath)

    try:
        with KedroSession.create(project_path=".") as session:
            session.run(pipeline_name="predict")

        output_path = "data/08_predictions/user_predictions.json"
        with open(output_path, "r") as file:
            output = json.load(file)

        response = {
            "user_id": user_id,
            "results": output
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)  # Passer debug à False en production