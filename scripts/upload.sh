#!/bin/bash

cd ~/github/image_files/
convert $1.ppm $1.png

cd ~/github/graphics_work/scripts/
python upload.py $1

#cd ~/github/image_files/
#rm *
