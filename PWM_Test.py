#!/usr/bin/python

# ChatGPT generated code to test two 12volt PWM fan control via EMC2101 from Raspberry PI 5
import board
import busio
from adafruit_emc2101 import EMC2101

i2c = busio.I2C(board.SCL, board.SDA)

fan1 = EMC2101(i2c, address=0x4C)
fan2 = EMC2101(i2C, address=0x4D)

fan1.manual_fan_speed = 50   # 50% PWM
fan2.manual_fan_speed = 100  # Full speed

print("Fan 1 RPM:", fan1.fan_speed_rpm)
print("Fan 2 RPM:", fan2.fan_speed_rpm)
