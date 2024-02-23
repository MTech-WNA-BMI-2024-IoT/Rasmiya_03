import smbus
import time

# Define the I2C address of the BH1750 sensor
BH1750_ADDR = 0x23

# Create an I2C bus object
bus = smbus.SMBus(1)

# Read the light intensity from the sensor
light_intensity = bus.read_i2c_block_data(BH1750_ADDR, 0x00, 2)

# Convert the light intensity from a 16-bit value to a lux value
lux = light_intensity[0] << 8 | light_intensity[1]

# Print the light intensity to the console
print("Light intensity:", lux, "lux")

# Wait for 1 second before reading the light intensity again
time.sleep(1)
