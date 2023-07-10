FROM python:3.10
EXPOSE 8501
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Lance l'application Streamlit
ENTRYPOINT ["/app/.venv/Scripts/streamlit.cmd", "run"]
CMD ["picture_pred.py"]