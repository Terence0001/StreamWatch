FROM python:3.9
EXPOSE 8501
RUN mkdir -p /app
# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Lance l'application Streamlit
ENTRYPOINT ["streamlit", "run"]
CMD ["picture_pred.py"]