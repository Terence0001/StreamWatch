import streamlit as st
from ultralytics import YOLO

# Set the title and subheader of the application
st.title("Détection d'intrusion")
st.subheader('Activer votre webcam, pour commencer')

# Create a button to start the webcam and detection
if st.button('Commencer'):
    # Load the YOLO model
    model = YOLO('./yolov8n.pt')

    # Initialize the camera input widget in Streamlit
    camera_input = st.camera_input("Détection en cours")
    
    # Check if the camera input widget is receiving frames
    if camera_input:
        # Run YOLO model inference on the video stream
        results = model.track(source=camera_input, show=True, stream=True)
        print(results)
        # Loop through the results
        for result in results:
            # Visualize the results on the frame
            annotated_frame = result.plot()
            

            # Display the annotated frame in Streamlit
            st.image(annotated_frame, caption="Détection en cours", use_column_width=True)

    
# if picture:
#     st.image(picture)

# model = YOLO('./yolov8n.pt')
# results = model.predict(source="0", show=True, stream=True)
# for r in results:
#     boxes = r.boxes  # Boxes object for bbox outputs
#     masks = r.masks  # Masks object for segment masks outputs
#     probs = r.probs  # Class probabilities for classification outputs
# print(results)

