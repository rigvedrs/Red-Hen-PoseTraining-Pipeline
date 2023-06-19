import os
import requests
import zipfile
import glob 
import shutil

def download_file(url, file_name):
    print(f"Downloading {file_name}...")
    response = requests.get(url, stream=True)
    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Download of {file_name} completed")

def download_and_extract(url, zip_file, folder_name):
    download_file(url, zip_file)
    print(f"Extracting {zip_file}...")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(folder_name)
    os.remove(zip_file)
    print(f"Extraction of {zip_file} completed")

os.makedirs("coco", exist_ok=True)
os.chdir("coco")

download_and_extract("http://images.cocodataset.org/annotations/annotations_trainval2017.zip", "annotations_trainval2017.zip", "annotations")

# Move files from annotations/annotations to annotations/
for file_path in glob.glob("annotations/annotations/*"):
    shutil.move(file_path, "annotations")

# Remove annotations/annotations directory
shutil.rmtree("annotations/annotations")

print("All JSON files downloaded successfully.")
