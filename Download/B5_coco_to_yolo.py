from ultralytics.yolo.data.converter import convert_coco
import subprocess

# Convert coco to yolo
convert_coco(labels_dir='coco/', use_keypoints=True)

# Move to Data dir
command = 'mv ./yolo_labels ../Data'
subprocess.run(command, shell=True)

print('Labels saved')