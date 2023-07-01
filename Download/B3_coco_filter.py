from pycocotools.coco import COCO
import json
import argparse

# Parsing arguments
parser = argparse.ArgumentParser()

parser.add_argument('--json_dir', type=str, default='coco/annotations/', help='Directory to JSON')
parser.add_argument('--output_dir', type=str, default='coco/', help='File path to output directory')

args = parser.parse_args()

output_dir = args.output_dir

# Path to the JSON annotation files
json_dir = args.json_dir
train_annotation_file = json_dir + 'person_keypoints_train2017.json'
val_annotation_file = json_dir + 'person_keypoints_val2017.json'

# Initialize COCO instances for train and val annotations
coco_train = COCO(train_annotation_file)
coco_val = COCO(val_annotation_file)

# Filter images in the train set
train_image_ids = coco_train.getImgIds(catIds=coco_train.getCatIds('person'))
filtered_train_image_ids = []
filtered_train_annotations = []
for image_id in train_image_ids:
    ann_ids = coco_train.getAnnIds(imgIds=image_id, iscrowd=None)
    annotations = coco_train.loadAnns(ann_ids)
    if any(annotation['category_id'] == 1 for annotation in annotations):  # Person category ID is 1
        filtered_train_image_ids.append(image_id)
        filtered_train_annotations.extend(annotations)

# Filter images in the validation set
val_image_ids = coco_val.getImgIds(catIds=coco_val.getCatIds('person'))
filtered_val_image_ids = []
filtered_val_annotations = []
for image_id in val_image_ids:
    ann_ids = coco_val.getAnnIds(imgIds=image_id, iscrowd=None)
    annotations = coco_val.loadAnns(ann_ids)
    if any(annotation['category_id'] == 1 for annotation in annotations):  # Person category ID is 1
        filtered_val_image_ids.append(image_id)
        filtered_val_annotations.extend(annotations)

# Print the number of filtered images in train and val sets
print(f"Filtered Train Images: {len(filtered_train_image_ids)}")
print(f"Filtered Val Images: {len(filtered_val_image_ids)}")



# Get the filtered image information from the COCO instances
filtered_train_images = coco_train.loadImgs(filtered_train_image_ids)
filtered_val_images = coco_val.loadImgs(filtered_val_image_ids)

# Prepare the filtered train dataset
filtered_train_data = {
    'info': coco_train.dataset['info'],
    'licenses': coco_train.dataset['licenses'],
    'images': filtered_train_images,
    'annotations': filtered_train_annotations,
    'categories': coco_train.dataset['categories']
}

# Save the filtered train dataset to 'filtered_train.json'

with open(output_dir+'train.json', 'w') as f:
    json.dump(filtered_train_data, f)

print('Train file saved.')


# Select the first 1000 images from the validation dataset for val.json and save the remaining for test.json

# Select the first 1000 images from the validation dataset for val.json and save the remaining for test.json

# Select the first 1000 filtered images for validation
val_image_ids_selected = filtered_val_image_ids[:1000]

# Select the remaining images for testing
test_image_ids = filtered_val_image_ids[1000:]

# Filter images and annotations for validation set
val_images = coco_val.loadImgs(val_image_ids_selected)
val_ann_ids = coco_val.getAnnIds(imgIds=val_image_ids_selected)
val_annotations = coco_val.loadAnns(val_ann_ids)

# Filter images and annotations for test set
test_images = coco_val.loadImgs(test_image_ids)
test_ann_ids = coco_val.getAnnIds(imgIds=test_image_ids)
test_annotations = coco_val.loadAnns(test_ann_ids)

# Prepare the validation dataset
val_data = {
    'info': coco_val.dataset['info'],
    'licenses': coco_val.dataset['licenses'],
    'images': val_images,
    'annotations': val_annotations,
    'categories': coco_val.dataset['categories']
}

# Save the validation dataset to 'val.json'
with open(output_dir+'val.json', 'w') as f:
    json.dump(val_data, f)

print('Val file saved.')

# Prepare the test dataset
test_data = {
    'info': coco_val.dataset['info'],
    'licenses': coco_val.dataset['licenses'],
    'images': test_images,
    'annotations': test_annotations,
    'categories': coco_val.dataset['categories']
}

# Save the test dataset to 'test.json'
with open(output_dir+'test.json', 'w') as f:
    json.dump(test_data, f)

print('Test file saved.')
