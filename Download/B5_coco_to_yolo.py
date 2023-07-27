import os
from ultralytics.yolo.data.converter import convert_coco

# Convert coco to yolo                                                                                                                                                                                            
convert_coco(labels_dir='coco/', use_keypoints=True)

# Create train, val, and test directories                                                                                                                                                                         
os.makedirs('../Data/dataset/labels/train/', exist_ok=True)
os.makedirs('../Data/dataset/labels/val/', exist_ok=True)
os.makedirs('../Data/dataset/labels/test/', exist_ok=True)

os.makedirs('../Data/dataset/images/train/', exist_ok=True)
os.makedirs('../Data/dataset/images/val/', exist_ok=True)
os.makedirs('../Data/dataset/images/test/', exist_ok=True)

# Move labels to respective directories                                                                                                                                                                           
os.system('find yolo_labels/labels/train/ -type f -exec mv -t ../Data/dataset/labels/train/ {} +')
os.system('mv ./yolo_labels/labels/test/* ../Data/dataset/labels/test/')
os.system('mv ./yolo_labels/labels/val/* ../Data/dataset/labels/val/')
print('Labels saved')
