# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel
import simpleio 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)

while True:
    try:
        cm=int(sonar.distance)
        print((cm,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if cm<5 :
      dot.fill((255, 0, 0))
    elif cm >= 5 and cm < 20 : 
        x = simpleio.map_range(cm, 5, 20, 0, 255)
        blue = x 
        red = 255-x 
        green = 0
        dot.fill((red, green, blue))
    elif cm >= 20 and cm<35 : 
        y = simpleio.map_range(cm, 20, 35, 255, 0)
        red = 0 
        green = 255- y
        blue = y
        dot.fill((red, green, blue)) 
    elif cm >35 :
        dot.fill((0, 255, 0))
