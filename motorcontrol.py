import board
import pwmio
import time

lmot_in1 = pwmio.PWMOut(board.GP16, frequency = 20000) # 20kHz
lmot_in2 = pwmio.PWMOut(board.GP17, frequency = 20000)
if __name__ == "__main__":
    while True:
        # forward:
        lmot_in1.duty_cycle = int(0.10 * 65535) # set to 25% speed forward should be an int
        lmot_in2.duty_cycle = 65535
        time.sleep(5)

        #backward
        lmot_in1.duty_cycle = 65535
        lmot_in2.duty_cycle = int(0.10 * 65535)
        time.sleep(5)