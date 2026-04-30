import RPi.GPIO as gpio

svet   = 6
knopka = 10
out     = 26
need_light = 0


gpio.setmode(gpio.BCM)
gpio.setup(knopka, gpio.IN)
gpio.setup(out, gpio.OUT)

while 1:
    if (gpio.input(knopka)):
        need_light = 1 - need_light
        gpio.output(out, need_light)
        #time.sleep(0.2)
        while (gpio.input(knopka)): None
    