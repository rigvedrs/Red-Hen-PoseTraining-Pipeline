#!/bin/bash
#SBATCH --job-name=train
#SBATCH --output=train.out
#SBATCH --error=train.err
#SBATCH --partition=gpu
#SBATCH --constraint=gpup100
#SBATCH --nodelist=gput039
#SBATCH --gres=gpu:1
#SBATCH --mem=50GB

module load singularity

echo "Filtering data"

singularity run --nv ../../ultralytics_latest.sif python3 tune.py

echo "Training Completed"
