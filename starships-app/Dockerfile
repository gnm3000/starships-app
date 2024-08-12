FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["chalice", "local", "--port", "8000", "--host", "0.0.0.0", "--no-autoreload"]
