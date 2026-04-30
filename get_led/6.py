import RPi.GPIO as gpio
import time

svet   = 6
knopka = 13
out     = 26
need_light = 0


gpio.setmode(gpio.BCM)
gpio.setup(knopka, gpio.IN)
gpio.setup(out, gpio.OUT)

pwm  = gpio.PWM(out, 200)
duty = 0.0
pwm.start(0)


while 1:
    pwm.ChangeDutyCycle(duty)
    duty = (duty + 1) % 101
    time.sleep(0.05)
    