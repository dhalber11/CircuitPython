# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython_MotorControl](#CircuitPython_MotorControl)
* [CircuitPython_Encoder](#CircuitPython_Encoder)
* [CircuitPython_TempSensor](#CircuitPython_TempSensor)
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

## CircuitPython_MotorControl

### Description 
For this assignment we needed to use a potentiometer to control a motor. The motor was wired through a transistor and diode
### Code
```python 
import time
import board
from analogio import AnalogIn,AnalogOut
from digitalio import DigitalInOut, Direction, Pull
import simpleio
from adafruit_motor import motor 

motorpin = AnalogOut(board.A1)
potentiometer = AnalogIn(board.A0)  # potentiometer connected to A1, power & ground

while True:

    print((int(simpleio.map_range(potentiometer.value,0,65535,0,255)),))     
    time.sleep(0.25) 
    motorpin.value = potentiometer.value
```

### Wiring 
![image](https://user-images.githubusercontent.com/113122357/199763599-3e56c349-a8c1-442a-b987-27956010ca2e.png)

### Reflection 
This assignment was difficult, that is for certain. I had many small issues with wiring that were breaking my entire circuit. The code for this assignment was extremely straightforward and quite simple. However the wiring had to be perfect or the "magic smoke" would come out of it all. Since we were working with a large amount of voltage there was a chance of the arduino being completely fried when we powered it up. There was a bunch of small issues that I needed some help to get around including some with my battery pack and the ground wires for them. As well as the transistor and diode. Overall it was very difficult with the wiring but easy with the code.  

## CircuitPython_Encoder 

### Description
For this assignment we were told to get a working traffic light using a rotary encoder and an lcd to display the selection. You can scroll to a setting on the lcd then select it by clicking on the encoder. 

### Code
```python
import rotaryio
import time
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import digitalio
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


enc = rotaryio.IncrementalEncoder(board.D9, board.D8,2)
last_position = None

encBtn = digitalio.DigitalInOut(board.D7)
encbtn = digitalio.Direction.INPUT
encbtn  = digitalio.Pull.UP

global prevState

def btnControl(buttonVal ,out):
    global prevState
    if buttonVal and buttonVal != prevState:
        prevState = True
        if out == 0:
            dot.fill((255,0,0))
        elif out == 1:
                dot.fill((255,255,0))
        else:
                dot.fill((0,255,0))
    elif  not buttonVal:
        prevState = False
     
        

def retEnc(x):
    array = ["stop","caution","go"] 
    output = x%3
    btnControl(encBtn.value,output)
    return array[output]




while True:
    lcd.print(retEnc(enc.position))
    time.sleep(.05)
    lcd.clear()
    print(f"{retEnc(enc.position)} {enc.position} {encBtn.value}")
```
### Wiring 
![Screenshot 2023-03-21 115021](https://user-images.githubusercontent.com/113122357/226664630-8d13238f-8fc5-40b8-9cc1-1b78a225223c.png)

### Reflection
I have to give credit to Paul for the code for this assignment. The wiring was straightforward as it has all been done before with the lcd. For the encoder some quick research was all I needed to figure it out. Overall an interesting assignment to learn about the rotary encoder. 

## CircuitPython_TempSensor

### Description
For this assignment we were told to get the temperature of the environment and print that value to an lcd. Along with this we needed to print a message that says "too hot", "too cold", or "just right", depending on the temperature. 

### Code
```python 
import board
import analogio
import time
from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

TMP36_PIN = board.A0  # Analog input connected to TMP36 output.

i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c,0x27), num_rows=2, num_cols=16)
# Function to simplify the math of reading the temperature.
lcd.set_cursor_pos(0,0)
lcd.print("temp:")
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


tmp36 = analogio.AnalogIn(TMP36_PIN)


while True:
   
    temp_C = tmp36_temperature_C(tmp36)
   
    temp_F = (temp_C * 9/5) + 32
   
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)
    lcd.set_cursor_pos(0, 6)
    lcd.print( "{}C " .format(temp_C)) 
    if temp_C >= 28:
        lcd.clear
        lcd.set_cursor_pos(1,0) 
        lcd.print("Too Hot!")
    if temp_C <= 23:
        lcd.clear
        lcd.set_cursor_pos(1,0)
        lcd.print("Brrr it's too cold")
    if temp_C > 23 and temp_C < 28: 
        lcd.clear
        lcd.set_cursor_pos(1,0)
        lcd.print("Just right")
   # lcd.set_cursor_pos(1,0)
   # lcd.print( "{}F" .format(temp_F)) 
```

### Wiring 
This wiring is very similar to the previous assignment. Simply replace the rotary encoder with a temperature sensor. The LCD remains the same. 
### Reflection
This assignment was very cool to play with another new tool to be able to measure air temperature. I was also able to get a refresher on the LCD coding that was helpful. It was a pretty straightforward assignment once the code for the temperature sensor was figured out. Libraries help SO much. 


# CAD 

## Swing Arm

### Description
For this assignment we were given an Onshape document with plans for a "Swing Arm". We were tasked with recreating this part using the given dimensions and answering a few questions that changed certain values within the part. 
### Evidence
Link to the Onshape document here: https://cvilleschools.onshape.com/documents/d05abfa364cd39b7a04ebfbd/w/d394d172d7c5c0d077bd6404/e/bc3a927ab2978dd4235e89ba?renderMode=0&uiState=6356a95bf85808678d2296f2
![image](https://user-images.githubusercontent.com/113122357/197559885-68d5dc36-702f-463f-955d-60c9db28335f.png)

### Reflection
This assignment was a bit of a more difficult one for me. Overall there was a trick to it that involved using constraints on all of the lines before you used dimensioning. This allowed a lot more ease when dimensioning and saved you from dimensioning multiple things. I had a few issues with the constraints when they overlapped but that was fixed through the simplest way possible, guess and check. This was a helpful assignemnt and we have had one more in the past that was similar to this.


## Pull Copter 

### Description
For this assingment we were split into partners and given an assignment that had two parts, Student A and Student B. Student B was a bit more challenging and this was my job for this assignment. We had to follow the given steps to design a pull copter that met the criteria provided. 

### Evidence
Link to Onshape document[ https://cvilleschools.onshape.com/documents/5922435839c6c360dffb1e19/w/cc4dba477bb2da6825e45380/e/b3e59d64fa0784bb0cf2d4a0?renderMode=0&uiState=6356ac2c5ddca250f4a1da28]
![image](https://user-images.githubusercontent.com/113122357/197562679-d844b237-e055-4d2e-b263-1ba693dec6e4.png)
![image](https://user-images.githubusercontent.com/113122357/197562882-ac9828fe-0c8c-4be9-b8dc-514da0b5b171.png)

### Reflection
This assignment was relatively easy for me as there was step by step info on how we were meant to do it. Most of the tools that we used were review for me but some were new such as the sweep tool and others. It went relatively smoothly and no notable issues arose during the design. It was fun to design this prop and see it all come together using shared assemblies.

## Multi-Part Design Studios

### Description
For this assignment we had a prompt similar to the swing arm but in the format of the Onshape Certification test. We were given pdfs of Design Intents as well as some dimensions and we were required to fully design the part and then answer four questions that changed certain dimensions. Answers were based on weight. 
### Evidence
Link to Onshape document here: https://cvilleschools.onshape.com/documents/1759606a5b121d398365f478/v/bcd464deee99af5d0a15353f/e/af2a8f3176123590fbad0882?renderMode=0&uiState=6356aeb8285ef11c0bbb29b8
![image](https://user-images.githubusercontent.com/113122357/197565373-8e1af1e1-e1e9-4fe7-9521-954d292b65ba.png)
![image](https://user-images.githubusercontent.com/113122357/197565501-3575832b-d576-4d36-ab27-20470fb575db.png)
![image](https://user-images.githubusercontent.com/113122357/197565593-fabd41ab-6d4e-4ca7-972c-e2d31e443312.png)
![image](https://user-images.githubusercontent.com/113122357/197565738-a78593ac-8d81-4bfe-a319-15fecf9c7e96.png)

### Reflection
Overall I did have some difficulty with this assignment mainly during the transition between questions. As I was changing dimensions something would get thrown off and I would be stuck trying to find out what that was. My main issue was constraints and what in the Part that I based new sketches off of. Everything is based off of another thing so if one changed then the other might come with it. In the end I got some help from Mr.H and he was a great help in finding what was off with my designs. This assignment was very useful as it was good practice for the Onshape Certification. 

