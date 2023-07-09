from python:3.11
expose 8501
cmd mkdir -p /app
WORKDIR /app
copy requirements.txt ./requirements.txt
run pip install -r requirements.txt
copy . .
ENTRYPOINT ["streamlit", "run"]
CMD ["picture_pred.py"]