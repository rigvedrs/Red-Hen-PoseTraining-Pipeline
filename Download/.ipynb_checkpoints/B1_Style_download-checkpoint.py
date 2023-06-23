import pandas as pd
import requests
import os
import re
from tqdm import tqdm
import argparse

# Parsing arguments
parser = argparse.ArgumentParser()

parser.add_argument('--csv_loc', type=str, default='B1_final_data.csv', help='File path to the content image')
parser.add_argument('--num', type=int, default=0, help='Number of images to download, 0 for all, and any other number for otherwise')
parser.add_argument('--output_dir', type=str, default='../Data/style_data/', help='File path to output directory')

args = parser.parse_args()

def sanitize(filename: str) -> str:
    # This line replaces any character not a number, letter, or underscore with an underscore
    filename = re.sub('[^a-zA-Z0-9\n\.]', '_', filename)
    return filename


# Read the file 
file_path = args.csv_loc
df = pd.read_csv(file_path)
assert args.num < len(df), f"Number entered is more than length of df ({len(df)})"

output_dir = args.output_dir

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

count = 0

# Download and save the selected images
if args.num == 0:
    for c, row in tqdm(df.iterrows(), total=len(df)):
        count+=1
        image_link = row['IMAGE_LINK']
        # title = sanitize(row['TITLE'])
        # technique = sanitize(row['TECHNIQUE'])
        file_name = f"{output_dir}/img_{count}.jpg"  

        response = requests.get(image_link)

        # Saving Image
        with open(file_name, 'wb') as file:
            file.write(response.content)

else:
    for c, row in tqdm(df.iterrows(), total=args.num):
        count+=1
        if c == args.num:
            break
        image_link = row['IMAGE_LINK']
        # title = sanitize(row['TITLE'])
        # technique = sanitize(row['TECHNIQUE'])
        file_name = f"{output_dir}/img_{count}.jpg"  
        
        response = requests.get(image_link)

        # Saving Image
        with open(file_name, 'wb') as file:
            file.write(response.content)