import RPi.GPIO as gpio
import time

leds = [16,12,25,17,27,23,22,24]

gpio.setmode(gpio.BCM)


gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

leds.extend(leds[::-1])


while 1:
    for out in leds:
        gpio.output(out, 1)
        time.sleep(0.1)
        gpio.output(out, 0)
        time.sleep(0.1)
    