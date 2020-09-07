import RPi.GPIO as gpio
import time


def distance(measure='cm'):

    gpio.setmode(gpio.BOARD)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.IN)

#PIN 23 --> 16 is the trig
#PIN 24 --> 18  is the echo

    #ensure that the trig is set low

    print("Distance measurement is in progress")
    gpio.output(16, False)
    time.sleep(2)


    gpio.output(16, True)
    time.sleep(0.00001)
    gpio.output(16, False)

    while gpio.input(18) == 0:
        nosig = time.time()

    while gpio.input(18) == 1:
        sig = time.time()

    t1 = sig - nosig

    if measure == 'cm':
        distance = t1  * 17150
        distance = round(distance, 2)

    elif distance == 'in':
        distance = t1/ 0.000148
        distance = round(distance, 2)
    else:
        print("Improper measurement")


    gpio.cleanup()
    return distance

print(distance('cm'))

