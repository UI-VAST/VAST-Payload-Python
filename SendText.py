# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# pylint: disable=wrong-import-position
import time

import GPSLogger
from GPSLogger import *
# CircuitPython / Blinka
import board

import serial
#uart = serial.Serial("/dev/serial0", 19200)
uart = serial.Serial("/dev/serial0", 9600)
#uart = board.UART()
#uart.baudrate = 19200

# via USB cable
# import serial
# uart = serial.Serial("/dev/ttyUSB0", 19200)

from adafruit_rockblock import RockBlock

rb = RockBlock(uart)

time.sleep(8)
while 1:
    # set the text
    print("Setting Text...")
    rb.text_out = GetLatestGPS()

    # try a satellite Short Burst Data transfer
    print("Talking to satellite...")
    status = rb.satellite_transfer()
    # loop as needed
    retry = 0
    while status[0] > 8:
        time.sleep(10)
        status = rb.satellite_transfer()
        print(retry, status)
        rb.text_out = GetLatestGPS()
        retry += 1

    print("\nSent!")
    time.sleep(180) #Sleep for 3 minutes
