import RPi.GPIO as gpio

svet = 6
knopke = 13
out     = 26


gpio.setmode(gpio.BCM)
gpio.setup(svet, gpio.IN)
gpio.setup(out, gpio.OUT)

while 1:
    gpio.output(out,gpio.input(svet))