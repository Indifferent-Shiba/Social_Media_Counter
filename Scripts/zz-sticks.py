#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from PIL import ImageDraw
import time
import random

# ##############################################################################################
# This is a minimilist program, using the SampleBase, that draws random lines of random colors.
#
# There is no API documentation. The best you can do is look to the binding definitions.
# These can be found in the project's bindings/python/rgbmatrix directory. Look at this file:
#
#     graphics.pyx
#
# There you will find the definitions for classes:
#
#     Color
#     Font
#
# And these methods for the graphics class:
#
#     DrawText( Canvas, Font, x, y, Color, Text )
#     DrawCircle( Canvas, x, y, radius, Color )
#     DrawLine( Canvas, x1, y1, x2, y2, Color )
#
# And it is handy to know that SampleBase provides a Canvas in self.matrix which is an rgbmatrix.
#
# ##############################################################################################

class Sticks(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Sticks, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            x1 = random.randint( 0, self.matrix.width-1 )
            y1 = random.randint( 0, self.matrix.height-1 )
            x2 = random.randint( 0, self.matrix.width-1 )
            y2 = random.randint( 0, self.matrix.height-1 )
            red = random.randint( 0, 255 )
            green = random.randint( 0, 255 )
            blue = random.randint( 0, 255 )
            graphics.DrawLine( self.matrix, x1, y1, x2, y2, graphics.Color( red, green, blue ) )
            time.sleep( 0.05 )


# Main function
if __name__ == "__main__":
    sticks = Sticks()
    if (not sticks.process()):
        sticks.print_help()
