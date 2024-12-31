"""
This script demonstrates the process of training a YOLO model using the Ultralytics YOLO library.

Key functionalities:
1. Loading a pretrained YOLO model.
2. Configuring the model for training on a custom dataset.
3. Training the model for a specified number of epochs with multiple GPUs.

Dependencies:
- ultralytics library
- A valid dataset YAML file (e.g., `data.yaml`) specifying paths for training and validation data.

"""

from ultralytics import YOLO

# Load a model
model = YOLO('yolo11m.pt')  # load any pretrained model (recommended for training)

# Train the model
results = model.train(data='config.yaml', epochs=200, imgsz=640)

