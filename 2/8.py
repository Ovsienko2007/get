import RPi.GPIO as gpio
import time

dinamic_range  = 3.192

dac_bits = [16,20,21,25,26,17,27,22][::-1]

gpio.setmode(gpio.BCM)

gpio.setup(dac_bits, gpio.OUT)

def func(freq):
    U = 0
    while 1:
        if (U < 1 / freq):
            is_up = True
        if (U > 1 - 1 / freq):
            is_up = False

        if is_up:
            U += 1 / freq
        else:
            U -= 1 / freq
        yield U

class R2R_DAC():
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode(gpio.BCM)

        gpio.setup(self.gpio_bits, gpio.OUT)

    def voltage_to_num(self, U):
        if not (0.0 <= U <= self.dynamic_range):
            print(f"Напряжение выходит за заданный диапазон ЦАП (0.00 - {dinamic_range:.2f})D\n" + 
                    "Устанавливаем 0 В")
            return 0
        return int(U / self.dynamic_range * 255 + 0.5)

    def lights(self, num):
        for out in self.gpio_bits:
            gpio.output(out,num % 2)
            num //= 2
        return
    
    def put_U(self, U):
        U_num = self.voltage_to_num(U)
        self.lights(U_num)

if __name__ == "__main__":
    try:
        dac = R2R_DAC(dac_bits, dinamic_range, True)
        sig_freq = 10
        sampl_freq = 100
        max_U = 3
        t = 0
        gen_U = func(sampl_freq)

        while 1:
            U = max_U * next(gen_U)
            dac.put_U(U)

            time.sleep(1 / sig_freq)

    finally:
        gpio.output(dac_bits,0)
        gpio.cleanup()

