# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Que valor quieres si el usuario no lo da

ARG APP_USER="default"
ENV APP_USER=$APP_USER

# Copia todo el código al contenedor
COPY . /app

# Define el comando por defecto para ejecutar la aplicación
CMD ["/bin/bash"]