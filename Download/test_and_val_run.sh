#!/bin/bash
set -e
#SBATCH --job-name=Gen_data
#SBATCH --output=gen_data.out
#SBATCH --error=gen_data.err
#SBATCH --time=12:00:00
#SBATCH --mem=50G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodelist=gput039

module load singularity

echo "Filtering data"

singularity run --nv ../../ultralytics_latest.sif python3 B3_coco_filter.py

echo "Downloading Data"

singularity run --nv ../../ultralytics_latest.sif python3 B4_download_coco_imgs.py --skip_train True

cd ../Style/

echo "Generating Test Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/test/ --style_dir ../Data/style_data/ --output ../Data/datasets/test/images/ --delete True

echo "Generating Val Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/val/ --style_dir ../Data/style_data/ --output ../Data/datasets/val/images/ --delete True

echo "Style Job Completed"