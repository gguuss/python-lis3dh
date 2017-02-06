#!/usr/bin/python

# Add the module root path until it's a proper library
import sys
sys.path.append("../../")

from LIS3DH import LIS3DH
from time import sleep

# Trim to a good voltage threshold
LOW_THRESH = 900
HIGH_THRESH = 1400

def light(val):
    if val == LOW_THRESH:
        return 'DARK'
    if val > HIGH_THRESH:
        return 'LIGHT'
    return 'FLOAT'

if __name__ == '__main__':
    sensor = LIS3DH(debug=True)
    sensor.setRange(LIS3DH.RANGE_2G)

    while True:
        a1 = sensor.getADC(sensor.ADC_1)
        a2 = sensor.getADC(sensor.ADC_2)
        a3 = sensor.getADC(sensor.ADC_3)
        print("\r1: %s\t2: %s\t3: %s" % (light(a1),light(a2), light(a3)))
        sleep(0.1)
