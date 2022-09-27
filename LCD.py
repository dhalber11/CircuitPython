import time
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
from digitalio import DigitalInOut, Direction, Pull 



btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

switch = DigitalInOut(board.D9)
switch.direction = Direction.INPUT
switch.pull = Pull.UP 

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=4, num_cols=20)

switch

lcd.clear 
value1 = 0 

prev_state = btn.value
lcd.print("button:")
lcd.set_cursor_pos(1,0)
lcd.print("switch:")
lcd.set_cursor_pos(0,8)

while True:
    cur_state = btn.value
    if cur_state != prev_state : 
        if not cur_state and switch.value == True:
           lcd.print(str(value1))
           lcd.set_cursor_pos(0,8)
           value1 +=1 
           print(value1)
           print(switch.value)
        if switch.value == False:
            lcd.set_cursor_pos(1,8)
            lcd.print(str(switch.value))
            value1 = value1                                     
    
         
       
    
    prev_state = cur_state
