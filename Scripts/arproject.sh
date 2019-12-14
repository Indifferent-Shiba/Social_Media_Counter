#!/bin/bash


##############################
# Paths and Option Variables ##
##############################
#export $CPP
CPP=/home/display32x64/rpi-rgb-led-matrix/examples-api-use
PYTHON=/home/pi/display32x64/rpi-rgb-led-matrix/bindings/python/samples

CPP_OPTS="--led-no-hardware-pulse --led-rows=32 --led-cols=32 --led-chain=4"
PYTHON_OPTS="--led-no-hardware-pulse LED_NO_HARDWARE_PULSE --led-rows=32 --led-cols=32 --led-chain=4"

GRAPHICS_PATH=/home/pi/display32x64/rpi-rgb-led-matrix/graphics

FONT_PATH=/home/pi/display32x64/rpi-rgb-led-matrix/fonts
LEDFONT="-f $FONT_PATH/FixedMedium-30.bdf"


################################
# Shuffle Transition Variables ##
################################

#Follow this structure for Animations#
t1="sudo $PYTHON/zz-animation.py -i $GRAPHICS_PATH/Animations/ectb/ectb#.ppm -n 74 -s 8 $PYTHON_OPTS"
t2="sudo $PYTHON/zz-animation.py -i $GRAPHICS_PATH/Animations/ectb/ectb#.ppm -n 74 -s 8 $PYTHON_OPTS"
t3="sudo $PYTHON/zz-animation.py -i $GRAPHICS_PATH/Animations/ectb/ectb#.ppm -n 74 -s 8 $PYTHON_OPTS"
t4="sudo $PYTHON/zz-animation.py -i $GRAPHICS_PATH/Animations/ectb/ectb#.ppm -n 74 -s 8 $PYTHON_OPTS"

#Follow this structure for scrolling images#
#t#="sudo $PYTHON/image-scroller.py -i $GRAPHICS_PATH/example.ppm -s 5 $PYTHON_OPTS"

#Follow this structure for small, repreated animations#
#t#="sudo $PYTHON/zz-animation.py -i $GRAPHICS_PATH/Animations/example/example#.ppm -n 40 -s 8 --led-no-hardware-pulse LED_NO_HARDWARE_PULSE --led-rows=32 --led-cols=32"

###########################
#Screen Transition Counter##
###########################

#Add each transition to the transition to the variable here, increasing the # by 1#
transitions=( "$t1" "$t2" "$t3" "$t4" )

#Checks the number of transitions that are there#
translen=${#transitions[@]}

#A place to store shuffled data. However, when adding new data, the old shuffle log may need to be ran through one time to get the new transition,
#or primed with the desired transition by pasting the transition with its full paths into it.#
shuf_log=`wc -l /home/pi/display32x64/rpi-rgb-led-matrix/shuffle_log.txt | cut -f1 -d' '`


while [ true ]
do
#if the number t is less than the number of transitions we have, run one of our social media scripts and grab a transition from the shuffle log#
	if [ $[t] -lt ${shuf_log} ]; then
		$(sed -n ${t}p shuffle_log.txt)
		((t += 1))
		echo $t
		echo $shuf_log
		source /home/pi/display32x64/rpi-rgb-led-matrix/fb_counter.sh
		$(sed -n ${t}p shuffle_log.txt)
		((t += 1))
		echo $t
		echo $shuf_log
		source /home/pi/display32x64/rpi-rgb-led-matrix/insta_counter.sh
		$(sed -n ${t}p shuffle_log.txt)
		((t += 1))
		echo $t
		echo $shuf_log
		source /home/pi/display32x64/rpi-rgb-led-matrix/twi_counter.sh
		$(sed -n ${t}p shuffle_log.txt)
		((t += 1))
		echo $t
		echo $shuf_log
		source /home/pi/display32x64/rpi-rgb-led-matrix/yt_counter.sh
	fi
#once the number t is greater than the number of transitions, reshuffle the shuffle log and start over#
	if [ ${t} -gt ${shuf_log} ]; then
		t=1
		echo "" > shuffle_log.txt
		echo $t
		shuf -e "${transitions[@]}" -o shuffle_log.txt
	fi
done
