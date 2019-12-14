#!/bin/bash

yt_count=`cat /home/pi/yt.txt`
subscribers=$(printf '%06s\n' $yt_count)
echo "$subscribers"
sudo $PYTHON/zz-image-n-text.py -i $GRAPHICS_PATH/yt.ppm -t "$subscribers" -y 25 -a 255,255,255 -s 10 -f $FONT_PATH/FixedMedium-30.bdf $PYTHON_OPTS
