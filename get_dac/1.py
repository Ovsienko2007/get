import RPi.GPIO as gpio

dinamic_range  = 3.0

dac_bits = [16,20,21,25,26,17,27,22][::-1]

gpio.setmode(gpio.BCM)

gpio.setup(dac_bits, gpio.OUT)

def voltage_to_num(U):
    if not (0.0 <= U <= dinamic_range):
        print(f"Напряжение выходит за заданный диапазон ЦАП (0.00 - {dinamic_range:.2f})D\n" + 
                "Устанавливаем 0 В")
        return 0
    return int(U / dinamic_range * 255)

def lights(num):
    for out in dac_bits:
        gpio.output(out,num % 2)
        num //= 2
    return

try:
    while 1:
        try:
            U = float(input("Введите напряжение в Вольиах:"))
            U_num = voltage_to_num(U)
            lights(U_num)
        except ValueError:
            print("это не число")
finally:
    gpio.output(dac_bits,0)
    gpio.cleanup()