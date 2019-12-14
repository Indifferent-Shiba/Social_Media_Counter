#!/bin/bash

twi_count=`cat /home/pi/twi.txt`
tweets=$(printf '%06s\n' $twi_count)
echo "$tweets"
sudo $PYTHON/zz-image-n-text.py -i $GRAPHICS_PATH/Twitter_blue.ppm -t "$tweets" -y 25 -a 255,255,255 -s 10 -f $FONT_PATH/FixedMedium-30.bdf $PYTHON_OPTS
