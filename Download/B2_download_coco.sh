#!/bin/bash

rmdir coco
mkdir coco
cd coco

download_file() {
    url=$1
    file_name=$2

    echo "Downloading $file_name..."
    wget -c "$url" --progress=bar:force:noscroll -O "$file_name"
    echo "Download of $file_name completed"
}

download_and_extract() {
    url=$1
    zip_file=$2
    folder_name=$3

    download_file "$url" "$zip_file"
    echo "Extracting $zip_file..."
    unzip -q "$zip_file" -d "$folder_name"
    rm "$zip_file"
    echo "Extraction of $zip_file completed"
}


download_and_extract "http://images.cocodataset.org/annotations/annotations_trainval2017.zip" "annotations_trainval2017.zip" "annotations"

mv annotations/annotations/* annotations/
rm -r annotations/annotations

echo "All JSON files downloaded successfully."
