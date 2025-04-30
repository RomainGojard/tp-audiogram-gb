# Utiliser une image Node.js officielle
FROM node:18

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers package.json et pnpm-lock.yaml pour installer les dépendances
COPY package*.json ./

# Installer pnpm et les dépendances du projet
RUN npm install -g pnpm && pnpm install

# Copier tout le code source dans le conteneur
COPY . .

# Construire l'application Next.js
RUN pnpm build

# Exposer le port utilisé par Next.js
EXPOSE 3000

# Démarrer le serveur Next.js
CMD ["pnpm", "start"]