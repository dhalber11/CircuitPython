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
        