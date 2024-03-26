import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input()
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"{voltage:.4} В")
            else:
                if num < 0:
                    print("Введите число больше 0")
                elif num > 255:
                    print("Введите число меьше 256")  
        except:
            if num == 'q': break
            else:
                print("Это не число")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
