# --- Frontend Dockerfile ---

FROM node:20-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Nur package.json & lockfile zuerst kopieren (bessere Cache-Nutzung)
COPY package.json package-lock.json* ./

# Dependencies installieren
RUN npm install

# Jetzt den Rest vom Code kopieren
COPY . .

# Port freigeben (für Vite Dev Server)
EXPOSE 5173

# Standardkommando: Dev Server starten
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
