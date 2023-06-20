import os

# Running all the code blocks for downloading the dataset and applying Style Transfer

print('*********************************************************************************')

os.chdir('Download/')

print('Running Download Blocks')

os.system('python3 B1_Style_download.py')

os.system('python3 B2_download_coco.py')

os.system('python3 B3_coco_filter.py')

os.system('python3 B4_download_coco_imgs.py')

os.system('python3 B5_coco_to_yolo.py')

print('*********************************************************************************')

os.chdir('../Style')

print('Running Style Transfer Block')

os.system('python3 B6_download_and_apply_adain.py')

print('*********************************************************************************')

print('Dataset Succesfully prepared')