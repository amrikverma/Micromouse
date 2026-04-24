import board
import time

import digitalio
import neopixel
import rotaryio
import pwmio
from analogio import AnalogIn
# adc 
l_adc = analogio.AnalogIn(board.GP28)
#"""TODO call AnalogIn on GP28"""

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
# from ds28e05  import DS28E05
from irsensor import IRSensors
import adafruit_motor.motor as motor


""" Main """

if __name__ == "__main__":
    # Interrupt - Lab 3
    enc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)

    while True:
        l_en.value = True
        lir_a.value = False
        time.sleep(0.001)

        print("l_adc.value:", l_adc.value, end = " ")

        lir_a.value = True

    # TODO try for lir_b or lir_a whichever one you didnt use instead, enable chosen sensor etc

    # Repeat above for this sensor

    # TODO disable IR emitters using l_en 
        l_en.value = False
        time.sleep(0.05)