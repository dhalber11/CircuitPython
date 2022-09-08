''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import RGB

r1 = board.D8
b1 = board.D9
g1 = board.D10
r2 = board.D4
b2 = board.D5
g2 = board.D7 # D6 uses the same timer as D8,9,10.  Avoid!

full = 65535                # Max Brightness
half = int(65535/2)         # Half Brightness

myRGBled1 = RGB(r1, g1, b1) # create a new RGB object, using pins 8, 9, & 10
myRGBled2 = RGB(r2, g2, b2) # create a new RGB object, using pins 4, 5, & 7


while True:
    '''Shines two RGB LEDs in opposing colours, then rainbows!'''
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.red()
    myRGBled2.cyan()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.green()
    myRGBled2.magenta()
    time.sleep(1)
    myRGBled1.off()
    myRGBled2.off()
    time.sleep(2)

    myRGBled1.Blinky(rate1) # Obviously you should replace "rate1" with a real number...
    myRGBled2.Blinky(rate2) # Sames
    time.sleep(3)

# extra spicy (optional):
# myRGB1.rainbow(rate1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
# myRGB2.rainbow(rate2) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
# time.sleep(5)
