import RPi.GPIO as gpio
import time

knopka_add = 9
knopka_sub = 10
num = int(0)

leds = [16,12,25,17,27,23,22,24][::-1]

gpio.setmode(gpio.BCM)

gpio.setup((knopka_add, knopka_sub), gpio.IN)
gpio.setup(leds, gpio.OUT)


def lights(num):
    for out in leds:
        gpio.output(out,num % 2)
        num //= 2
    return

lights(num)
while 1:

    if (gpio.input(knopka_add)):
        time.sleep(0.1)
        if (gpio.input(knopka_sub)):
            num = 2** len(leds) - 1
            lights(num)

            while (gpio.input(knopka_add) or gpio.input(knopka_sub)): None

        else:
            num = (num + 1) % (2** len(leds) - 1)

            lights(num)
            while (gpio.input(knopka_add)): None


    if (gpio.input(knopka_sub)):
        time.sleep(0.1)
        if (gpio.input(knopka_add)):
            num = 2** len(leds) - 1
            lights(num)

            while (gpio.input(knopka_add) or gpio.input(knopka_sub)): None

        else:
            num = (num - 1) % (2** len(leds) - 1)
            lights(num)
            while (gpio.input(knopka_sub)): None


        
