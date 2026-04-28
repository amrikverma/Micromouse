import board
import time

import digitalio
import neopixel
import rotaryio
import pwmio
from analogio import AnalogIn

# from ds28e05  import DS28E05
from irsensor import IRSensors
import adafruit_motor.motor as motor

""" Peripherals """

l_adc = AnalogIn(board.GP28)

# emitter 
l_en = digitalio.DigitalInOut(board.GP7)
l_en.direction = digitalio.Direction.OUTPUT
l_en.value = False

# sensors
lir_a = digitalio.DigitalInOut(board.GP5)
lir_a.direction = digitalio.Direction.OUTPUT
lir_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
lir_a.value = True # high Z mode

lir_b = digitalio.DigitalInOut(board.GP6)
lir_b.direction  = digitalio.Direction.OUTPUT
lir_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN
lir_b.value = True

'''Main'''

if __name__ == "__main__":
    while True:
        # TODO enable IR emitters using l_en set one of its variables to a (boolean)
        l_en.value = True

        # TODO enable chosen sensor lir_a or lir_b by setting one of its variable to false
        lir_a.value = False
        # TODO wait a bit, 1ms should do time. ...
        time.sleep(0.001)
        # TODO take analog reading for future printing print(l_adc. , end=" ")
        print(l_adc.value, end=" ")
        # TODO disable chosen sensor lir_a or lir_b 
        lir_a.value = True

        # TODO try for lir_b or lir_a whichever one you didnt use instead, enable chosen sensor etc
        lir_b.value = False
        time.sleep(0.001)
        print(l_adc.value, end=" ")
        lir_b.value = True
        # TODO disable IR emitters using l_en 
        l_en.value = False
        time.sleep(0.05)
'''import board
import time

import digitalio
import neopixel
import rotaryio
import pwmio
from analogio import AnalogIn

# from ds28e05  import DS28E05
from irsensor import IRSensors
import adafruit_motor.motor as motor

""" Peripherals """

ir = IRSensors(
    board.GP7,  board.GP5,  board.GP6,  board.GP28, # left
    board.GP9,  board.GP10, board.GP11, board.GP26, # center
    board.GP21, board.GP20, board.GP22, board.GP27  # right
)


if __name__ == "__main__":
    while True:
        ir.scan()
        print("lir_a:", ir.lir_a, "\t", "lir_b:", ir.lir_b, "\t",
            "cir_a:", ir.cir_a, "\t", "cir_b:", ir.cir_b, "\t",
            "rir_a:", ir.rir_a, "\t", "rir_b:", ir.rir_b)
        time.sleep(0.05)'''