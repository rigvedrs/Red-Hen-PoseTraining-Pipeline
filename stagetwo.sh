#!/bin/bash
set -e
#SBATCH --job-name=SecondJob
#SBATCH --output=SecondJob.out
#SBATCH --error=SecondJob.err
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
cd Style/
singularity run --nv ../../ultralytics_latest.sif python3 B6_download_and_apply_adain.py
echo "Stage: 2 Successfully completed"

echo "Stage: 3 - Fine-tuning the pose detection model"
cd ../Train/
singularity run --nv ../../ultralytics_latest.sif python3 tune.py
echo "Stage: 3 Successfully completed"
