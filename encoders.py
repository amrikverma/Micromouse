import board
import time
import digitalio

# a and b Hall effect sensors of left encoder
a = digitalio.DigitalInOut(board.GP12)
b = digitalio.DigitalInOut(board.GP13)

while True:
    print(int(a.value), int(b.value))
    time.sleep(0.001)