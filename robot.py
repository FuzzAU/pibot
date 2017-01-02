import time

import pins
import ultrasonic
import RPi.GPIO as GPIO


print('Robot - Starting')

GPIO.setmode(GPIO.BCM)
# Set up LEDs to be output pins
GPIO.setup(pins.GREEN_LED, GPIO.OUT)
GPIO.setup(pins.BLUE_LED, GPIO.OUT)
GPIO.setup(pins.RED_LED, GPIO.OUT)
GPIO.output(pins.GREEN_LED, False)
GPIO.output(pins.BLUE_LED, False)
GPIO.output(pins.RED_LED, False)

# Setup ultrasonic sensor
ultrasonic.setup()

try:
    while True:
        distance = ultrasonic.get_distance()

        print('Distance [cm]: %f' % distance)
        # Check that the distance returned is valid. If distance returned is None
        # then we can't compare that to a number, so lets check that it's valid first
        if distance:
            if distance < 60:
                GPIO.output(pins.GREEN_LED, True)
            else:
                GPIO.output(pins.GREEN_LED, False)

            if distance < 30:
                GPIO.output(pins.BLUE_LED, True)
            else:
                GPIO.output(pins.BLUE_LED, False)

            if distance < 10:
                GPIO.output(pins.RED_LED, True)
            else:
                GPIO.output(pins.RED_LED, False)
        # Sleep for a little while so we aren't hard looping
        time.sleep(0.10)
except KeyboardInterrupt:
    # When a user presses Ctrl-C on the console it is a
    # sign they want to end the application
    GPIO.cleanup()
