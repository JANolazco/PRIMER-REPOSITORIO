# Usar la imagen oficial de Python como base
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requisitos e instalarlos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar todo el contenido del proyecto al directorio de trabajo
COPY . .

# Exponer el puerto que usará Django
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
