import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print((volume,))

    for j in range (0,11):
        leds[j].value = 0

    tempvol = 22000
    for i in range(0,11):
        if volume > (tempvol + 2000):
            leds[i].value = 1
            tempvol += 2000





    sleep(0.01)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
