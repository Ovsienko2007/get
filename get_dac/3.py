import RPi.GPIO as gpio

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
        while 1:
            try:
                U = float(input("Введите напряжение в Вольтах:"))
                dac.put_U(U)
            except ValueError:
                print("это не число")
    finally:
        dac.deinit()