#!/bin/bash
set -e
#SBATCH --job-name=StyleJob
#SBATCH --output=StyleJob.out
#SBATCH --error=StyleJob.err
#SBATCH --time=12:00:00
#SBATCH --mem=100G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodelist=gput042

echo "Stage: 1 - Loading environment"
module load singularity
cd Red-Hen-PoseTraining-Pipeline/
echo "Stage: 1 - Environment successfully loaded"

echo "Stage: 2 - Generating Data"
echo "Stage: 2 - Generating Train Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/train/ --style_dir ../Data/style_data/ --output ../Data/datasets/train/images/ --delete True

echo "Stage: 2 - Generating Test Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/test/ --style_dir ../Data/style_data/ --output ../Data/datasets/test/images/ --delete True

echo "Stage: 2 - Generating Val Data"
singularity run --nv ../../ultralytics_latest.sif python3 applystyle.py --content_dir ../Data/coco_data/val/ --style_dir ../Data/style_data/ --output ../Data/datasets/val/images/ --delete True
echo "Stage: 2 Successfully completed"
