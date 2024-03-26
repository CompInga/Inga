import RPi.GPIO as GPIO

pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)

p.start(0)

try:
    while(1):
        x = int(input())
        if x>100 or x<0:
            print('Неверное значение')
            break
        p.ChangeDutyCycle(x)
        print("Вольтаж: ", 3.3*x/100)

finally:
    p.stop()
    GPIO.output(pin,0)
    GPIO.cleanup()