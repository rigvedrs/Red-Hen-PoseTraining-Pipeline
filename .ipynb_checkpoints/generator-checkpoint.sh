#!/bin/bash

# Running all the code blocks for downloading the dataset and applying Style Transfer

echo '*********************************************************************************'

cd Download/

echo 'Running Download Blocks'

python3 B1_Style_download.py

python3 B2_download_coco.py

python3 B3_coco_filter.py

python3 B4_download_coco_imgs.py

python3 B5_coco_to_yolo.py

echo '*********************************************************************************'

cd ../Style

echo 'Running Style Transfer Block'

python3 B6_download_and_apply_adain.py

echo '*********************************************************************************'

echo 'Dataset Succesfully prepared'
