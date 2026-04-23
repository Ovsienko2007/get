import RPi.GPIO as gpio
import time
import math

dinamic_range  = 3.305

class R2R_DAC():
    def __init__(self, gpio_bits, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_bits     = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose       = verbose
        self.pwm_frequency = pwm_frequency

        gpio.setmode(gpio.BCM)

        gpio.setup(self.gpio_bits, gpio.OUT)
        self.pwm  = gpio.PWM(gpio_bits, pwm_frequency)
        self.pwm.start(0)

    def voltage_to_num(self, U):
        if not (0.0 <= U <= self.dynamic_range):
            print(f"Напряжение выходит за заданный диапазон ЦАП (0.00 - {dinamic_range:.2f})D\n" + 
                    "Устанавливаем 0 В")
            return 0
        return U / self.dynamic_range * 100
    
    def put_U(self, U):
        U_num = self.voltage_to_num(U)
        self.pwm.ChangeDutyCycle(U_num)

    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        gpio.cleanup()

if __name__ == "__main__":
    try:
        dac = R2R_DAC(12, 500, dinamic_range, True)
        sig_freq = 10
        sampl_freq = 1000
        max_U = dinamic_range
        t = 0

        while 1:
            U = max_U * (1 + math.sin(2 * 3.1415926535 / sampl_freq * t)) / 2
            dac.put_U(U)

            time.sleep(1 / sig_freq)
            t += 10

    finally:
        dac.deinit()