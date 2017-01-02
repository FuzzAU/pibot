"""
This file maps BCM pin numbers to names to use in code
To help understand the pinouts, see https://pinout.xyz/

It is possible to also use board numbering if GPIO mode is GPIO.BOARD
See http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
for more info
"""

# LEDs
GREEN_LED = 8       # Pin 24
BLUE_LED = 7        # Pin 26
RED_LED = 1         # Pin 28

# Ultrasonic sensor
ULTRASONIC_TRIG = 23        # Pin 16
ULTRASONIC_ECHO = 24        # Pin 18

