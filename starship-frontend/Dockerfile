# Etapa de construcción
FROM node:18-alpine AS builder
WORKDIR /my-space

# Copiar archivos de configuración de npm y ejecutar npm install
COPY package.json package-lock.json ./
RUN npm ci

# Copiar todo el código fuente y construir la aplicación
COPY . .
RUN npm run build

# Etapa de ejecución
FROM node:18-alpine AS runner
WORKDIR /my-space

# Copiar archivos necesarios desde la etapa de construcción
COPY --from=builder /my-space/package.json ./
COPY --from=builder /my-space/package-lock.json ./
COPY --from=builder /my-space/next.config.mjs ./
COPY --from=builder /my-space/public ./public
COPY --from=builder /my-space/.next/standalone ./
COPY --from=builder /my-space/.next/static ./.next/static

# Exponer el puerto que usará la aplicación
EXPOSE 3000

# Comando de inicio
CMD ["node", "server.js"]
