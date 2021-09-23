"""
Created August 5 2019
@author: jucanilu
"""
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import serial
from time import sleep, strftime, time

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

m = 0 #materia
s = "ST" #stable
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
        m=9
        #print("button 10 pressed")
    if GPIO.input(11) == 1:
        m=11
        #print("button 9 pressed")
    if GPIO.input(10) == 1:
        m=10
        #print("button 11 pressed")
    if GPIO.input(5) == 1:
        m=5
        #print("button 5 pressed")
    if GPIO.input(6) == 1:
        m=6
        #print("button 6 pressed")
    if GPIO.input(13) == 1:
        m=13
        #print("button 13 pressed")
    if GPIO.input(19) == 1:
        m=19
        #print("button 19 pressed")
    else:
        x=ser.readline()
        s=x.split(",")[0]
        if s == "ST":
            y=x.strip()
            y=x.split()[1]
            y=y.rsplit("KG")[0]
            with open("/home/pi/serial/logs/materia.csv", "a") as log:
                log.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(m),str(y),max(w10),max(w9),max(w11),max(w13),max(w6),max(w5),max(w19)))
        #if m == 9 and s == "ST":
        #    w9.append(y)
        #    print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        #if m == 11 and s == "ST":
        #    w11.append(y)
        #    print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        if m == 10 and s == "ST":
            w10.append(y)
            print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        if m == 5 and s == "ST":
            w5.append(y)
            print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        if m == 6 and s == "ST":
            w6.append(y)
            print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        if m == 13 and s == "ST":
            w13.append(y)
            print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
        #if m == 19 and s == "ST":
        #    w19.append(y)
        #    print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19)))
