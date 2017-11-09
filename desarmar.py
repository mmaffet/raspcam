import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
buzz_pin = 22
io.setup(buzz_pin,io.OUT)
io.output(buzz_pin,False)
io.cleanup()
