import board
import time
import digitalio
from analogio import AnalogIn

# l_en  = """TODO create DigitalInOut output on GP7"""
l_en = digitalio.DigitalInOut(board.GP7)
l_en.direction = digitalio.Direction.OUTPUT
l_en.drive_mode = digitalio.DriveMode.PUSH_PULL
# l_adc = """TODO create AnalogIn on GP28"""
l_adc = AnalogIn(board.GP28)

l_a   = digitalio.DigitalInOut(board.GP5)
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

# l_b = """TODO create DigitalInOut on GP6 in open-drain mode"""
# l_b = digitalio.DigitalInOut(board.GP6)
# l_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN

while True:
    # TODO enable IR emitters using l_en
    l_en.value = True

    # TODO enable chosen sensor l_a or l_b
    l_a.value = False

    # TODO wait a bit
    time.sleep(0.001)

    # TODO take analog reading for future printing
    print(l_adc.value)

    # TODO disable chosen sensor l_a or l_b
    l_a.value = True

    # TODO disable IR emitters using l_en
    l_en.value = False
    time.sleep(0.05)