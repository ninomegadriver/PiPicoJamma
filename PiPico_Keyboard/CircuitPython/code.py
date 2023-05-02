# RaspberryPi Pico Keyboard code for use with "PiPico Jamma":
# https://github.com/ninomegadriver/PiPicoJamma
#
# Nino MegaDriver, 2022
# nino@nino.com.br
# http://www.megadriver.com.br
#
# Key mappings according to Mame's default keys.
# Bear in mind that Mame dosen't have default keys
# for Player2 button 6 and Advance Mame dosen't have
# defaults for Player2 buttons 4, 5 and 6.
# You'll have to configure these on Mame according
# to this Code
#
# Code derived from:
# https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/code-the-pico-keyboard
# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

# Hold your horses!
# We have to put the device to sleep to give some time
# for the Host PI to boot, otherwise it won't be recognized
time.sleep(10)

import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

pins = (
    board.GP0,    # 0:  Service
    board.GP1,    # 1:  Test
    board.GP2,    # 2:  COIN2
    board.GP3,    # 3:  COIN1
    board.GP4,    # 4:  P2 START
    board.GP5,    # 5:  P1 START
    board.GP6,    # 6:  P2 UP
    board.GP7,    # 7:  P1 UP
    board.GP8,    # 8:  P2 DOWN
    board.GP9,    # 9:  P1 DOWN
    board.GP10,   # 10: P2 LEFT
    board.GP11,   # 11: P1 LEFT
    board.GP12,   # 12: P2 RIGHT
    board.GP13,   # 13: P1 RIGHT
    board.GP14,   # 14: P2 BTN1
    board.GP15,   # 15: P1 BTN1
    board.GP16,   # 16: P2 BTN6
    board.GP17,   # 17: P2 BTN5
    board.GP18,   # 18: P2 BTN4
    board.GP19,   # 19: P1 BTN6
    board.GP20,   # 20: P1 BTN5
    board.GP21,   # 21: P1 BTN4
    board.GP22,   # 22: P1 BTN3
    board.GP26,   # 23: P2 BTN3
    board.GP27,   # 24: P1 BTN2
    board.GP28    # 25: P2 BTN2
)

KEY = 2

keymap = {
    (0): (KEY, [Keycode.F2]),              # SERVICE
    (1): (KEY, [Keycode.NINE]),            # TEST
    # Player 1
    (3): (KEY, [Keycode.FIVE]),            # COIN1
    (5): (KEY, [Keycode.ONE]),             # P1 START
    (7): (KEY, [Keycode.UP_ARROW]),        # P1 UP
    (9): (KEY, [Keycode.DOWN_ARROW]),      # P1 Down
    (11): (KEY, [Keycode.LEFT_ARROW]),     # P1 LEFT
    (13): (KEY, [Keycode.RIGHT_ARROW]),    # P1 RIGHT
    (15): (KEY, [Keycode.LEFT_CONTROL]),   # P1 BTN1
    (24): (KEY, [Keycode.LEFT_ALT]),       # P1 BTN2
    (22): (KEY, [Keycode.SPACE]),          # P1 BTN3
    (21): (KEY, [Keycode.LEFT_SHIFT]),     # P1 BTN4
    (20): (KEY, [Keycode.Z]),              # P1 BTN5
    (19): (KEY, [Keycode.X]),              # P1 BTN6
    # Player 2
    (2): (KEY, [Keycode.SIX]),             # COIN2
    (4): (KEY, [Keycode.TWO]),             # P2 START
    (6): (KEY, [Keycode.R]),               # P2 UP
    (8): (KEY, [Keycode.F]),               # P2 Down
    (10): (KEY, [Keycode.D]),              # P2 LEFT
    (12): (KEY, [Keycode.G]),              # P2 RIGHT
    (14): (KEY, [Keycode.A]),              # P2 BTN1
    (25): (KEY, [Keycode.S]),              # P2 BTN2
    (23): (KEY, [Keycode.Q]),              # P2 BTN3
    (18): (KEY, [Keycode.W]),              # P2 BTN4
    (17): (KEY, [Keycode.E]),              # P2 BTN5
    (16): (KEY, [Keycode.H]),              # P2 BTN6
}

switches = []
for i in range(len(pins)):
    switch = DigitalInOut(pins[i])
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    switches.append(switch)


switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


while True:
    for button in range(len(pins)):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                    else:
                        cc.send(keymap[button][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])

                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)  # debounce
