import subprocess
import requests

def download_file(url, file_name):
    print(f"Downloading {file_name}...")
    response = requests.get(url, stream=True)
    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Download of {file_name} completed")

# Clone pytorch-AdaIN repository
subprocess.run(["git", "clone", "https://github.com/rigvedrs/pytorch-AdaIN.git"])

# Move files and directories from pytorch-AdaIN
subprocess.run(["mv", "pytorch-AdaIN/{.*,*}", "./"])
subprocess.run(["rm", "-rf", "pytorch-AdaIN/"])

# Create 'models' directory
subprocess.run(["mkdir", "models/"])

# Download decoder.pth
download_file("https://docs.google.com/uc?export=download&id=1bMfhMMwPeXnYSQI6cDWElSZxOxc6aVyr", "models/decoder.pth")

# Download vgg_normalised.pth
download_file("https://drive.google.com/uc?id=1EpkBA2K2eYILDSyPTt0fztz59UjAIpZU", "models/vgg_normalised.pth")

print("Download completed successfully.")

# Apply style using applystyle.py script
subprocess.run(["python3", "applystyle.py", "--content_dir", "../Data/coco_data/train/", "--style_dir", "Data/style_data/", "--output", "../Data/datasets/train/images/"])
subprocess.run(["python3", "applystyle.py", "--content_dir", "../Data/coco_data/test/", "--style_dir", "Data/style_data/", "--output", "../Data/datasets/test/images/"])
subprocess.run(["python3", "applystyle.py", "--content_dir", "../Data/coco_data/val/", "--style_dir", "Data/style_data/", "--output", "../Data/datasets/val/images/"])
