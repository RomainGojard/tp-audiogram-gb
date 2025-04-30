FROM node:18

# Installer pnpm globalement
RUN npm install -g pnpm

WORKDIR /app

COPY package*.json ./

RUN pnpm install

COPY . .

EXPOSE 8080

CMD ["pnpm", "dev"]
