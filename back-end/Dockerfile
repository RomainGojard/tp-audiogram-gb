FROM python:3.13.2

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean

# Installer les dépendances Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du projet
COPY . .

# Exposer le port de l'API Flask
#EXPOSE 5002

# Commande pour démarrer l'API Flask
CMD ["python", "app.py"]