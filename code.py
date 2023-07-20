import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar
import time
import neopixel

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

dot[0] = (160, 32, 240)

# Button 4
analog_in = AnalogIn(board.A1)

analog_in_2 = AnalogIn(board.A0)


def getVoltage(pin):
    return (pin.value * 3.3) / 65535


while True:

    currVoltage = getVoltage(analog_in)
    currVoltage2 = getVoltage(analog_in_2)


    try:
        #print("Pin value: ", analog_in.value)
        print(currVoltage, currVoltage2)
        #print(currVoltage)
        time.sleep(0.25)

    except RuntimeError:
        print("Retrying!")
        time.sleep(0.1)
