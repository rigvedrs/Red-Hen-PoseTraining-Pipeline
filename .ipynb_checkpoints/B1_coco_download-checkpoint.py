import json 
import requests 
import os

coco_json_path = '../extra/coco_json/person_keypoints_val2017.json'

with open(coco_json_path, 'r') as file:
    coco_data = json.load(file)