import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#Initialize the USB Keyboard layout
kbd = Keyboard(usb_hid.devices)

# Define Pins
row_pins = [board.GP0, board.GP1, board.GP2]
col_pins = [board.GP3, board.GP4, board.GP5]

# Setup Hardware Layout
rows = [digitalio.DigitalInOut(pin) for pin in row_pins]
for row in rows:
    row.direction = digitalio.Direction.OUTPUT
    row.value = True 

cols = [digitalio.DigitalInOut(pin) for pin in col_pins]
for col in cols:
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP  

keymap = [
    [Keycode.ONE,  Keycode.TWO,  Keycode.THREE],
    [Keycode.FOUR, Keycode.FIVE, Keycode.SIX],
    [Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE]
]


pressed_keys = [[False, False, False],
                [False, False, False],
                [False, False, False]]



while True:
    for r_idx, row in enumerate(rows):
        row.value = False  
        
        for c_idx, col in enumerate(cols):
          
            if not col.value:
                if not pressed_keys[r_idx][c_idx]:
                    print(f"Key pressed at Row {r_idx}, Col {c_idx}") #debugging
                    kbd.press(keymap[r_idx][c_idx])
                    pressed_keys[r_idx][c_idx] = True
            else:
            
                if pressed_keys[r_idx][c_idx]:
                    print(f"Key released at Row {r_idx}, Col {c_idx}") #debuggin
                    kbd.release(keymap[r_idx][c_idx])
                    pressed_keys[r_idx][c_idx] = False
                    
        row.value = True 
        
    time.sleep(0.01)  
