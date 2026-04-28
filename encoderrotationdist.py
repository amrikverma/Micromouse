import board
import time
import rotaryio
from math import pi

lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

ENCODER_TICKS_PER_REVOLUTION = 360
WHEELBASE_DIAMETER = 82.55 #mm
WHEEL_DIAMETER = 34.0 # mm

if __name__ == "__main__":
    while True:

        left_dist  = lenc.position * WHEEL_DIAMETER * pi / ENCODER_TICKS_PER_REVOLUTION
        right_dist = renc.position * WHEEL_DIAMETER * pi / ENCODER_TICKS_PER_REVOLUTION

        dist  = (left_dist + right_dist)/2.0
        theta = (right_dist - left_dist)/WHEELBASE_DIAMETER

        print(dist, theta)
        time.sleep(0.05)