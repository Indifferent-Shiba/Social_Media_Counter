#!/bin/bash

inst_count=`cat /home/pi/inst.txt`
hearts=$(printf '%06s\n' $inst_count)
echo "$hearts"
sudo $PYTHON/zz-image-n-text.py -i $GRAPHICS_PATH/Instagram.ppm -t "$hearts" -y 25 -a 255,255,255 -s 10 -f $FONT_PATH/FixedMedium-30.bdf $PYTHON_OPTS
