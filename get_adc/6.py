import smbus

import time

from matplotlib import pyplot as plt


dinamic_range  = 5.271

class set_U_num():
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)

        self.adress = 0x4D
        self.vm  = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
        self.arr =[0]

    def set_number(self, number):
        if (number > 0xFFF):
            print("num out of range")
            return 0
        fb = self.vm | self.pds | number >> 8
        sb = number & 0xFF

        self.bus.write_byte_data(self.adress, fb, sb)

            
    def get_number(self):
        data = self.bus.read_word_data(self.adress, 0)
        ld = data >> 8
        ud = data & 0xFF
        number = ud << 8 | ld

        if self.verbose:
            print(f"adress: {self.adress}\n\tfb = 0x{fb:02x}\n\tsb = 0x{sb:02x}\n")
        return number

    def put_U(self, U):
        number = int(0xFFF * U / self.dynamic_range)
        self.set_number(number)

    def get_U(self):
        number = self.get_number()

        time.sleep(0.1)
        return 0.1

    def show_U_arr(self, time_max):
        time2 = 0

        while time2 < time_max:
            timer = self.get_U()
            self.arr.append(timer)
            time2+=timer


        plt.figure(figsize=(10,6))

        plt.hist(self.arr, rwidth = 0.1)

        plt.xlim(0,0.06)

        plt.xticks([i/100 for i in range(0,60,2)], rotation = 90)

        self.deinit()
        plt.show()


    def deinit(self):
        self.bus.close()


if __name__ == "__main__":
    try:
        dac = set_U_num(5.225)
        dac.show_U_arr(3)



    finally:
        dac.deinit()