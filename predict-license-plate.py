"""
This script demonstrates how to use a pretrained YOLOv8 model for inference on a video file.
The script leverages the Ultralytics YOLO library to:
1. Load a pretrained YOLO model.
2. Perform predictions (inference) on a specified video.
3. Save the prediction results to the output directory.

Dependencies:
- ultralytics library
- A trained YOLO model file (e.g., `best.pt`).
- A test video file for inference

"""

from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('./runs/detect/train/weights/best.pt')

# Run inference
model.predict('./resources/car.mp4', save=True, imgsz=320, conf=0.2)
