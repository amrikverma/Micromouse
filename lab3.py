# from ds28e05  import DS28E05
# from irsensor import IRSensors
# import adafruit_motor.motor as motor
# Polling - Lab 3
# Interrupt - Lab 3
    # enc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)

    # # a and b Hall effect sensors of left encoder
    # a = digitalio.DigitalInOut(board.GP12)
    # b = digitalio.DigitalInOut(board.GP13)

    # counter = 0
    # position = 0
    # a_prev = a.value

    # def leftEncoderRisingEdge():
    #     """TODO increment or decrement position depending on which way the motor is spinning
    #     Try experimenting with the instance variables of a and b (we only need either a or b). Refer to the
    #     waveform code from earlier for an idea, think about rising edges"""
    #     global position # access global position
    #     if b.value == 0 : # can be simplified lol
    #         position += 1
    #     else:
    #         position -= 1

    # while True:
    #     a_val = a.value
    #     if a_val and not a_prev: # rising edge of a
    #         leftEncoderRisingEdge()
    #     a_prev = a_val

    #     if counter % 1000 == 0:
    #         print(position)
    #     counter += 1