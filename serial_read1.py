"""
Created August 5 2019
@author: jucanilu
"""
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setup(10,GPIO.IN)
GPIO.setup(9,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.IN)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0
materia=0
st="ST"
w = []

while 1:
    x=ser.readline()
    st=x.split(",")[0]
    if len(x.strip()) == 0:
        time.sleep(0.1)
        #print (x)
    if GPIO.input(10) == 1:
        materia=10
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        w.append(y)
        print(w)
        print("maxvalue: ", max(w))
        print("button 10 pressed")
        print("input 10, %s, %s" % (materia, y))
    if GPIO.input(9) == 1:
        materia=9
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        print("button 9 pressed")
        print("input 9,  %s, %s" % (materia, y))
    if GPIO.input(11) == 1:
        materia=11
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        print("button 11 pressed")
        print("input 11, %s, %s" % (materia, y))
    if GPIO.input(5) == 1:
        materia=5
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        print("button 5 pressed")
        print("input 5, %s, %s" % (materia, y))
    if GPIO.input(6) == 1:
        materia=6
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        print("button 6 pressed")
        print("input 6, %s, %s " % (materia, y))
    if GPIO.input(13) == 1:
        materia=13
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        print("input 13, %s, %s" % (materia, y))
    if GPIO.input(19) == 1:
        materia=19
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        
        print("input 19, %s, %s" % (materia, y))
    else:
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        time.sleep(1)
        print("input 0, %s, %s" % (materia, y))
