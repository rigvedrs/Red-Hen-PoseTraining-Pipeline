import ultralytics
from ultralytics import YOLO
# import wandb
import os

# wandb.login(key=)

# os.system('yolo pose train data="stylecoco.yaml" model=yolov8n.yaml pretrained=yolov8n.pt epochs=120 imgsz=640 project=Hands-fracture-YOLOv8 name=V8n-80-hq')

# Load a model
model = YOLO('yolov8l-pose.pt') # load a pretrained model 

# Train the model
model.train(data='stylecoco.yaml', epochs=50,imgsz=640)

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category