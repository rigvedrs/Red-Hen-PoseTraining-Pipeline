import os
from ultralytics.yolo.data.converter import convert_coco

# Convert coco to yolo
convert_coco(labels_dir='coco/', use_keypoints=True)

# Create train, val, and test directories
os.makedirs('../Data/dataset/train/labels/', exist_ok=True)
os.makedirs('../Data/dataset/val/labels/', exist_ok=True)
os.makedirs('../Data/dataset/test/labels/', exist_ok=True)

os.makedirs('../Data/dataset/train/images/', exist_ok=True)
os.makedirs('../Data/dataset/val/images/', exist_ok=True)
os.makedirs('../Data/dataset/test/images/', exist_ok=True)

# Move labels to respective directories
os.system('find yolo_labels/labels/train/ -type f -exec mv -t ../Data/dataset/train/labels/ {} +')
os.system('mv ./yolo_labels/labels/test/* ../Data/dataset/test/labels/')
os.system('mv ./yolo_labels/labels/val/* ../Data/dataset/val/labels/')

print('Labels saved') 