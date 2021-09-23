"""
Created August 5 2019
@author: jucanilu
"""
#!/usr/bin/env python
import time
import serial
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter=0

while 1:
    x=ser.readline()
    s=x.split(",")[0]
    if len(x.strip()) > 0:
        y=x.split()[1]
        y=y.split("KG")[0]
        print(y)
    else:
        time.sleep(0.1)
