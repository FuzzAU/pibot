import pins
import time
import RPi.GPIO as GPIO

# Amount of time to make sure ultrasonic sensor trigger is held low before starting
# Note: we may not actually need this
SLEEP_TIME_BEFORE_START = 0.05
# Amount of time to hold trigger line high to ensure ultrasonic sensor sees our request
TRIGGER_HIGH_TIME = 0.00001


def setup():
    """
    Run this function once at the start of the program to setup the pins for
    the ultra sonic scanner
    """
    GPIO.setup(pins.ULTRASONIC_TRIG, GPIO.OUT)
    GPIO.setup(pins.ULTRASONIC_ECHO, GPIO.IN)


def get_distance():
    """
    This funciton will request a sensor measurement from the ultrasonic scanner,
    wait for it to respond and then return the distance measurement in centimeters
    :return: distance measured by ultrasonic sensor in centimeters
    """
    GPIO.output(pins.ULTRASONIC_TRIG, False)
    time.sleep(SLEEP_TIME_BEFORE_START)

    GPIO.output(pins.ULTRASONIC_TRIG, True)
    time.sleep(TRIGGER_HIGH_TIME)
    GPIO.output(pins.ULTRASONIC_TRIG, False)

    wait_count = 0
    working = True

    while GPIO.input(pins.ULTRASONIC_ECHO) == 0:
        if wait_count > 100000:
            working = False
        continue

    if not working:
        print('Oops, something went wrong waiting for echo to go high')
        return None

    pulse_start = time.time()

    wait_count = 0
    working = True
    while GPIO.input(pins.ULTRASONIC_ECHO) == 1:
        if wait_count > 100000:
            working = False
        continue

    if not working:
        print('Oops, something went wrong waiting for echo to go low')
        return None
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
