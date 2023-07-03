from ultralytics import YOLO

# load model
model = YOLO(MODEL_PATH)
model.fuse()

# predict
detections = model(frame)
