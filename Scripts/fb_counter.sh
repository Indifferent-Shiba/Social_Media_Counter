#!/bin/bash

fb_count=`cat /home/pi/fb.txt`
likes=$(printf '%06s\n' $fb_count)
echo "$likes"
sudo $PYTHON/zz-image-n-text.py -i $GRAPHICS_PATH/FB.ppm -t "$likes" -y 25 -a 255,255,255 -s 10 -f $FONT_PATH/FixedMedium-30.bdf $PYTHON_OPTS
