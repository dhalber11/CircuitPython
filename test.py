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

lcd.print("Button:")
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
      lcd.print("Up  ")
    else:
      
      lcd.set_cursor_pos(1,0)
      lcd.print("Down")

    prev_state = cur_state
  