import RPi.GPIO as GPIO
import time
from time import sleep     # this lets us have a time delay

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(10, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(9, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(11, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(5, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(6, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(13, GPIO.IN)    # set GPIO 25 as input
GPIO.setup(19, GPIO.IN)    # set GPIO 25 as input

counter_10 = 0
counter_9 = 0
counter_11 = 0
counter_5 = 0
counter_6 = 0
counter_13 = 0
counter_19 = 0

print "Press a Button"

while True:
    if GPIO.input(10) == 1 and counter_10 >= 0:
        counter_10 = counter_10 + 1
        print "GPIO 10"#counter_10
        time.sleep(.2)
    if GPIO.input(19) == 1 and counter_19 >= 0:
        counter_19 = counter_19 + 1
        print "GPIO 19"#counter_19
        time.sleep(.2)
    else:
        print "NOT"
        time.sleep(1)
'''
        if GPIO.input(10): # if port 25 == 1
            print "Port 10 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(9): # if port 25 == 1
            print "Port 9 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(11): # if port 25 == 1
            print "Port 11 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(5): # if port 25 == 1
            print "Port 5 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(6): # if port 25 == 1
            print "Port 6 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(13): # if port 25 == 1
            print "Port 13 is 1/GPIO.HIGH/True - button pressed"
        if GPIO.input(19): # if port 25 == 1
            print "Port 19 is 1/GPIO.HIGH/True - button pressed"
        else:
            print "Port NOT is 0/GPIO.LOW/False - button not pressed"
        sleep(0.1)         # wait 0.1 seconds
except KeyboardInterrupt:

'''
GPIO.cleanup()         # clean up after yourself
