import streamlit as st
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

# Titre de l'application
st.title("Détection d'intrusion")
st.subheader('Activer votre webcam, pour commencer')

if st.button('Commencer'):
    # Création du modèle YOLO
    model = YOLO('./yolov8n.pt')
    
    # Détection et affichage des résultats
    results = st.camera_input("Détection en cours")
    while st.camera_input:
        model(results, source="0", stream=True)

    
# if picture:
#     st.image(picture)

# model = YOLO('./yolov8n.pt')
# results = model.predict(source="0", show=True, stream=True)
# for r in results:
#     boxes = r.boxes  # Boxes object for bbox outputs
#     masks = r.masks  # Masks object for segment masks outputs
#     probs = r.probs  # Class probabilities for classification outputs
# print(results)

