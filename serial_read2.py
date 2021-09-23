"""
Created August 5 2019
@author: jucanilu
"""
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(10,GPIO.IN)
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
y = 0
w9 = [0]
w11 = [0]
w10 = [0]
w5 = [0]
w6 = [0]
w13 = [0]
w19 = [0]

while 1:
    #x=ser.readline()
    if GPIO.input(9) == 1:
        materia=9
        print("button 10 pressed")
    if GPIO.input(11) == 1:
        materia=11
        print("button 9 pressed")
    if GPIO.input(10) == 1:
        materia=10
        print("button 11 pressed")
    if GPIO.input(5) == 1:
        materia=5
        print("button 5 pressed")
    if GPIO.input(6) == 1:
        materia=6
        print("button 6 pressed")
    if GPIO.input(13) == 1:
        materia=13
        print("button 13 pressed")
    if GPIO.input(19) == 1:
        materia=19
        print("button 19 pressed")
    else:
        x=ser.readline()
        y=x.split()[1]
        y=y.split("KG")[0]
        if materia == 9:
            w9.append(y)
            print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 11:
            w11.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 10:
            w10.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 5:
            w5.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 6:
            w6.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 13:
            w13.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))
        if materia == 19:
            w19.append(y)
            print("input 0, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (materia, y, max(w10), max(w9), max(w11), max(w5), max(w6), max(w13), max(w19)))

