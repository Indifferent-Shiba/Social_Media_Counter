#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image
from rgbmatrix import graphics

# ############################################################################################
# Notes from Bruce Tong:
#
# This code is the result experimenting and playing with the sample python code. It will not
# do everything your project probably wants to do. Between this code and the other samples,
# you already have a lot of options, but for really fancy stuff you'll have to write your
# own program. I've tried to document this program to make that easier for you.
# ############################################################################################

# ############################################################################################
# Define a class that inherits from the SampleBase class found elsewhere in this project.
# The SampleBase class is intended to be an example, but it is pretty good for general use.
# ############################################################################################

class ImageAndText(SampleBase):

# ############################################################################################
# Adding arguments to the parser is enough to make the program collect those arguments from
# the command line, add it to the help text shown by -h and fill in the specified default
# if an argument was not received. Once added, the argument will show up as the variable...
#
#     self.args.XXXXX
#
# where XXXXX is the full name of the argument you specified. So --color is self.args.color
# when you get around to trying to use it. Something to keep in mind is that when you get
# an argument from the command line, it might be in the form of a string value that you
# might need to cast into a different type for your uses, int(), float(), etc.
# ############################################################################################

    def __init__(self, *args, **kwargs):
        super(ImageAndText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-a", "--color", help="The text color", default="255,255,255")
        self.parser.add_argument("-f", "--font", help="The font file", default="/home/pi/display32x64/rpi-rgb-led-matrix/fonts/FixedMedium-30.bdf")
        self.parser.add_argument("-i", "--image", help="The image to display", default="/home/pi/display32x64/rpi-rgb-led-matrix/graphics/runtext.ppm")
        self.parser.add_argument("-s", "--sleep", help="How long to sleep in seconds", default=20)
        self.parser.add_argument("-t", "--text", help="The text to show", default="Hello World!")
        self.parser.add_argument("-x", "--xoffset", help="The text X offset", default=34)
        self.parser.add_argument("-y", "--yoffset", help="The text Y offset", default=24)

# ############################################################################################
# The run() method drives the program.
# ############################################################################################

    def run(self):

        # ####################################################################################
        # Record the start time. We need this to know when to exit the program.
        # ####################################################################################

        start = time.time()

        # ####################################################################################
        # We won't really loop forever if the timer feature is functional. We just don't know
        # how many times to loop to fill the desired time, so we let the timer break the loop.
        # This example really doesn't need a loop since neither the image nor the text
        # changes during execution, but I left the loop in so that you could make it do
        # more dynamic things like move the image and text.
        # ####################################################################################

        while True:
            # ################################################################################
            # Prepare and render the image. We only do this once so we don't waste time loading
            # the image over and over again. We also could have put this code outside the loop.
            # ################################################################################

            if not 'image' in self.__dict__:
                self.image = Image.open(self.args.image).convert('RGB')
                self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)

            # ################################################################################
            # Double buffering lets the program show one display buffer while it builds another.
            # Then you switch buffers and get one flicker instead of lots of them.
            # Later in the code we'll swap the buffers.
            # ################################################################################

            double_buffer = self.matrix.CreateFrameCanvas()
            double_buffer.SetImage(self.image, 0)

            # ################################################################################
            # Prepare and render the text by loading the font and extracting the RGB values.
            # ################################################################################

            font = graphics.Font()
            font.LoadFont(self.args.font)

            colorList = self.args.color.split(",")
            textColor=graphics.Color( int(colorList[0]), int(colorList[1]), int(colorList[2]) )

            graphics.DrawText( double_buffer, font, \
                int(self.args.xoffset), int(self.args.yoffset), \
                textColor, self.args.text )

            # ################################################################################
            # Show the newly generated buffer by swapping in our new display buffer...
            # ################################################################################

            double_buffer = self.matrix.SwapOnVSync(double_buffer)

            # ################################################################################
            # This sleep just basically gives the CPU a break. As was mentioned above in
            # the discussion of the while loop, this particular program could just sleep
            # the entire duration and then exit. But if you're doing any animation or
            # otherwise making things move, this sleep would control the pace.
            # ################################################################################

            time.sleep( 0.10 )

            # ################################################################################
            # See if we're over the time limit. If so, exit the loop and the program...
            # ################################################################################

            current = time.time()
            if current - start > float(self.args.sleep):
                break

# ############################################################################################
# ############################################################################################

# Main function
# e.g. call with
#  sudo ./zz-image-n-text.py --chain=4
# if you have a chain of four

if __name__ == "__main__":
    imageAndText = ImageAndText()
    if (not imageAndText.process()):
        imageAndText.print_help()
