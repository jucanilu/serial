"""
Created August 5 2019
@author: jucanilu
"""
#!/usr/bin/env python
#import RPi.GPIO as GPIO
import time
import datetime
#import serial
import sys
import csv
import os
from time import sleep, strftime, time

#Variables globales:
m = 0       #materia
m2 = 0      #banderaCalcio
s = "ST"    #stable
wm2 = [0]   #banderaCalcio

w9 = [0]
w11 = [0]
w10 = [0]
w5 = [0]
w6 = [0]
w13 = [0]
w19 = [0]

e9 = 0
e11 = 0
e10 = 0
e5 = 0
e6 = 0
e13 = 0
e19 = 0
em2 = 0
e100 = 0

#Timing and CSV file creation
now = datetime.datetime.now()
#logPath = "/home//serial/logs/"
logPath = "/Users/jcniebla/serial/logs/"
FileName = ""
FileName = str("_".join(str(datetime.datetime.now()).split(" ")))
FileName = str("_".join(FileName.split(":")))
FileName = str("_".join(FileName.split(".")))
FileName = str("_".join(FileName.split("-")))
FileName = logPath + FileName + ".csv"
file = open(FileName,"w")
file.write("Date, Button, Y, m1, m2, m3, m4,m5, m6, m7, M1, M2, M3, M4, M5, M6, M7, M8(NUCLEO) \r\n")

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(9,GPIO.IN)
        GPIO.setup(11,GPIO.IN)
        GPIO.setup(10,GPIO.IN)
        GPIO.setup(5,GPIO.IN)
        GPIO.setup(6,GPIO.IN)
        GPIO.setup(13,GPIO.IN)
        GPIO.setup(19,GPIO.IN)

def serial():
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    x=ser.readline()
    y=x.split()[1]
    y=y.rsplit("KG")[0]
    print(int(y))

def loop():
        while True:
                if GPIO.input(9) == 1:
                    m=9
                    print("button 9 pressed - sorgo")
                if GPIO.input(10) == 1:
                    m=10
                    print("button 10 pressed - soya integral")
                if GPIO.input(11) == 1:
                    m=11
                    print("button 11 pressed - sorgo")
                if GPIO.input(5) == 1:
                    m=5
                    print("button 5 pressed - soya normal")
                if GPIO.input(6) == 1:
                    m=6
                    print("button 6 pressed - grano destilado")
                if GPIO.input(13) == 1:
                    m=13
                    print("button 13 pressed - soya integral")
                if GPIO.input(19) == 1:
                    m=19
                    print("button 19 pressed - calcio fino")
                    wm2.append(y)
                    print("wm2.append(y) <--- function")
                else:
                    print(int(y))
                    if int(y) < 1 and max(w19) > 0:

                        e11 = int(max(w11))                     #10
                        #e9 = int(max(w9)) - int(max(w11))      #11
                        e10 = int(max(w10)) - int(max(w11))     #12
                        #e13 = int(max(w13)) - int(max(w10))    #13
                        e6 = int(max(w6)) - int(max(w10))       #14
                        e5 = int(max(w5)) - int(max(w6))        #15
                        em2 = int(max(wm2)) - int(max(w5))
                        e19 = int(max(w19)) - int(max(wm2))     #16
                        e100 = 1000 - int(max(w19))             #17

                        print("i1,%s,%s, %s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w10),max(w6),max(w5),max(wm2),max(w19),e11,e10,e6,e19,e5,e100))
                        file.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17}\n".format(strftime("%Y-%m-%d %H:%M:%S"),int(m),int(y),max(w9),max(w11),max(w10),max(w13),max(w6),max(w5),max(wm2),max(w19),e11,e10,e6,e5,em2,e19,e100))
                        file.flush()
                        sleep(1)
                        w11 = [0]
                        w9 = [0]
                        w10 = [0]
                        w13 = [0]
                        w6 = [0]
                        w19 = [0]
                        w5 = [0]
                        wm2 = [0]
                    if m == 9 or m == 11 and s == "ST": #sorgo
                        w9.append(y)
                        w11.append(y)
                        print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19),max(wm2)))
                    if m == 10 or m == 13 and s == "ST": #soya integral
                        w10.append(y)
                        w13.append(y)
                        print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19),max(wm2)))
                    if m == 5 and s == "ST":
                        w5.append(y)
                        print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19),max(wm2)))
                    if m == 6 and s == "ST":
                        w6.append(y)
                        print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19),max(wm2)))
                    if m == 19 and s == "ST":
                        w19.append(y)
                        print("i0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (m,y,max(w11),max(w9),max(w10),max(w13),max(w6),max(w5),max(w19),max(wm2)))

def endprogram():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        serial()
        loop()
    except KeyboardInterrupt:
        print("KeyboardInterrupt Detected")
        endprogram()
