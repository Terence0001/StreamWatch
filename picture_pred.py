import cv2, requests
import streamlit as st

st.title("Détection d'intrusion")

if st.button('Prendre une photo'):
    # Capture de l'image à partir de la webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Affichage de l'image capturée
    st.image(frame, channels="BGR")

    # Envoi de l'image à l'API
    url = "https://api.ultralytics.com/v1/predict/gnFZUCbZVXyO44qIywhW"
    headers = {"x-api-key": "ef579f0d3f6e41e931bcd8be9aed359a4436503dce"}
    data = {"size": 640, "confidence": 0.42, "iou": 0.50}

    # Conversion de l'image en bytes
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()

    # Envoi de la requête API avec l'image
    response = requests.post(url, headers=headers, data=data, files={"image": img_bytes})

    # Vérification de la réponse de la requête
    response.raise_for_status()

    # Affichage des résultats de l'inférence
    st.json(response.json())

    # Fermeture de la webcam
    cap.release()
