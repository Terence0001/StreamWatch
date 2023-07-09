# Utiliser l'image Python officielle en tant qu'image de base
FROM python:3.11

# Exposer le port 8501 pour accéder à l'application Streamlit
EXPOSE 8501

# Créer le répertoire de travail dans l'image
WORKDIR /app

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installer les dépendances Python spécifiées dans requirements.txt
RUN pip install -r requirements.txt

# Copier tous les fichiers de l'application dans l'image
COPY . .

# Commande d'exécution par défaut pour lancer l'application Streamlit
CMD ["streamlit", "run", "picture_pred.py"]
