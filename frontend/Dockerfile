FROM node:20-slim

WORKDIR /app

COPY package*.json ./

# optional: kleine Tools für Builds (sonst gibt's oft Probleme mit npm in slim)
RUN apt-get update && apt-get install -y python3 make g++ && rm -rf /var/lib/apt/lists/*

# 👇 hier installieren wir Rollup und das ARM-Binary direkt
RUN npm install --legacy-peer-deps && \
    npm install --save-dev rollup @rollup/rollup-linux-arm64-gnu

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
