#!/bin/bash
#SBATCH --job-name=MyJob
#SBATCH --output=myjob.out
#SBATCH --error=myjob.err
#SBATCH --time=12:00:00
#SBATCH --mem=100G
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --nodelist=gput042

echo "Stage: 1 - Loading Code Files and environment"
module load singularity
git clone https://github.com/rigvedrs/Red-Hen-PoseTraining-Pipeline.git
cd Red-Hen-PoseTraining-Pipeline/
echo "Stage: 1 Successfully completed"

echo "Stage: 2 - Downloading and Generating Data"
singularity run --nv ../ultralytics_latest.sif chmod +x generator.sh
singularity run --nv ../ultralytics_latest.sif ./generator.sh
echo "Stage: 2 Successfully completed"

echo "Stage: 2 - Fine-tuning the pose detection model"
cd Train
singularity run --nv ../../ultralytics_latest.sif python3 tune.py
echo "Stage: 2 Successfully completed"
