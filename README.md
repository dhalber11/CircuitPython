# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
For this assignment we were tasked with making the neopixel on the board light up different colors. This was our first assignment in Circuit Python. 

Here's how you make code look like code:

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

print("Make it red!")

while True:
    dot.fill((255, 0, 0))

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
This assignment was used as our intro to the world of Circuit Python. A lot of the time spent on it was downloading libraries and setting ourselves up for the rest of the year. Learning a new language is always difficult but this was a good introduction into the world of Circuit Python. It left me with a good understanding of how the actual platform works and how to code and make things work. 



## CircuitPython_Servo

### Description & Code
For this assignment we were tasked to use a servo and a couple buttons to control it. The servo had to go back and forth between 0 and 180 degrees. The spicy part was to only have the servos move when the buttons are pressed.  
```python
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D1)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN 

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.

my_servo = servo.Servo(pwm, min_pulse=600, max_pulse=2700)

angle = 90 

while True:
   if btn1.value and angle <180:
      print("btn1 pressed")
      angle = angle +5 
      my_servo.angle = angle 
      time.sleep(0.01)
   elif btn2.value and angle >0:
      print("btn2 pressed")
      angle = angle -5 
      my_servo.angle = angle 
      time.sleep(0.01)
   else: 
      print("servo off")
      time.sleep(1)


```

### Evidence


https://user-images.githubusercontent.com/113122357/193072533-0f375f94-46a8-4b5a-bf4c-c79ef55ac3d1.mp4




### Wiring
![Neat Stantia-Bombul](https://user-images.githubusercontent.com/113122357/193075627-149c96a1-73db-4443-9701-8494ad860df8.png)


### Reflection

This assignment introduced us to a few more libraries and allowed us to learn and recap on wiring different components. It was a bit difficult and taught us to use code from online and tweak it for our own use. The spicy part was difficult to figure out but I was able to finish it with some help from friends. 


## CircuitPython_Distance Sensor

### Description & Code
For this assignment we were tasked with using the values from a distance sensor and fading the colors in and out. 
```python
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio 

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = .1

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


```

### Evidence


https://user-images.githubusercontent.com/113122357/197228814-64b68543-8df9-49a2-94a3-cd4bae5fec09.mp4



### Wiring
![Incredible Luulia-Lappi](https://user-images.githubusercontent.com/113122357/197229576-1ee94bfb-3387-4934-84f3-4033f21a40d9.png)

### Reflection
This was a relatively basic assignment that simply told us to print the values of the HC-SRO4. However the more difficult part came with smoothly shifting the color of the Neopixel based off of those values. That right there is the key to this assignment, we had to use a map_range function to take the values given and shift the colors between them. This was a helpful and challenging assignment that taught me about this new function that I had never used before. 



## CircuitPython_LCD

### Description & Code
For this assignment we had to use a LCD display to show the amount of times a button was pressed and whether or not a switch is on or off. 
```python
import board
import time
import digitalio
from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull 

btn= DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

switch = DigitalInOut(board.D9)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

value = 0
SwitchState = switch.value

lcd.print("Button:")   #prints what is in the quotes to the lcd 
lcd.set_cursor_pos(0,8)

prev_state = btn.value

while True:
    cur_state = btn.value

    if cur_state != prev_state:  
        if not cur_state:
            value+=1
            lcd.set_cursor_pos(0,8)
            lcd.print(str(value))
    if switch.value == True:
      lcd.set_cursor_pos(1,0)
      lcd.print("True")
    else:
      
      lcd.set_cursor_pos(1,0)
      lcd.print("False")

    prev_state = cur_state
  

```

### Evidence

https://user-images.githubusercontent.com/113122357/197231832-460e8970-b184-42ca-ac3e-2e6dc0a6dfe3.mp4

Credits to Jinho Park for the video find his repository here: https://github.com/Jpark27614/CircuitPython

### Wiring!
[unnamed](https://user-images.githubusercontent.com/113122357/197233714-8c205f59-5b4f-4fbc-b296-d2d00e058221.png)


### Reflection
This assignment was a bit challenging as there was some new parts that I had not used before. The Slideswitch was a bit hard to figure out but with the right libraries it is not difficult. I had a bit of difficulty finding the LCD libraries but other than that this was just a good refresher to the world of LCD. 

## Swing Arm

### Description
For this assignment we were given an Onshape document with plans for a "Swing Arm". We were tasked with recreating this part using the given dimensions and answering a few questions that changed certain values within the part. 
### Evidence
Link to the Onshape document here: https://cvilleschools.onshape.com/documents/d05abfa364cd39b7a04ebfbd/w/d394d172d7c5c0d077bd6404/e/bc3a927ab2978dd4235e89ba?renderMode=0&uiState=6356a95bf85808678d2296f2
![image](https://user-images.githubusercontent.com/113122357/197559885-68d5dc36-702f-463f-955d-60c9db28335f.png)

### Reflection
This assignment was a bit of a more difficult one for me. Overall there was a trick to it that involved using constraints on all of the lines before you used dimensioning. This allowed a lot more ease when dimensioning and saved you from dimensioning multiple things. I had a few issues with the constraints when they overlapped but that was fixed through the simplest way possible, guess and check. This was a helpful assignemnt and we have had one more in the past that was similar to this.
