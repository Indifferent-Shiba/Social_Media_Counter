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

class DoubleText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(DoubleText, self).__init__(*args, **kwargs)

    def run(self):
        self.image = Image.open("./graphics/Pizza.ppm").convert('RGB')
        self.image.resize( (self.matrix.width, self.matrix.height), Image.ANTIALIAS )
        self.matrix.SetImage( self.image, 0 );

        font = graphics.Font()
        font.LoadFont( "./fonts/6x10.bdf" )
        textColor = graphics.Color( 255, 165, 0 );

        graphics.DrawText( self.matrix, font, 36, 12, textColor, "BNIC Tonight" );
        graphics.DrawText( self.matrix, font, 36, 24, textColor, "6 PM - Pizza" );
        time.sleep( 10.0 )


# Main function
if __name__ == "__main__":
    doubleText = DoubleText()
    if (not doubleText.process()):
        doubleText.print_help()
