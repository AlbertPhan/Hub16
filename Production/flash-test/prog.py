#!/bin/python3

# Script to program and test Hub16

import os
import time

# Flash Device
erase = "avrdude -v -patmega32u4 -cusbasp -Pusb -e -Ulock:w:0x3F:m -Uefuse:w:0xcb:m -Uhfuse:w:0xd8:m -Ulfuse:w:0xff:m"
bootloader = "avrdude -v -patmega32u4 -cusbasp -Pusb -Uflash:w:Caterina-Leonardo.hex:i -Ulock:w:0x2F:m"
flash = "avrdude -v -patmega32u4 -cavr109 -P/dev/ttyACM0 -b57600 -D -Uflash:w:../../Firmware/binaries/hub16_default.hex:i"

os.system(erase)
os.system(bootloader)
time.sleep(1) # Delay for 32u4 to reset and enumerate
os.system(flash)

# Test Device

chars_reqd = "abcdefghijklmnopqrstuv"
chars_input = input("Press all the keys!: ")
chars_remain = ""

while True:

    for char in chars_reqd:
            if char in chars_input:
                chars_remain = chars_remain.replace(char, "")
            elif char not in chars_remain:
                chars_remain = chars_remain + char

    if len(chars_remain) == 0:
        print("ALL KEYS WORKING")
        break

    chars_reqd = chars_remain
    chars_input = input("Need to press {}: ".format(chars_remain))