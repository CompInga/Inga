import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]

def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

x = 0
a = 1
T = input()

try:
    while(True):
        
        try:
            T = int(T)
            GPIO.output(dac, dec2bin(x))
            time.sleep(T/512)
            if (x == 255): 
                a = -1
            if (x == 0): 
                a = 1
            x += a
        except:
            break    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")