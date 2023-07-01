import ultralytics
from ultralytics import YOLO

import wandb
wandb.login(key=)

# os.system('yolo pose train data="stylecoco.yaml" model=yolov8n.yaml pretrained=yolov8n.pt epochs=120 imgsz=640 project=Hands-fracture-YOLOv8 name=V8n-80-hq')


# Load the model
model = YOLO('yolov8l-pose.pt') # load pretrained model 

# Train the model
model.train(data='stylecoco.yaml', epochs=50,imgsz=640, save=True, plots=True)




# # Validate the model
# metrics = model.val()  # no arguments needed, dataset and settings remembered
# # Open a file with writing mode
# with open('metrics.txt', 'w') as file:
#     # Write box.map, map50, map75 to file
#     file.write(f'Box.map: {metrics.box.map}\n')
#     file.write(f'Box.map50: {metrics.box.map50}\n')
#     file.write(f'Box.map75: {metrics.box.map75}\n')
#     # Write each value of box.maps to file
#     for i, val in enumerate(metrics.box.maps, start=50):
#         file.write(f'Box.map{i}: {val}\n')
