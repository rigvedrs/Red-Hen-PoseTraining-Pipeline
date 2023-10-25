# Red-Hen-PoseTraining-Pipeline
This repo contains the training pipeline for applying style transfer on COCO dataset and finetuning the yolo v8 model on it.

The proposed pipeline for training looks like the following:

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*WjdII99nuk5gTYaDTg-hyg.png)

The only difference here is I have used the new YOLO V8 model.

## Run
To run the entire pipeline, simply run the following command:
```
sbatch run_pipeline.sh 
```

This will run the entire pipeline from generating the data to training the model on it. 

Note: Ensure that you also have the singularity file in the same folder. You can do that by running this:
```
rsync -az <yourid>@pioneer.case.edu:/mnt/rds/redhen/gallina/home/rss210/ultralytics_latest.sif .
```
