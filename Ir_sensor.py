import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin used for the sensor
SENSOR_PIN = 17

# Set the sensor pin as input
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        # Read the sensor value
        sensor_value = GPIO.input(SENSOR_PIN)

        # Print the sensor value
        print("Sensor value:", sensor_value)

        # Wait for a short duration before reading again
        time.sleep(0.5)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
