#!/bin/bash

git clone https://github.com/rigvedrs/pytorch-AdaIN.git

mv pytorch-AdaIN/{.*,*} ./

rm -rf pytorch-AdaIN/

mkdir models/

wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1bMfhMMwPeXnYSQI6cDWElSZxOxc6aVyr' -O models/decoder.pth

wget --no-check-certificate 'https://drive.google.com/uc?id=1EpkBA2K2eYILDSyPTt0fztz59UjAIpZU' -O models/vgg_normalised.pth

echo "Download completed successfully."

python3 applystyle.py --content_dir ../Data/coco_data/train/ --style_dir Data/style_data/ --output ../Data/datasets/train/images/

python3 applystyle.py --content_dir ../Data/coco_data/test/ --style_dir Data/style_data/ --output ../Data/datasets/test/images/

python3 applystyle.py --content_dir ../Data/coco_data/val/ --style_dir Data/style_data/ --output ../Data/datasets/val/images/