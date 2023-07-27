#!/bin/bash
#SBATCH --job-name=gen_data
#SBATCH --output=gen_data.out
#SBATCH --error=gen_data.err
#SBATCH --partition=gpu
#SBATCH --constraint=gpup100
#SBATCH --nodelist=gput039
#SBATCH --gres=gpu:1
#SBATCH --mem=50GB

module load singularity

echo "Filtering data"

singularity run --nv ../../ultralytics_latest.sif python3 B3_coco_filter.py

echo "Downloading Data"

singularity run --nv ../../ultralytics_latest.sif python3 B4_download_coco_imgs.py --skip_train True

cd ../Style/

echo "Generating Test Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/test/ --style_dir ../Data/style_data/ --output ../Data/dataset/test/images/ --delete True

echo "Generating Val Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/val/ --style_dir ../Data/style_data/ --output ../Data/dataset/val/images/ --delete True

echo "Style Job Completed"
