#!/bin/bash

rsync -az rsync ultralytics_latest.sif $PFSDIR
cd $PFSDIR
echo ".sif File synced successfully"

echo "Loading singularity enviroment...."
module load singularity
echo "Enviroment successfully Loaded."

echo "Stage: 1 - Loading Code Files"
git clone https://github.com/rigvedrs/Red-Hen-PoseTraining-Pipeline.git
echo "Code files succesfully loaded"

echo "Stage: 2 - Downloading and Generating Data"
singularity run --nv ultralytics_latest.sif python3 Red-Hen-PoseTraining-Pipeline/generator.py
echo "Stage: 2 Succesfully completed"

echo "Stage: 2- Training the feature-extractor to extract patch level features"
singularity run --nv christian-art-tagging_latest.sif python feature_extractor/train.py -c --train --device cuda --data_dir feature_extractor/

echo "Stage: 3- Training the Image-Captioning model that uses intra-modal features"
singularity run --nv christian-art-tagging_latest.sif python captioning/train.py --data_dir curation/EmileMaleDataset/ --feature_extractor_path feature_extractor/artDL.pt --device cuda --train
