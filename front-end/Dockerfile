# Étape 1 : Construire l'application
FROM node:18 AS builder
WORKDIR /app

# Installer pnpm globalement
RUN npm install -g pnpm

# Copier les fichiers nécessaires pour l'installation des dépendances
COPY package.json ./

# Installer les dépendances
RUN pnpm install

# Copier le reste des fichiers du projet
COPY . .

# Construire l'application
RUN pnpm build

# Étape 2 : Servir l'application avec Next.js
FROM node:18 AS runner
WORKDIR /app

# Installer pnpm globalement dans l'étape runner
RUN npm install -g pnpm

# Copier les fichiers construits depuis l'étape précédente
COPY --from=builder /app ./

# Exposer le port 8080
EXPOSE 8080

# Lancer l'application en production
CMD ["pnpm", "start"]