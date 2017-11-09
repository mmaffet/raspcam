import RPi.GPIO as io
io.setmode(io.BCM)
door_pin = 23
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

def estado():
    if io.input(door_pin):
        #Puerta Abierta
        return True
    if (io.input(door_pin)==False):
        #Puerta Cerrada
        return False
    
        

