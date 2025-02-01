# Usa una imagen base de Python
FROM python:3.9-slim

# Instala los paquetes necesarios para psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos (si tienes uno)
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . /app/

# Define la variable de entorno para que Flask ejecute el archivo run.py
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Expón el puerto en el que Flask se ejecutará (por defecto es el 5000)
EXPOSE 5000

# Comando para ejecutar la aplicación directamente con Python
CMD ["python", "run.py"]

