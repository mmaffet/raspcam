
import time # so we can use "sleep" to wait between actions
import RPi.GPIO as io # import the GPIO library we just installed but call it "io"
#from ISStreamer.Streamer import Streamer # import the IS Streamer we just installed but call it "Streamer"
## cam startup at 640x480
## raspistill --nopreview -w 640 -h 480 -q 5 -o /media/pi/KINGSTON/pic.jpg -tl 0 -t 9999999 -th 0:0:0 & 
## MJPG STREAMER START, can be changed on /tmp/stream to another drive example like a pendrive to not overload de sd drive
## LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /media/pi/KINGSTON -n pic.jpg" -o "output_http.so -w /usr/local/www"

## set GPIO mode to BCM
## this takes GPIO number instead of pin number
io.setmode(io.BCM)

## enter the number of whatever GPIO pin you're using
door_pin = 23
buzz_pin = 22

## use the built-in pull-up resistor
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp


## initialize door 
door=0

## this loop will execute the if statement that is true
while True:
	## if the switch is open
	if io.input(door_pin):
		print("Door Open") # stream a message saying "Open"
##		logger.flush() # send the message immediately
		door=0 # set door to its initial value
		io.setup(buzz_pin,io.OUT)
		time.sleep(1) # wait 1 second before the next action
	## if the switch is closed and door does not equal 1
	if (io.input(door_pin)==False and door!=1):
		print("Door Close") # stream a message saying "Close"
		
		door=1 # set door so that this loop won't act again until the switch has been opened