# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto que usará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "bff_app:app", "--host", "0.0.0.0", "--port", "5000"]
