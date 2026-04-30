import RPi.GPIO as gpio
import time

svet   = 6
knopka = 13
out    = 26
time_sleep = float(input())

gpio.setmode(gpio.BCM)
gpio.setup(svet, gpio.IN)
gpio.setup(out, gpio.OUT)

while 1:
    gpio.output(out, 1)
    time.sleep(time_sleep)
    gpio.output(out, 0)
    time.sleep(time_sleep)