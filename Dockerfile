FROM python:3.9
EXPOSE 8501
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN python -m venv .venv
COPY .venv ./.venv
SHELL ["cmd", "/S", "/C", "CALL", ".venv\\Scripts\\activate.bat && pip install -r requirements.txt"]
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD ["picture_pred.py"]
