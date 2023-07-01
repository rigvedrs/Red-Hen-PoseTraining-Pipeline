import json
import os
import requests
from tqdm import tqdm
import argparse

# Parsing arguments
parser = argparse.ArgumentParser()

parser.add_argument('--json_dir', type=str, default='coco/', help='File path to JSON directory')
parser.add_argument('--output_dir', type=str, default='../Data/coco_data/', help='File path to output directory')
parser.add_argument('--skip_train', type=bool, default=False, help'If you want to skip downloading the train images')

args = parser.parse_args()

# Path to the JSON annotation files
json_loc = args.json_dir
train_json_file = json_loc + 'train.json'
val_json_file = json_loc + 'val.json'
test_json_file = json_loc + 'test.json'

# Directory to save the downloaded images
output_loc = args.output_dir
train_output_dir = output_loc + 'train/'
val_output_dir = output_loc + 'val/'
test_output_dir = output_loc + 'test/'

# Load the train dataset from the JSON file
with open(train_json_file, 'r') as f:
    train_data = json.load(f)

# Load the val dataset from the JSON file
with open(val_json_file, 'r') as f:
    val_data = json.load(f)

# Load the test dataset from the JSON file
with open(test_json_file, 'r') as f:
    test_data = json.load(f)

# Get the list of images from train dataset
train_images = train_data['images']

# Get the list of images from val dataset
val_images = val_data['images']

# Get the list of images from test dataset
test_images = test_data['images']

# Create the output directories if they don't exist
os.makedirs(train_output_dir, exist_ok=True)
os.makedirs(val_output_dir, exist_ok=True)
os.makedirs(test_output_dir, exist_ok=True)

# Download the images from train dataset with a progress bar
if args.skip_train:
    print('Skipping train images')
else:
    print("Downloading train images:")
    with tqdm(total=len(train_images), ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        for image_info in train_images:
            image_url = image_info['coco_url']
            image_id = image_info['id']
            file_name = f"{train_output_dir}/{str(image_id).zfill(12)}.jpg"

            # Send a request to download the image
            response = requests.get(image_url)

            # Save the image to the specified file path
            with open(file_name, 'wb') as file:
                file.write(response.content)

            pbar.update(1)

# Download the images from val dataset with a progress bar
print("Downloading val images:")
with tqdm(total=len(val_images), ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
    for image_info in val_images:
        image_url = image_info['coco_url']
        image_id = image_info['id']
        file_name = f"{val_output_dir}/{str(image_id).zfill(12)}.jpg"

        # Send a request to download the image
        response = requests.get(image_url)

        # Save the image to the specified file path
        with open(file_name, 'wb') as file:
            file.write(response.content)

        pbar.update(1)

# Download the images from test dataset with a progress bar
print("Downloading test images:")
with tqdm(total=len(test_images), ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
    for image_info in test_images:
        image_url = image_info['coco_url']
        image_id = image_info['id']
        file_name = f"{test_output_dir}/{str(image_id).zfill(12)}.jpg"

        # Send a request to download the image
        response = requests.get(image_url)

        # Save the image to the specified file path
        with open(file_name, 'wb') as file:
            file.write(response.content)

        pbar.update(1)

print('Train, Val, and Test images downloaded.')
