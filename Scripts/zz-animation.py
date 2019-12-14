#!/usr/bin/env python
import time
from samplebase import SampleBase
from PIL import Image
from rgbmatrix import graphics

# To-Do:
# Parameter for Text to Display.
# Parameter for how long to Display.
# Parameter for Font.
# Parameter for Text Color.


# ############################################################################################
# Define a class that inherits from the SampleBase class found elsewhere in this project.
# The SampleBase class is intended to be an example, but it is pretty good for general use.
# ############################################################################################

class ImageAnimation(SampleBase):

# ############################################################################################
# Class Constructor...
# ############################################################################################

    def __init__(self, *args, **kwargs):
        super(ImageAnimation, self).__init__(*args, **kwargs)
        self.parser.add_argument("-a", "--color", help="The text color", default="255,255,255")
        self.parser.add_argument("-f", "--font", help="The font file", default="/home/pi/display32x64/rpi-rgb-led-matrix/fonts/FixedMedium-15.bdf")
        self.parser.add_argument("-i", "--image", help="The image to display", default="/home/pi/display32x64/rpi-rgb-led-matrix/graphics/animations/MegamanDance#.ppm")
        self.parser.add_argument("-n", "--number", help="The number of frames", default="2")
        self.parser.add_argument("-s", "--sleep", help="How long to sleep in seconds", default=20)
        self.parser.add_argument("-t", "--text", help="The text to show", default=" ")
        self.parser.add_argument("-x", "--xoffset", help="The text X offset", default=34)
        self.parser.add_argument("-y", "--yoffset", help="The text Y offset", default=24)

# ############################################################################################
# The run() method drives the program.
# ############################################################################################

    def run(self):

        # Prepare to render text...

        font = graphics.Font()
        font.LoadFont(self.args.font)
        textColor=graphics.Color(255,255,255)

        # We'll start with the first frame...

        currFrame = 1;

        # We're ready to start, so start the timer...

        start = time.time()

        while True:
            # Prepare and render the image. This involves replacing the # sign in the image
            # name with the current frame number...

            frameImageName = self.args.image.replace( "#", str( currFrame ), 1 )
            self.image = Image.open(frameImageName).convert('RGB')
            self.image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
            double_buffer = self.matrix.CreateFrameCanvas()
            double_buffer.SetImage(self.image, 0)

            # Render the text...

            my_text=self.args.text
            graphics.DrawText( double_buffer, font, int(self.args.xoffset), int(self.args.yoffset), textColor, my_text )

            # Show it by swapping in our new display buffer...

            double_buffer = self.matrix.SwapOnVSync(double_buffer)

            # Prepare for the next frame...
            currFrame = currFrame + 1

            if currFrame > int(self.args.number):
                currFrame = 1

            # See how we're doing on time and exit the loop if done...

            current = time.time()

            if ( current - start ) > float(self.args.sleep):
                break

            time.sleep( 0.10 )

            # End of function

# ############################################################################################
# ############################################################################################

# Main function
# e.g. call with
#  sudo ./zz-image-n-text.py --chain=4
# if you have a chain of four

if __name__ == "__main__":
    imageAnimation = ImageAnimation()
    if (not imageAnimation.process()):
        imageAnimation.print_help()
