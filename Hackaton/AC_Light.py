from machine import ADC, Pin
import time

p0 = Pin(32, Pin.OUT)
p0.value(1)

estado = False

p1 = Pin(36, Pin.IN, Pin.PULL_UP)


while True:

    if(p1.value()):
        if(estado):
            estado = 0
        else:
            estado = 1
            
        p0.value(estado)
        print(estado)
        time.sleep_ms(200)
