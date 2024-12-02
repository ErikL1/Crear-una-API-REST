# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir flask

# Expone el puerto que usará la aplicación
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
