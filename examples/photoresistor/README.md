# Photoresistor Example
Demonstrates how to detect light using a photoresistor.

## Configuration

Connect the LIS3DH to the Raspberry Pi 3 pins:
  * Vin to 5v 
  * Gnd to Gnd
  * Clock to SCL
  * Data to SDA

Connect the trim pot to power:
  * Left pin to 3.3v from LIS3DH
  * Right pin to GND
  * Middle pin to Photoresistor

Connect a resistor (10k):
  * Gnd to resistor
  * Resistor out to Photoresistor out

Connect the photoresister circuit:
  * Resistor / Photoresistor out to A1/A2/A3

![wiring diagram](https://raw.githubusercontent.com/gguuss/python-lis3dh/new-adafruit-lib/examples/photoresistor/wiring.png)

## Running the sample
* Configure all requisite modules
* Start the sample by running `python photoresistor.py`
* Cover the sensor to lower the voltage and show "Dark"
* Shine a light on the sensor to raise the voltage and show "Light"
