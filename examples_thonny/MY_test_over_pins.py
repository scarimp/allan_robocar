#esempio_mio  21-03-2019

import machine
from time import sleep

pin12 = machine.Pin(12, machine.Pin.OUT)
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
#addr = 5000
#i2c.writeto(addr, b'1234')
#i2c.readfrom(addr, 4)
while True:
    pin12.value(not pin12.value())
    print(pin12.value())
    sleep(1)
