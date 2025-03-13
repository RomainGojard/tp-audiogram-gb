Voici les principales étapes du pipeline à adopter :

1. **Extraction et préparation des données**
    - **Objectif** : Collecter et nettoyer les données des audiogrammes
    - **Pourquoi ?** : Les données doivent être prétraitées pour éliminer le bruit, gérer les valeurs manquantes et standardiser les fréquences sonores
    - **Tâches** :
      - Extraction des audiogrammes sous forme de paires (fréquence, dB)
      - Nettoyage des données (valeurs manquantes, erreurs)
      - Normalisation des valeurs dB pour une meilleure convergence du modèle
    - **Dans Kedro** :
      - étape de data_processing
      - un node pour chacune des tâches
      - et catalog.yml : Définition des sources de données (CSV, base de données, API, etc.)

2. **Sélection des caractéristiques**
    - **Objectif** : Identifier les variables les plus pertinentes pour la prédiction des valeurs futures.
    - **Pourquoi ?** : Toutes les fréquences n’ont pas nécessairement la même importance, et il peut être utile de réduire la dimensionnalité.
    - **Tâches** :
      - Analyse des corrélations entre fréquences
      - Transformation des données si nécessaire (ex: PCA, encodage)
    - **Dans Kedro** :
      - étape de feature_engineering
      - avec les nodes : 
        - Calcul des corrélations entre fréquences audiométriques
        - Réduction de dimensions si nécessaire (PCA, autoencoders)
        - Transformation des données pour améliorer la prédiction si nécéssaire

3. **Entraînement du modèle**
    - **Objectif** : Développer un modèle de prédiction pour estimer les futurs gains prothétiques.
    - **Pourquoi ?** : L'objectif est d’avoir un modèle capable de généraliser les prédictions des valeurs futures de l’audiogramme.
    - **Tâches** :
      - Sélection d’un modèle de séries temporelles (ex : LSTM, Prophet, ARIMA).
      - Ajustement des hyperparamètres.
      - Validation croisée pour éviter le surapprentissage.
    - **Dans Kedro** :
      - étape de model_training
      - avec les nodes : 
        - Séparation des données en train/test
        - Entraînement d’un modèle (LSTM, ARIMA, Prophet, etc.)
        - Ajustement des hyperparamètres
      - parameters.yml : Stockage des paramètres de modèle (ex: learning rate, nombre de couches)

4. **Évaluation des performances**
    - **Objectif** : Vérifier la qualité du modèle avant son déploiement.
    - **Pourquoi ?** : Un modèle mal évalué peut générer des prédictions erronées ayant un impact médical.
    - **Tâches** :
      - Utilisation de métriques comme RMSE, MAE ou R².
      - Comparaison avec un modèle de base (ex : moyenne mobile).
      - Test du modèle sur des données non vues.
    - **Dans Kedro** :
      - étape de model_evaluation
      - avec les nodes : 
        - Prédictions sur les données de test
        - Comparaison des performances avec des métriques comme RMSE, MAE
        - Analyse des erreurs et validation croisée

5. **Déploiement du modèle**
    - **Objectif** : Intégrer le modèle dans un outil utilisable par les audioprothésistes.
    - **Pourquoi ?** : Une fois validé, le modèle doit être accessible pour fournir des prédictions en temps réel.
    - **Tâches** :
      - Conteneurisation du modèle (ex : Docker).
      - Mise en place d’une API pour l’interaction avec les audioprothésistes.
      - Monitoring et mises à jour régulières.
    - **Dans Kedro** :
      - étape de model_deployment
      - avec les nodes : 
        - Sérialisation du modèle (ex: pickle, joblib)
        - Déploiement sous forme d’API (FastAPI, Flask)
        - Monitoring des performances en production
      - catalog.yml : Définition de l’emplacement de stockage du modèle (local, cloud)

**Pourquoi ces pipelines ?**
- **Fiabilité** : Assurer des prédictions précises pour éviter des erreurs dans l’adaptation des prothèses auditives.
- **Automatisation** : Réduire le temps nécessaire à l’analyse des audiogrammes.
- **Traçabilité** : Suivre et comprendre l’impact des ajustements des prothèses auditives.
- **Scalabilité** : Faciliter l’évolution du modèle en intégrant de nouvelles données.
